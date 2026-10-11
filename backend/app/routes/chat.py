"""Chat and AI cultural summary routes.

POST /api/chat       — conversational answers via Groq AI ("Ask Pune — Read Closer")
POST /api/summarize  — concise verified place summaries via Groq AI
GET  /api/chat/status — client-safe configuration status and suggested questions
"""

import time
from collections import defaultdict, deque
from typing import Any

from fastapi import APIRouter, HTTPException, Request

from .. import config, groq_service, knowledge
from ..schemas import ChatRequest, ChatResponse, SummaryRequest, SummaryResponse

router = APIRouter(prefix="/api", tags=["chat"])

_chat_request_times: dict[str, deque] = defaultdict(lambda: deque(maxlen=60))


def _check_chat_rate(ip: str) -> None:
    """Enforce per-IP rate limiting on AI requests."""
    window = 60.0
    now = time.time()
    stamps = _chat_request_times[ip]
    while stamps and now - stamps[0] > window:
        stamps.popleft()
    if len(stamps) >= config.CHAT_RATE_LIMIT_PER_MINUTE:
        raise HTTPException(
            status_code=429,
            detail="Too many AI requests from this connection. Please wait a minute and try again.",
        )
    stamps.append(now)


def _client_ip(request: Request) -> str:
    return request.client.host if request.client else "unknown"


@router.get("/chat/status")
def chat_status() -> dict[str, Any]:
    """Safe status endpoint returning configuration state without leaking secrets."""
    return {
        "configured": config.groq_configured(),
        "model": config.GROQ_MODEL,
        "suggested_questions": knowledge.SUGGESTED_QUESTIONS,
    }


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(payload: ChatRequest, request: Request) -> ChatResponse:
    """Conversational cultural assistant endpoint powered by Groq.

    Grounded in verified Pune knowledge base with citations.
    """
    _check_chat_rate(_client_ip(request))

    history_dicts = [msg.model_dump() for msg in payload.history] if payload.history else []

    result = await groq_service.generate_chat_reply(
        message=payload.message,
        history=history_dicts,
        place_id=payload.place_id,
        language=payload.language,
    )

    return ChatResponse(**result)


@router.post("/summarize", response_model=SummaryResponse)
async def summarize_endpoint(payload: SummaryRequest, request: Request) -> SummaryResponse:
    """Summarise verified place information card using Groq AI.

    Caches responses to avoid redundant API requests.
    """
    _check_chat_rate(_client_ip(request))

    result = await groq_service.generate_place_summary(
        place_id=payload.place_id,
        language=payload.language,
        client_content=payload.content,
    )

    return SummaryResponse(**result)
