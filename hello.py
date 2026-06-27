from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import os


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(__file__), **kwargs)


if __name__ == "__main__":
    port = 8000
    with ThreadingHTTPServer(("0.0.0.0", port), Handler) as httpd:
        print(f"Serving GPS check-in app at http://localhost:{port}")
        httpd.serve_forever()
