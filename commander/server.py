"""Commander dashboard: tiny local web app for composing agent instructions.

Serves one page on http://127.0.0.1:8765 with three palettes
(Folders / Actions / Files), a name field and a judgement-sentence box.
Create with no judgement text executes immediately; everything else
composes one coherent message for an agent.
"""
from __future__ import annotations

import json
import secrets
import subprocess
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import core

PORT = 8765
LOG_DIR = Path(__file__).resolve().parent / "logs"
MAX_BODY = 64 * 1024
_ALLOWED_HOSTS = {f"127.0.0.1:{PORT}", f"localhost:{PORT}"}

# Per-start random token: the page gets it from GET / and echoes it on POST.
# Kills cross-site request forgery (cross-origin pages cannot read it) on top
# of the Host check, which kills DNS-rebinding.
TOKEN = secrets.token_urlsafe(16)

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Commander</title>
<style>
  :root { --bg:#14161a; --card:#1e2127; --fg:#e6e6e6; --dim:#8a8f98; --acc:#5b9dd9; --ok:#7bc47f; }
  * { box-sizing:border-box; }
  body { background:var(--bg); color:var(--fg); font:15px/1.5 "Segoe UI",system-ui,sans-serif;
         max-width:760px; margin:24px auto; padding:0 16px; }
  h1 { font-size:20px; margin:0 0 4px; }
  .sub { color:var(--dim); font-size:13px; margin-bottom:20px; }
  .group { background:var(--card); border-radius:10px; padding:14px 16px; margin-bottom:12px; }
  .label { font-size:12px; text-transform:uppercase; letter-spacing:.08em; color:var(--dim); margin-bottom:8px; }
  .chips { display:flex; flex-wrap:wrap; gap:8px; }
  .chip { border:1px solid #3a3f47; background:#262a31; color:var(--fg); border-radius:8px;
          padding:6px 12px; cursor:pointer; font-size:14px; }
  .chip small { color:var(--dim); margin-left:6px; }
  .chip.sel { border-color:var(--acc); background:#2c3b4d; }
  .chip:hover { border-color:var(--acc); }
  input[type=text], textarea { width:100%; background:#262a31; border:1px solid #3a3f47;
          border-radius:8px; color:var(--fg); padding:9px 12px; font:inherit; }
  textarea { min-height:70px; resize:vertical; }
  .row { display:flex; gap:10px; margin-top:12px; }
  button { background:var(--acc); color:#fff; border:0; border-radius:8px; padding:10px 22px;
           font:inherit; font-weight:600; cursor:pointer; }
  button.ghost { background:#262a31; border:1px solid #3a3f47; font-weight:400; }
  button:disabled { opacity:.5; cursor:default; }
  #out { margin-top:16px; }
  .msg { background:#262a31; border:1px solid #3a3f47; border-left:4px solid var(--acc);
         border-radius:8px; padding:12px 14px; white-space:pre-wrap; word-break:break-all; }
  .ok { border-left-color:var(--ok); }
  .log { margin-top:16px; color:var(--dim); font-size:13px; }
  .log div { padding:2px 0; border-bottom:1px dashed #2a2e34; word-break:break-all; }
</style>
</head>
<body>
<h1>Commander</h1>
<div class="sub">click &rarr; type (only if needed) &rarr; one coherent message</div>

<div class="group"><div class="label">Folders</div><div class="chips" id="g-place"></div></div>
<div class="group"><div class="label">Actions</div><div class="chips" id="g-action"></div></div>
<div class="group"><div class="label">Files</div><div class="chips" id="g-kind"></div></div>

<div class="group">
  <div class="label">File name (optional)</div>
  <input type="text" id="name" placeholder="e.g. NewDatabase, draft, analysis">
  <div class="label" style="margin-top:12px">Instruction — your judgement sentence (optional)</div>
  <textarea id="instr" placeholder='e.g. "focus on the tone in paragraph 3, I want a strong hook"'></textarea>
  <div class="row">
    <button id="run">Run</button>
    <button id="goose" class="ghost" style="display:none">Send to goose</button>
  </div>
</div>

<div id="out"></div>
<div class="log" id="log"></div>

<script>
const TOKEN = "__TOKEN__";
const state = { place:null, action:"create", kind:"md", lastMessage:null };
const $ = id => document.getElementById(id);

async function api(path, body) {
  const opts = {headers: {"X-Commander-Token": TOKEN}};
  if (body) { opts.method = "POST"; opts.headers["Content-Type"] = "application/json"; opts.body = JSON.stringify(body); }
  const r = await fetch(path, opts);
  if (r.status === 403) { location.reload(); throw new Error("stale token"); }
  return r.json();
}

function chips(el, items, key) {
  el.innerHTML = "";
  for (const it of items) {
    const b = document.createElement("button");
    b.className = "chip" + (state[key] === it.v ? " sel" : "");
    b.innerHTML = it.label;
    b.onclick = () => { state[key] = state[key] === it.v && key !== "action" ? null : it.v; render(); };
    el.appendChild(b);
  }
}

function render() {
  chips($("g-place"), PLACES, "place");
  chips($("g-action"), ACTIONS, "action");
  chips($("g-kind"), KINDS, "kind");
}

function log(line) {
  const d = document.createElement("div");
  d.textContent = new Date().toLocaleTimeString() + "  " + line;
  $("log").prepend(d);
}

$("run").onclick = async () => {
  if (!state.place) return show("Pick a folder first.", false);
  const body = { action:state.action, place:state.place,
                 kind: state.kind, name: $("name").value.trim(),
                 instruction: $("instr").value };
  const res = await api("/api/run", body);
  if (res.error) return show("Error: " + res.error, false);
  if (res.mode === "executed") {
    $("goose").style.display = "none"; state.lastMessage = null;
    show("Created  " + res.path, true); log("created " + res.path);
  } else {
    state.lastMessage = res.message;
    show(res.message + "\\n\\n(copied to clipboard)", true);
    navigator.clipboard.writeText(res.message).catch(()=>{});
    log("composed " + res.message.split("\\n")[0].slice(0, 80) + "...");
    $("goose").style.display = "";
  }
};

$("goose").onclick = async () => {
  if (!state.lastMessage) return;
  $("goose").disabled = true;
  const res = await api("/api/goose", {message: state.lastMessage});
  $("goose").disabled = false;
  show(res.error ? "Error: " + res.error
       : "goose launched headless — output goes to " + res.log, res.error ? false : true);
  log("sent to goose");
};

function show(text, ok) {
  $("out").innerHTML = '<div class="msg' + (ok ? ' ok' : '') + '">' + text + "</div>";
}

let PLACES = [], ACTIONS = [], KINDS = [];
api("/api/places").then(v => {
  PLACES = v.places.map(p => ({v:p.code, label:p.code + "<small>" + p.desc + "</small>"}));
  ACTIONS = v.actions.map(a => ({v:a, label:a[0].toUpperCase()+a.slice(1)}));
  KINDS = v.kinds.map(k => ({v:k, label:k}));
  render();
});
</script>
</body>
</html>"""


class Handler(BaseHTTPRequestHandler):
    def _guard(self, post: bool = False) -> bool:
        """Return True (and answer) when the request must be rejected."""
        if self.headers.get("Host", "") not in _ALLOWED_HOSTS:
            self._send({"error": "forbidden host"}, 403)
            return True
        if post:
            if self.headers.get("Content-Type", "").split(";")[0].strip() != "application/json":
                self._send({"error": "content-type must be application/json"}, 415)
                return True
            if self.headers.get("X-Commander-Token") != TOKEN:
                self._send({"error": "bad or missing token - reload the page"}, 403)
                return True
        return False

    def _send(self, payload: dict, status: int = 200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self._guard():
            return
        if self.path == "/":
            html = PAGE.replace("__TOKEN__", TOKEN).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(html)))
            self.end_headers()
            self.wfile.write(html)
        elif self.path == "/api/places":
            vocab = core.load_vocab()
            self._send({
                "places": [{"code": c, "desc": e["desc"]} for c, e in vocab["places"].items()],
                "actions": list(core.ACTIONS),
                "kinds": list(vocab["kinds"]),
            })
        else:
            self._send({"error": "not found"}, 404)

    def do_POST(self):
        if self._guard(post=True):
            return
        length = int(self.headers.get("Content-Length", 0))
        if length > MAX_BODY:
            return self._send({"error": "body too large"}, 413)
        try:
            data = json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            return self._send({"error": "bad JSON"}, 400)
        try:
            if self.path == "/api/run":
                result = self._run(data)
                self._send(result, 400 if "error" in result else 200)
            elif self.path == "/api/goose":
                result = self._goose(data)
                self._send(result, 400 if "error" in result else 200)
            else:
                self._send({"error": "not found"}, 404)
        except Exception as exc:  # surface any failure to the page, never a stack trace
            self._send({"error": str(exc)}, 400)

    @staticmethod
    def _run(data: dict) -> dict:
        action = data.get("action", "create")
        place = data.get("place") or ""
        kind = (data.get("kind") or "").strip()
        name = (data.get("name") or "").strip()
        instruction = (data.get("instruction") or "").strip()
        if not place:
            return {"error": "no folder selected"}
        if action == "create" and not instruction:
            path = core.create(place, kind, name or None)
            return {"mode": "executed", "path": str(path)}
        message = core.compose(action, place, kind or None, name or None, instruction)
        return {"mode": "message", "message": message}

    @staticmethod
    def _goose(data: dict) -> dict:
        message = (data.get("message") or "").strip()
        if not message:
            return {"error": "empty message"}
        LOG_DIR.mkdir(exist_ok=True)
        log_path = LOG_DIR / f"goose-{time.strftime('%Y%m%d-%H%M%S')}.log"
        with open(log_path, "w", encoding="utf-8") as log_file:
            subprocess.Popen(
                ["goose", "run", "-t", message],
                stdout=log_file, stderr=subprocess.STDOUT,
                cwd=str(core.PROJECT_ROOT),
                creationflags=subprocess.CREATE_NO_WINDOW,
            )
        return {"mode": "goose", "log": str(log_path)}

    def do_OPTIONS(self):
        self._send({"error": "forbidden"}, 403)

    def log_message(self, *args):  # keep the console quiet
        pass


def main():
    url = f"http://127.0.0.1:{PORT}"
    try:
        server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    except OSError:
        print(f"Port {PORT} is busy - the dashboard is probably already running. Opening {url}")
        webbrowser.open(url)
        return
    print(f"Commander dashboard on {url} (Ctrl+C to stop)")
    threading.Timer(0.5, webbrowser.open, args=(url,)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
