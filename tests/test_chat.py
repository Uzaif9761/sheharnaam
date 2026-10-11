"""Tests for Groq AI chat and summary endpoints.

Tests:
- /api/chat/status
- /api/chat (missing key setup message, validation, mocked successful Groq response, error handling)
- /api/summarize (summaries, language variations, caching)
- Knowledge base grounding and geographic accuracy
- Chat rate limiting
"""

from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from backend.app import config, groq_service, knowledge
from backend.app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_chat_status_endpoint(client):
    res = client.get("/api/chat/status")
    assert res.status_code == 200
    data = res.json()
    assert "configured" in data
    assert "model" in data
    assert "suggested_questions" in data
    assert len(data["suggested_questions"]) >= 5


def test_chat_endpoint_validation_empty_message(client):
    res = client.post("/api/chat", json={"message": "   "})
    assert res.status_code == 422


def test_chat_endpoint_validation_long_message(client):
    res = client.post("/api/chat", json={"message": "a" * 1005})
    assert res.status_code == 422


def test_chat_endpoint_missing_api_key_returns_setup_message(client, monkeypatch):
    monkeypatch.setattr(config, "GROQ_API_KEY", "")
    res = client.post("/api/chat", json={"message": "What is Tambat Ali known for?"})
    assert res.status_code == 200
    data = res.json()
    assert data["setup_required"] is True
    assert data["status"] == "setup_required"
    assert "Ask Pune is currently resting" in data["reply"]
    assert len(data["sources"]) > 0


def test_chat_endpoint_with_mocked_groq_success(client, monkeypatch):
    monkeypatch.setattr(config, "GROQ_API_KEY", "gsk_test_mock_key_valid_123456789")

    mock_reply = "Tambat Ali is Kasba Peth's historic coppersmith lane known for Mathar Kaam."

    with patch("backend.app.groq_service._call_groq_api", new_callable=AsyncMock) as mock_api:
        mock_api.return_value = mock_reply

        res = client.post(
            "/api/chat",
            json={
                "message": "What is Tambat Ali known for?",
                "history": [],
            },
        )
        assert res.status_code == 200
        data = res.json()
        assert data["reply"] == mock_reply
        assert data["setup_required"] is False
        assert data["status"] == "ok"
        assert any("INTACH Pune" in s["title"] for s in data["sources"])


def test_chat_endpoint_with_mocked_auth_error(client, monkeypatch):
    monkeypatch.setattr(config, "GROQ_API_KEY", "gsk_invalid_test_key_123456789")

    with patch("backend.app.groq_service._call_groq_api", new_callable=AsyncMock) as mock_api:
        mock_api.side_effect = ValueError("Invalid Groq API key configured.")

        res = client.post("/api/chat", json={"message": "Tell me about Chitrashala Press."})
        assert res.status_code == 200
        data = res.json()
        assert "invalid" in data["reply"].lower()
        assert data["setup_required"] is True
        assert data["status"] == "error"


def test_chat_endpoint_with_mocked_timeout_error(client, monkeypatch):
    monkeypatch.setattr(config, "GROQ_API_KEY", "gsk_valid_key_123456789")

    with patch("backend.app.groq_service._call_groq_api", new_callable=AsyncMock) as mock_api:
        mock_api.side_effect = TimeoutError("Request timed out")

        res = client.post("/api/chat", json={"message": "Tell me about Mandai."})
        assert res.status_code == 200
        data = res.json()
        assert "timed out" in data["reply"].lower()
        assert data["status"] == "error"


def test_summarize_missing_key_fallback(client, monkeypatch):
    monkeypatch.setattr(config, "GROQ_API_KEY", "")
    res = client.post(
        "/api/summarize",
        json={"place_id": "tambat-ali", "language": "en"},
    )
    assert res.status_code == 200
    data = res.json()
    assert data["place_id"] == "tambat-ali"
    assert data["setup_required"] is True
    assert "Tambat Ali" in data["summary"]
    assert len(data["sources"]) > 0


def test_summarize_with_mocked_groq_and_cache(client, monkeypatch):
    monkeypatch.setattr(config, "GROQ_API_KEY", "gsk_valid_key_123456789")

    # Clear cache for isolated test
    groq_service._summary_cache.clear()

    mock_summary = "Chitrashala Press in Sadashiv Peth democratised vernacular print culture in western India."

    with patch("backend.app.groq_service._call_groq_api", new_callable=AsyncMock) as mock_api:
        mock_api.return_value = mock_summary

        # 1. First call -> should invoke Groq API
        res1 = client.post(
            "/api/summarize",
            json={"place_id": "chitrashala-press", "language": "en"},
        )
        assert res1.status_code == 200
        data1 = res1.json()
        assert data1["summary"] == mock_summary
        assert data1["cached"] is False
        assert mock_api.call_count == 1

        # 2. Second call -> should hit cache without calling Groq API again
        res2 = client.post(
            "/api/summarize",
            json={"place_id": "chitrashala-press", "language": "en"},
        )
        assert res2.status_code == 200
        data2 = res2.json()
        assert data2["summary"] == mock_summary
        assert data2["cached"] is True
        assert mock_api.call_count == 1  # No additional call!



def test_knowledge_base_geographic_accuracy():
    """Verify that knowledge base enforces strict geographic and tour package truth."""
    # Peth places
    assert knowledge.VERIFIED_PLACES["chitrashala-press"]["is_peth"] is True
    assert knowledge.VERIFIED_PLACES["tambat-ali"]["is_peth"] is True
    assert knowledge.VERIFIED_PLACES["mahatma-phule-mandai"]["is_peth"] is True
    assert knowledge.VERIFIED_PLACES["vaidya-upahar-gruha"]["is_peth"] is True

    # Official walk stops
    assert knowledge.VERIFIED_PLACES["chitrashala-press"]["is_official_walk_stop"] is True
    assert knowledge.VERIFIED_PLACES["tambat-ali"]["is_official_walk_stop"] is True

    # Camp places (MUST NOT be marked as Peth or official stops)
    assert knowledge.VERIFIED_PLACES["marz-o-rin"]["is_peth"] is False
    assert knowledge.VERIFIED_PLACES["marz-o-rin"]["is_official_walk_stop"] is False
    assert "Camp" in knowledge.VERIFIED_PLACES["marz-o-rin"]["neighborhood"]

    assert knowledge.VERIFIED_PLACES["kayani-bakery"]["is_peth"] is False
    assert knowledge.VERIFIED_PLACES["kayani-bakery"]["is_official_walk_stop"] is False

    assert knowledge.VERIFIED_PLACES["garden-vada-pav"]["is_peth"] is False
    assert knowledge.VERIFIED_PLACES["garden-vada-pav"]["is_official_walk_stop"] is False


def test_chat_rate_limiting(client, monkeypatch):
    """Verify client IP rate limit on AI endpoints."""
    monkeypatch.setattr(config, "CHAT_RATE_LIMIT_PER_MINUTE", 3)
    from backend.app.routes import chat as chat_routes

    chat_routes._chat_request_times.clear()

    # 3 calls should succeed
    for _ in range(3):
        res = client.post("/api/chat", json={"message": "Namaste"})
        assert res.status_code == 200

    # 4th call must be blocked with 429
    res = client.post("/api/chat", json={"message": "Namaste"})
    assert res.status_code == 429
    assert "Too many AI requests" in res.json()["detail"]
