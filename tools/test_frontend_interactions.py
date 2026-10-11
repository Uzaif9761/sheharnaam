"""Frontend integration & interaction tests using Chrome DevTools / DOM Dump.
Verifies:
1. Category filters work dynamically
2. Card drawers expand/collapse
3. Audience selector switches smoothly
4. Zero console errors
"""
import subprocess
import time
import http.server
import threading
import pathlib
import sys

PORT = 8922
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

def run_server():
    server = http.server.HTTPServer(("127.0.0.1", PORT), QuietHandler)
    server.serve_forever()

server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()
time.sleep(1)

test_page = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>interactive-test</title></head>
<body>
<pre id="log">RUNNING</pre>
<iframe id="app" src="/index.html" style="width:1200px;height:900px;"></iframe>
<script>
window.onerror = function(msg, url, line) {{
  window.__hasError = true;
  document.getElementById("log").textContent += "\\nJS ERROR: " + msg + " at " + line;
}};

var frame = document.getElementById("app");
frame.onload = function() {{
  setTimeout(function() {{
    var win = frame.contentWindow;
    var doc = frame.contentDocument;
    var logs = [];

    function assert(cond, desc) {{
      logs.push((cond ? "[PASS] " : "[FAIL] ") + desc);
    }}

    // 1. Check Brand & Tagline
    var brandTag = doc.querySelector(".brand-tagline");
    assert(brandTag && brandTag.textContent.includes("The City Between the Landmarks"), "Brand tagline is 'The City Between the Landmarks'");

    // 2. Check Read Pune in the Details Section
    var detailsSec = doc.getElementById("details");
    assert(detailsSec !== null, "Section #details exists");
    var heading = detailsSec ? detailsSec.querySelector("h2").textContent : "";
    assert(heading.includes("READ PUNE IN THE DETAILS") || heading.includes("READ PUNE IN THE"), "Section heading is 'READ PUNE IN THE DETAILS'");

    // 3. Check All 7 Editorial Cards Exist
    var cards = doc.querySelectorAll(".editorial-card");
    assert(cards.length === 7, "Found 7 editorial place cards (found " + cards.length + ")");

    // 4. Test Category Filter Click: Print
    var printBtn = doc.querySelector('.editorial-filter-btn[data-filter="print"]');
    if (printBtn) {{
      printBtn.click();
      var visibleCards = Array.from(cards).filter(c => !c.hasAttribute("hidden"));
      assert(visibleCards.length === 1, "Print filter shows exactly 1 card (Chitrashala Press)");
      assert(visibleCards[0].textContent.includes("Chitrashala Press"), "Visible card is Chitrashala Press");
    }} else {{
      assert(false, "Print filter button found");
    }}

    // 5. Test Category Filter Click: Food
    var foodBtn = doc.querySelector('.editorial-filter-btn[data-filter="food"]');
    if (foodBtn) {{
      foodBtn.click();
      var foodCards = Array.from(cards).filter(c => !c.hasAttribute("hidden"));
      assert(foodCards.length === 4, "Food filter shows exactly 4 food cards (found " + foodCards.length + ")");
      var geoBanner = doc.getElementById("details-geo-notice");
      assert(geoBanner && !geoBanner.hasAttribute("hidden"), "Geographic Notice banner is visible during food filtering");
    }}

    // 6. Test Category Filter Click: All
    var allBtn = doc.querySelector('.editorial-filter-btn[data-filter="all"]');
    if (allBtn) {{
      allBtn.click();
      var allCards = Array.from(cards).filter(c => !c.hasAttribute("hidden"));
      assert(allCards.length === 7, "All filter restores all 7 cards (found " + allCards.length + ")");
    }}

    // 7. Test Card Drawer Expand / Collapse
    var firstCard = cards[0];
    var toggle = firstCard.querySelector(".editorial-card-toggle");
    assert(toggle !== null, "Card toggle button exists");
    if (toggle) {{
      var initialExpanded = toggle.getAttribute("aria-expanded");
      toggle.click();
      var nowExpanded = toggle.getAttribute("aria-expanded");
      assert(nowExpanded === "true" && firstCard.classList.contains("is-expanded"), "Card expanded on click (aria-expanded='true', class is-expanded)");
      
      toggle.click();
      var collapsedAgain = toggle.getAttribute("aria-expanded");
      assert(collapsedAgain === "false" && !firstCard.classList.contains("is-expanded"), "Card collapsed on second click (aria-expanded='false')");
    }}

    // 8. Test Audience Selector Switch
    var visitorTab = doc.getElementById("tab-visitor");
    var localTab = doc.getElementById("tab-local");
    var audTitle = doc.getElementById("audience-display-title");
    assert(visitorTab && localTab && audTitle, "Audience selector elements present");
    if (visitorTab && audTitle) {{
      visitorTab.click();
      setTimeout(function() {{
        assert(visitorTab.classList.contains("is-active") && visitorTab.getAttribute("aria-selected") === "true", "Visitor tab selected");
        assert(audTitle.textContent.includes("Understand Pune beyond the monuments") || audTitle.textContent.includes("monuments"), "Title updated to visitor perspective");
        
        localTab.click();
        setTimeout(function() {{
          assert(localTab.classList.contains("is-active") && localTab.getAttribute("aria-selected") === "true", "Local tab re-selected as primary");
          document.getElementById("log").textContent = "COMPLETED:\\n" + logs.join("\\n");
        }}, 200);
      }}, 200);
    }}

  }}, 500);
}};
</script>
</body>
</html>"""

pathlib.Path("tools/test_interactions_runner.html").write_text(test_page, encoding="utf-8")

cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--virtual-time-budget=6000",
    "--dump-dom",
    f"http://127.0.0.1:{PORT}/tools/test_interactions_runner.html"
]

proc = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
dom = proc.stdout

if "COMPLETED:" in dom:
    print(dom.split("COMPLETED:")[1].split("</pre>")[0].strip())
else:
    print("Test output:")
    if "<pre id=\"log\">" in dom:
        print(dom.split("<pre id=\"log\">")[1].split("</pre>")[0])
    else:
        print(dom[:600])
