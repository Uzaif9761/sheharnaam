"""Tests verifying frontend DOM integration of Ask Pune Chatbot and AI Summary feature."""

import pytest
from fastapi.testclient import TestClient

from backend.app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_landing_page_includes_chat_assets(client):
    res = client.get("/")
    assert res.status_code == 200
    html = res.text

    # Check CSS and JS
    assert 'href="assets/css/chat.css"' in html
    assert 'src="assets/js/chat.js"' in html

    # Check launcher button and drawer
    assert 'id="chat-launcher-btn"' in html
    assert 'id="chat-drawer"' in html
    assert 'id="chat-input"' in html
    assert 'id="chat-send-btn"' in html
    assert 'id="chat-clear-btn"' in html
    assert 'id="chat-close-btn"' in html
    assert 'Ask Pune &mdash; Read Closer' in html

    # Check hero entry point
    assert 'data-ask-pune=""' in html


def test_landing_page_includes_all_seven_ai_summaries(client):
    res = client.get("/")
    assert res.status_code == 200
    html = res.text

    expected_places = [
        "chitrashala-press",
        "tambat-ali",
        "mahatma-phule-mandai",
        "vaidya-upahar-gruha",
        "marz-o-rin",
        "kayani-bakery",
        "garden-vada-pav",
    ]

    for place_id in expected_places:
        assert f'data-place="{place_id}"' in html, f"Missing AI summary button for {place_id}"
        assert f'id="ai-summary-panel-{place_id}"' in html, f"Missing AI summary panel for {place_id}"

    # Verify multilingual controls in panels
    assert 'data-lang="en"' in html
    assert 'data-lang="hi"' in html
    assert 'data-lang="hinglish"' in html
