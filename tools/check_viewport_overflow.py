"""Run complete responsive overflow check and capture screenshots across all 5 breakpoints."""
import subprocess
import time
import http.server
import threading
import pathlib
import sys

PORT = 8911
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BREAKPOINTS = [360, 390, 768, 1024, 1440]

OUT_DIR = pathlib.Path("tools/screenshots")
OUT_DIR.mkdir(parents=True, exist_ok=True)

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

def run_server():
    server = http.server.HTTPServer(("127.0.0.1", PORT), QuietHandler)
    server.serve_forever()

server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()
time.sleep(1)

print(f"Server started on http://127.0.0.1:{PORT}")

# 1. Capture screenshots at all 5 breakpoints
print("Capturing screenshots at 360px, 390px, 768px, 1024px, 1440px...")
for w in BREAKPOINTS:
    shot_path = OUT_DIR / f"shot-{w}px.png"
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        f"--window-size={w},1200",
        f"--screenshot={shot_path.resolve()}",
        f"http://127.0.0.1:{PORT}/index.html"
    ]
    subprocess.run(cmd, capture_output=True, timeout=15)
    if shot_path.exists():
        print(f"  [OK] {w}px screenshot saved ({shot_path.stat().st_size} bytes)")
    else:
        print(f"  [FAIL] {w}px screenshot failed")

# 2. Check overflow via Chrome dump-dom with a wait
print("\nChecking horizontal overflow at each breakpoint...")
# Wait sufficient time for iframe runner to execute all 5 widths
runner_cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--virtual-time-budget=6000",
    "--dump-dom",
    f"http://127.0.0.1:{PORT}/tools/test_overflow_runner.html"
]
proc = subprocess.run(runner_cmd, capture_output=True, text=True, timeout=20)
dom = proc.stdout

if "COMPLETED:" in dom:
    results_part = dom.split("COMPLETED:")[1].split("</pre>")[0]
    print(results_part.strip())
else:
    print("Runner output:")
    if "<pre id=\"results\">" in dom:
        print(dom.split("<pre id=\"results\">")[1].split("</pre>")[0])
    else:
        print(dom[:500])
