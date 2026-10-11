/* ==========================================================================
   SHEHARNAAMA — "Ask Pune — Read Closer" Chatbot & AI Summary Client
   Secure client-side implementation:
   - Server-proxied Groq API calls only (no client API keys)
   - HTML-sanitized output (zero XSS risk)
   - Session history preservation and new conversation reset
   - Suggested prompts, Enter-to-send, loading dots, error retry
   - Place card "Summarise with AI" with client caching & language toggle
   ========================================================================== */

(function () {
  "use strict";

  // In-memory summary cache: key -> { summary, sources, cached, language }
  var summaryCache = {};

  // Session chat history: array of { role: "user" | "assistant", content: string, sources?: [] }
  var chatHistory = [];
  var lastFailedMessage = null;

  var WELCOME_MESSAGE = {
    role: "assistant",
    content:
      "Namaskar! I am **Ask Pune — Read Closer**, your cultural companion for **SHEHARNAAMA: The City Between the Landmarks**.\n\n" +
      "Ask me about Pune's quiet neighbourhood layers: living metalcraft in Tambat Ali, 19th-century typography at Chitrashala Press, " +
      "morning market rhythms at Mahatma Phule Mandai, or heritage food traditions. You can speak in English, Hindi, or Hinglish!",
    sources: [],
  };

  /* ---------- HTML Sanitizer & Simple Safe Markdown Parser ---------- */

  function escapeHtml(text) {
    if (!text) return "";
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  function renderSafeMarkdown(markdown) {
    if (!markdown) return "";
    var safe = escapeHtml(markdown);

    // Bold: **text**
    safe = safe.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");

    // Italics: *text* or _text_
    safe = safe.replace(/\*(.*?)\*/g, "<em>$1</em>");

    // Links: [text](url) -> sanitize url strictly to https?
    safe = safe.replace(/\[([^\]]+)\]\((https?:\/\/[^\s\)]+)\)/g, function (_, label, url) {
      return '<a href="' + url + '" target="_blank" rel="noopener noreferrer" class="chat-source-link">' +
        label + ' <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6M15 3h6v6M10 14L21 3"/></svg></a>';
    });

    // Split into paragraphs / lines
    var paragraphs = safe.split(/\n\n+/);
    var htmlParts = [];

    paragraphs.forEach(function (para) {
      var lines = para.split("\n");
      var isList = lines.every(function (l) { return l.trim().startsWith("- ") || l.trim().startsWith("* "); });

      if (isList) {
        var items = lines.map(function (l) {
          return "<li>" + l.replace(/^[-*]\s+/, "") + "</li>";
        }).join("");
        htmlParts.push("<ul>" + items + "</ul>");
      } else {
        htmlParts.push("<p>" + lines.join("<br>") + "</p>");
      }
    });

    return htmlParts.join("");
  }

  /* ---------- DOM References ---------- */

  var launcherBtn = document.getElementById("chat-launcher-btn");
  var chatDrawer = document.getElementById("chat-drawer");
  var chatCloseBtn = document.getElementById("chat-close-btn");
  var chatClearBtn = document.getElementById("chat-clear-btn");
  var chatMessagesEl = document.getElementById("chat-messages");
  var chatForm = document.getElementById("chat-form");
  var chatInput = document.getElementById("chat-input");
  var chatSendBtn = document.getElementById("chat-send-btn");

  /* ---------- Drawer Toggle ---------- */

  function openChat() {
    if (!chatDrawer) return;
    chatDrawer.classList.add("is-open");
    launcherBtn && launcherBtn.setAttribute("aria-expanded", "true");
    if (chatInput) {
      setTimeout(function () { chatInput.focus(); }, 150);
    }
  }

  function closeChat() {
    if (!chatDrawer) return;
    chatDrawer.classList.remove("is-open");
    launcherBtn && launcherBtn.setAttribute("aria-expanded", "false");
    launcherBtn && launcherBtn.focus();
  }

  function toggleChat() {
    if (!chatDrawer) return;
    if (chatDrawer.classList.contains("is-open")) {
      closeChat();
    } else {
      openChat();
    }
  }

  /* ---------- Session Storage Persistence ---------- */

  function saveSessionHistory() {
    try {
      sessionStorage.setItem("sheharnaama_chat_history", JSON.stringify(chatHistory));
    } catch (_) {}
  }

  function loadSessionHistory() {
    try {
      var stored = sessionStorage.getItem("sheharnaama_chat_history");
      if (stored) {
        chatHistory = JSON.parse(stored);
      }
    } catch (_) {}
    if (!chatHistory || chatHistory.length === 0) {
      chatHistory = [WELCOME_MESSAGE];
    }
  }

  /* ---------- Render Chat Messages ---------- */

  function renderMessages() {
    if (!chatMessagesEl) return;
    chatMessagesEl.innerHTML = "";

    chatHistory.forEach(function (msg, idx) {
      var msgRow = document.createElement("div");
      msgRow.className = "chat-msg " + (msg.role === "user" ? "chat-msg-user" : "chat-msg-bot");

      var bubble = document.createElement("div");
      bubble.className = "chat-msg-bubble";
      bubble.innerHTML = renderSafeMarkdown(msg.content);

      msgRow.appendChild(bubble);

      // Render verified sources section if present
      if (msg.sources && msg.sources.length > 0) {
        var sourcesEl = document.createElement("div");
        sourcesEl.className = "chat-msg-sources";
        var label = document.createElement("span");
        label.className = "chat-sources-label";
        label.textContent = "Verified Sources:";
        sourcesEl.appendChild(label);

        msg.sources.forEach(function (src) {
          var a = document.createElement("a");
          a.className = "chat-source-link";
          a.href = src.url;
          a.target = "_blank";
          a.rel = "noopener noreferrer";
          a.textContent = src.title;
          sourcesEl.appendChild(a);
        });

        bubble.appendChild(sourcesEl);
      }

      // If welcome message, attach suggested questions chips
      if (idx === 0 && msg.role === "assistant") {
        var suggestionsEl = document.createElement("div");
        suggestionsEl.className = "chat-suggestions";
        suggestionsEl.innerHTML =
          '<p class="chat-suggestions-title">Suggested Inquiries:</p>' +
          '<button type="button" class="chat-chip" data-query="What is Tambat Ali known for?">What is Tambat Ali known for?</button>' +
          '<button type="button" class="chat-chip" data-query="Tell me about Chitrashala Press.">Tell me about Chitrashala Press.</button>' +
          '<button type="button" class="chat-chip" data-query="Summarise the cultural significance of Pune’s traditional markets.">Summarise the cultural significance of Pune’s traditional markets.</button>' +
          '<button type="button" class="chat-chip" data-query="Tell me about Pune’s everyday food culture.">Tell me about Pune’s everyday food culture.</button>' +
          '<button type="button" class="chat-chip" data-query="What does ‘The City Between the Landmarks’ mean?">What does ‘The City Between the Landmarks’ mean?</button>';

        bubble.appendChild(suggestionsEl);
      }

      chatMessagesEl.appendChild(msgRow);
    });

    scrollToBottom();
  }

  function scrollToBottom() {
    if (!chatMessagesEl) return;
    setTimeout(function () {
      chatMessagesEl.scrollTop = chatMessagesEl.scrollHeight;
    }, 40);
  }

  /* ---------- Loading and Error States ---------- */

  var loadingEl = null;

  function showLoading() {
    hideLoading();
    loadingEl = document.createElement("div");
    loadingEl.className = "chat-loading-dots";
    loadingEl.innerHTML =
      '<span class="chat-dot"></span><span class="chat-dot"></span><span class="chat-dot"></span>' +
      '<span style="margin-left:4px;">Reading Pune closer...</span>';
    chatMessagesEl.appendChild(loadingEl);
    scrollToBottom();
    if (chatSendBtn) chatSendBtn.disabled = true;
  }

  function hideLoading() {
    if (loadingEl && loadingEl.parentNode) {
      loadingEl.parentNode.removeChild(loadingEl);
    }
    loadingEl = null;
    if (chatSendBtn) chatSendBtn.disabled = false;
  }

  function showError(errorMessage, retryCallback) {
    hideLoading();
    var errRow = document.createElement("div");
    errRow.className = "chat-msg chat-msg-bot";

    var banner = document.createElement("div");
    banner.className = "chat-error-banner";

    var text = document.createElement("span");
    text.textContent = errorMessage || "Something went wrong communicating with the cultural assistant.";
    banner.appendChild(text);

    if (retryCallback) {
      var retryBtn = document.createElement("button");
      retryBtn.type = "button";
      retryBtn.className = "chat-retry-btn";
      retryBtn.textContent = "Retry";
      retryBtn.addEventListener("click", function () {
        errRow.remove();
        retryCallback();
      });
      banner.appendChild(retryBtn);
    }

    errRow.appendChild(banner);
    chatMessagesEl.appendChild(errRow);
    scrollToBottom();
  }

  /* ---------- Send Chat Message ---------- */

  async function sendMessage(text) {
    var query = (text || (chatInput ? chatInput.value : "")).trim();
    if (!query) return;

    if (chatInput) {
      chatInput.value = "";
      chatInput.style.height = "auto";
    }

    // Add user message to UI
    chatHistory.push({ role: "user", content: query });
    saveSessionHistory();
    renderMessages();
    showLoading();

    lastFailedMessage = query;

    // Filter history for API (exclude initial welcome)
    var apiHistory = chatHistory
      .slice(1, -1)
      .slice(-6)
      .map(function (m) {
        return { role: m.role, content: m.content };
      });

    try {
      var response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          message: query,
          history: apiHistory,
        }),
      });

      hideLoading();

      if (!response.ok) {
        var errJson = await response.json().catch(function () { return {}; });
        var detail = errJson.detail || "Server error occurred (" + response.status + ")";
        showError(typeof detail === "string" ? detail : "Request failed.", function () {
          sendMessage(lastFailedMessage);
        });
        return;
      }

      var data = await response.json();

      chatHistory.push({
        role: "assistant",
        content: data.reply,
        sources: data.sources || [],
      });
      saveSessionHistory();
      renderMessages();
      lastFailedMessage = null;
    } catch (err) {
      hideLoading();
      showError("Network connection error. Please check your internet connection.", function () {
        sendMessage(lastFailedMessage);
      });
    }
  }

  /* ---------- Event Listeners ---------- */

  if (launcherBtn) {
    launcherBtn.addEventListener("click", toggleChat);
  }

  if (chatCloseBtn) {
    chatCloseBtn.addEventListener("click", closeChat);
  }

  if (chatClearBtn) {
    chatClearBtn.addEventListener("click", function () {
      chatHistory = [WELCOME_MESSAGE];
      saveSessionHistory();
      renderMessages();
    });
  }

  if (chatForm) {
    chatForm.addEventListener("submit", function (e) {
      e.preventDefault();
      sendMessage();
    });
  }

  if (chatInput) {
    // Enter sends, Shift+Enter new line
    chatInput.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
      }
    });

    // Auto-grow textarea
    chatInput.addEventListener("input", function () {
      this.style.height = "auto";
      this.style.height = Math.min(this.scrollHeight, 100) + "px";
    });
  }

  // Handle suggested inquiry pill clicks (delegated)
  if (chatMessagesEl) {
    chatMessagesEl.addEventListener("click", function (e) {
      var chip = e.target.closest(".chat-chip");
      if (chip) {
        var q = chip.getAttribute("data-query");
        if (q) sendMessage(q);
      }
    });
  }

  // Close on Escape key
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && chatDrawer && chatDrawer.classList.contains("is-open")) {
      closeChat();
    }
  });

  // Global triggers: buttons with data-ask-pune
  document.addEventListener("click", function (e) {
    var trigger = e.target.closest("[data-ask-pune]");
    if (trigger) {
      e.preventDefault();
      openChat();
      var prompt = trigger.getAttribute("data-ask-pune");
      if (prompt && prompt.length > 2) {
        sendMessage(prompt);
      }
    }
  });

  /* ==========================================================================
     Place Cards "Summarise with AI" Feature
     ========================================================================== */

  async function fetchSummary(placeId, lang, containerEl) {
    var cacheKey = placeId + ":" + lang;
    var contentEl = containerEl.querySelector(".ai-summary-content");
    var sourcesEl = containerEl.querySelector(".ai-summary-sources");
    var cachedBadge = containerEl.querySelector(".ai-summary-badge-cached");

    // Check client cache first
    if (summaryCache[cacheKey]) {
      var cachedItem = summaryCache[cacheKey];
      contentEl.innerHTML = renderSafeMarkdown(cachedItem.summary);
      if (cachedBadge) cachedBadge.hidden = false;
      renderSummarySources(sourcesEl, cachedItem.sources);
      return;
    }

    if (cachedBadge) cachedBadge.hidden = true;
    contentEl.innerHTML =
      '<div class="ai-summary-loading">' +
      '<span class="chat-dot"></span><span class="chat-dot"></span>' +
      '<span>Generating cultural summary via Groq...</span>' +
      '</div>';

    try {
      var res = await fetch("/api/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          place_id: placeId,
          language: lang,
        }),
      });

      if (!res.ok) {
        var err = await res.json().catch(function () { return {}; });
        contentEl.innerHTML =
          '<p style="color:var(--error); margin:0;">Unable to generate summary: ' +
          escapeHtml(err.detail || "Server error") +
          '</p>';
        return;
      }

      var data = await res.json();
      summaryCache[cacheKey] = data;

      contentEl.innerHTML = renderSafeMarkdown(data.summary);
      if (cachedBadge) cachedBadge.hidden = !data.cached;
      renderSummarySources(sourcesEl, data.sources);
    } catch (err) {
      contentEl.innerHTML =
        '<p style="color:var(--error); margin:0;">Network error generating summary. Please try again.</p>';
    }
  }

  function renderSummarySources(sourcesEl, sources) {
    if (!sourcesEl) return;
    if (!sources || sources.length === 0) {
      sourcesEl.hidden = true;
      return;
    }
    sourcesEl.hidden = false;
    sourcesEl.innerHTML = '<span class="chat-sources-label">Sources:</span> ';
    sources.forEach(function (s) {
      var a = document.createElement("a");
      a.className = "chat-source-link";
      a.href = s.url;
      a.target = "_blank";
      a.rel = "noopener noreferrer";
      a.textContent = s.title;
      sourcesEl.appendChild(a);
    });
  }

  function initPlaceCardSummaries() {
    var summaryButtons = document.querySelectorAll(".btn-ai-summary");
    summaryButtons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var placeId = btn.getAttribute("data-place");
        var panel = document.getElementById("ai-summary-panel-" + placeId);
        if (!panel) return;

        var isHidden = panel.hidden;
        panel.hidden = !isHidden;
        btn.setAttribute("aria-expanded", String(isHidden));

        if (isHidden) {
          // Fetch summary for currently active language
          var activeLangBtn = panel.querySelector(".ai-lang-btn.is-active");
          var lang = activeLangBtn ? activeLangBtn.getAttribute("data-lang") : "en";
          fetchSummary(placeId, lang, panel);
        }
      });
    });

    // Language switchers
    var langButtons = document.querySelectorAll(".ai-lang-btn");
    langButtons.forEach(function (lBtn) {
      lBtn.addEventListener("click", function () {
        var parentPanel = lBtn.closest(".ai-summary-panel");
        if (!parentPanel) return;
        var placeId = parentPanel.getAttribute("data-place-id");
        var lang = lBtn.getAttribute("data-lang");

        parentPanel.querySelectorAll(".ai-lang-btn").forEach(function (b) {
          b.classList.toggle("is-active", b === lBtn);
        });

        fetchSummary(placeId, lang, parentPanel);
      });
    });
  }

  /* ---------- Initialize ---------- */

  document.addEventListener("DOMContentLoaded", function () {
    loadSessionHistory();
    renderMessages();
    initPlaceCardSummaries();
  });

  // Export helper for debugging or console inspection
  window.SheharnaamaChat = {
    open: openChat,
    close: closeChat,
    send: sendMessage,
  };
})();
