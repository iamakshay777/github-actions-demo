# app.py
# ---------------------------------------------------------------
# Tiny HTTP server we ship end-to-end with our CI/CD pipeline.
#
# Flow:
#   1. You push this file to GitHub.
#   2. GitHub Actions builds it into a Docker image.
#   3. The image is copied to an EC2 server and started as a
#      container, with port 8080 exposed to the world.
#   4. Anyone visiting  http://<EC2-public-ip>:8080  sees the
#      message below — proof the deploy worked.
#
# We use Python's built-in `http.server` so there are no extra
# dependencies for students to install. In a real app you'd
# typically use Flask, FastAPI, Django, etc.
# ---------------------------------------------------------------

from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080
MESSAGE = "Hello from CI/CD! This container was built and deployed by GitHub Actions."


class Handler(BaseHTTPRequestHandler):
    # `do_GET` runs on every HTTP GET request (i.e. every browser visit).
    def do_GET(self):
        self.send_response(200)                                  # 200 = OK
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(MESSAGE.encode("utf-8"))                # body of the response


if __name__ == "__main__":
    # Bind to 0.0.0.0 (not 127.0.0.1) so the server is reachable
    # from outside the container, not just from inside it.
    print(f"Serving on http://0.0.0.0:{PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
