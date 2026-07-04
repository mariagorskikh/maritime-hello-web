import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

# Maritime injects PORT at runtime; default to 8080 for local runs.
PORT = int(os.environ.get("PORT", "8080"))


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps(
            {
                "app": "hello-web",
                "message": "Hello from a custom agent on Maritime",
                "listening_on": PORT,
                "path": self.path,
            },
            indent=2,
        ).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):  # noqa: A002 — stdlib signature
        pass


HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
