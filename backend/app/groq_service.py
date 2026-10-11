"""Sheharnaama — Groq AI Service integration.

Handles all AI requests for "Ask Pune — Read Closer", including:
- Conversational cultural companion queries (POST /api/chat)
- Place card summaries (POST /api/summarize)
- Verified knowledge grounding
- Robust error handling, rate limiting, and in-memory summary caching
"""

import logging
from typing import Any

from . import config, knowledge

logger = logging.getLogger("sheharnaama.groq")

SYSTEM_PROMPT = (
    "You are Ask Pune — Read Closer, the cultural companion of SHEHARNAAMA: The City Between the Landmarks.\n\n"
    "Help users understand Pune through its crafts, printing, markets, food culture and everyday neighbourhood character.\n\n"
    "Speak warmly, clearly and concisely. Respond in the language the user uses, including English, Hindi or Hinglish. "
    "Encourage curiosity and help users notice details they may have overlooked.\n\n"
    "Use the supplied verified knowledge base as your primary source of factual information. "
    "Never invent historical facts, dates, locations, business details, traditions or citations. "
    "If the supplied information does not support an answer, clearly acknowledge that limitation.\n\n"
    "You represent a contemporary, respectful brand rooted in Pune's local character. "
    "Avoid generic tourism clichés, exaggerated claims and repetitive marketing slogans.\n\n"
    "The approved tour package is fixed. Never invent routes, timings, prices, availability, inclusions or tour activities. "
    "You are a cultural information assistant, not a booking confirmation system."
)

# In-memory summary cache: key -> {"summary": str, "sources": list, "model": str}
_summary_cache: dict[tuple[str, str], dict[str, Any]] = {}


def get_cached_summary(place_id: str, language: str) -> dict[str, Any] | None:
    return _summary_cache.get((place_id.lower().strip(), language.lower().strip()))


def cache_summary(place_id: str, language: str, data: dict[str, Any]) -> None:
    _summary_cache[(place_id.lower().strip(), language.lower().strip())] = data


async def _call_groq_api(
    messages: list[dict[str, str]],
    model: str | None = None,
    max_tokens: int = 600,
    temperature: float = 0.5,
) -> str:
    """Execute Groq API call using official Groq SDK with httpx fallback."""
    target_model = model or config.GROQ_MODEL
    api_key = config.GROQ_API_KEY

    # 1. Try official Groq SDK
    try:
        from groq import AsyncGroq
        import groq

        client = AsyncGroq(api_key=api_key, timeout=config.GROQ_TIMEOUT_SECONDS)
        response = await client.chat.completions.create(
            model=target_model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        if response.choices and response.choices[0].message:
            return response.choices[0].message.content or ""
        raise RuntimeError("Groq returned an empty response.")
    except ImportError:
        # Fallback to direct HTTP request using httpx if Groq SDK is not importable
        logger.info("groq package not importable; using direct httpx client")
        import httpx

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": target_model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        async with httpx.AsyncClient(timeout=config.GROQ_TIMEOUT_SECONDS) as http_client:
            resp = await http_client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                json=payload,
                headers=headers,
            )
            if resp.status_code == 401:
                raise ValueError("Invalid Groq API key configured.")
            if resp.status_code == 429:
                raise TimeoutError("Groq API rate limit exceeded.")
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"]["content"]


async def generate_chat_reply(
    message: str,
    history: list[dict[str, str]] | None = None,
    place_id: str | None = None,
    language: str | None = "auto",
) -> dict[str, Any]:
    """Generate cultural assistant answer grounded in verified Pune knowledge.

    Returns dict matching ChatResponse schema:
    {"reply": str, "sources": list[dict], "model": str, "setup_required": bool, "status": str}
    """
    # 1. Check if Groq API key is configured
    if not config.groq_configured():
        # Provide helpful setup message along with verified sources
        _, sources = knowledge.build_knowledge_context(message, place_id=place_id)
        return {
            "reply": config.GROQ_SETUP_MESSAGE,
            "sources": sources[:3],
            "model": config.GROQ_MODEL,
            "setup_required": True,
            "status": "setup_required",
        }

    # 2. Retrieve verified context & sources
    context_text, sources = knowledge.build_knowledge_context(message, place_id=place_id)

    # 3. Assemble message payload for Groq
    groq_messages: list[dict[str, str]] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "system",
            "content": (
                "VERIFIED FACTUAL CONTEXT FROM SHEHARNAAMA KNOWLEDGE BASE:\n\n"
                f"{context_text}\n\n"
                "INSTRUCTIONS FOR YOUR ANSWER:\n"
                "- Ground all factual statements in this context.\n"
                "- Respect geographic distinction: Peth places (Sadashiv, Kasba, Shukrawar, Budhwar) vs. Non-Peth Camp places (Marz-o-rin, Kayani, Garden Vada Pav).\n"
                "- Only mention places as tour stops if verified in the context as part of The Peth Stories Walk.\n"
                "- Never fabricate dates, prices, or claims not found in this context.\n"
                "- If the user asks in Hindi or Hinglish, answer in that language naturally.\n"
                "- Keep responses concise (under 180 words) and warm."
            ),
        },
    ]

    # Include recent conversation turns (up to 6)
    if history:
        for turn in history[-6:]:
            groq_messages.append({"role": turn["role"], "content": turn["content"]})

    # Add current user message
    groq_messages.append({"role": "user", "content": message})

    # 4. Invoke Groq API with robust error handling
    try:
        reply_text = await _call_groq_api(groq_messages, max_tokens=600, temperature=0.5)
        return {
            "reply": reply_text.strip(),
            "sources": sources,
            "model": config.GROQ_MODEL,
            "setup_required": False,
            "status": "ok",
        }
    except Exception as exc:
        logger.warning("Groq chat completion failure: %s", exc)
        err_str = str(exc).lower()

        if "model_not_found" in err_str or "does not exist" in err_str:
            return {
                "reply": (
                    f"The configured Groq model is currently unavailable on this account. "
                    "Please verify GROQ_MODEL in your server configuration."
                ),
                "sources": sources[:2],
                "model": config.GROQ_MODEL,
                "setup_required": True,
                "status": "error",
            }
        if (
            "auth" in err_str
            or "api_key" in err_str
            or "api key" in err_str
            or "401" in err_str
            or "invalid_api_key" in err_str
            or "invalid" in err_str
        ):
            return {
                "reply": (
                    "The Groq API key configured on this server appears to be invalid. "
                    "Please verify GROQ_API_KEY in your server configuration."
                ),
                "sources": sources[:2],
                "model": config.GROQ_MODEL,
                "setup_required": True,
                "status": "error",
            }
        if "rate" in err_str or "429" in err_str:
            return {
                "reply": (
                    "The Groq AI service is currently busy handling high traffic. "
                    "Please pause a moment and try asking again."
                ),
                "sources": sources[:2],
                "model": config.GROQ_MODEL,
                "setup_required": False,
                "status": "rate_limited",
            }
        if "timeout" in err_str or "timed out" in err_str:
            return {
                "reply": (
                    "The request to Groq AI timed out. "
                    "Please check your internet connection or try asking again."
                ),
                "sources": sources[:2],
                "model": config.GROQ_MODEL,
                "setup_required": False,
                "status": "error",
            }

        return {
            "reply": (
                "Unable to connect to the Groq AI service right now. "
                "Please verify your server network or GROQ_API_KEY configuration and try again."
            ),
            "sources": sources[:2],
            "model": config.GROQ_MODEL,
            "setup_required": False,
            "status": "error",
        }


async def generate_place_summary(
    place_id: str,
    language: str = "en",
    client_content: str | None = None,
) -> dict[str, Any]:
    """Generate concise summary for a verified place card.

    Uses in-memory cache to avoid repeated Groq calls.
    Returns dict matching SummaryResponse schema.
    """
    clean_id = place_id.strip().lower()
    clean_lang = language.strip().lower()

    # 1. Check in-memory cache
    cached = get_cached_summary(clean_id, clean_lang)
    if cached:
        return {
            "place_id": clean_id,
            "summary": cached["summary"],
            "sources": cached["sources"],
            "language": clean_lang,
            "cached": True,
            "model": cached["model"],
            "setup_required": False,
        }

    # 2. Get verified place information
    place = knowledge.get_place(clean_id)
    if not place:
        return {
            "place_id": clean_id,
            "summary": "This place reference is not found in our verified cultural knowledge base.",
            "sources": [],
            "language": clean_lang,
            "cached": False,
            "model": config.GROQ_MODEL,
            "setup_required": False,
        }

    sources = place.get("sources", [])

    # 3. Check if Groq API key is configured
    if not config.groq_configured():
        fallback_summary = place.get("summary", "")
        return {
            "place_id": clean_id,
            "summary": (
                f"{fallback_summary}\n\n"
                f"[Note: {config.GROQ_SETUP_MESSAGE}]"
            ),
            "sources": sources,
            "language": clean_lang,
            "cached": False,
            "model": config.GROQ_MODEL,
            "setup_required": True,
        }

    # 4. Build prompt for Groq
    lang_instruction = {
        "en": "Respond in English. Keep it to 2-3 concise, evocative sentences.",
        "hi": "Respond in natural Hindi (Devanagari script). Keep it to 2-3 concise, culturally respectful sentences.",
        "hinglish": "Respond in natural Hinglish (conversational Hindi in Latin/English script). Keep it to 2-3 concise, friendly sentences.",
    }.get(clean_lang, "Respond in English.")

    place_context = (
        f"Place: {place['name']} ({place['category']})\n"
        f"Neighborhood: {place['neighborhood']} (Peth core: {place['is_peth']})\n"
        f"Role: {place['walk_role']}\n"
        f"Founded: {place['founded_year']} by {place['founders']}\n"
        f"Details:\n" + "\n".join(f"- {d}" for d in place["cultural_details"])
    )
    if client_content:
        place_context += f"\nAdditional Card Context: {client_content[:500]}"

    groq_messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": (
                f"Please provide an AI Summary for this verified Pune cultural place:\n\n"
                f"{place_context}\n\n"
                f"{lang_instruction}\n"
                "Never invent facts, dates, or tour inclusions not provided in the source."
            ),
        },
    ]

    try:
        summary_text = await _call_groq_api(groq_messages, max_tokens=250, temperature=0.3)
        summary_clean = summary_text.strip()

        # Cache the result
        cache_data = {
            "summary": summary_clean,
            "sources": sources,
            "model": config.GROQ_MODEL,
        }
        cache_summary(clean_id, clean_lang, cache_data)

        return {
            "place_id": clean_id,
            "summary": summary_clean,
            "sources": sources,
            "language": clean_lang,
            "cached": False,
            "model": config.GROQ_MODEL,
            "setup_required": False,
        }
    except Exception as exc:
        logger.warning("Groq summary generation failure for %s: %s", clean_id, exc)
        # Fall back to verified base summary if Groq request fails
        fallback_summary = place.get("summary", "")
        return {
            "place_id": clean_id,
            "summary": f"{fallback_summary} (AI connection unavailable; showing verified cultural record).",
            "sources": sources,
            "language": clean_lang,
            "cached": False,
            "model": config.GROQ_MODEL,
            "setup_required": False,
        }
