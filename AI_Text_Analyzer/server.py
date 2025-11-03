# server.py
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from textblob import TextBlob
from collections import Counter
import re

PORT = 8000

def analyze_text(text):
    blob = TextBlob(text)
    # words: only alphabetic tokens, lowercased
    words = [w.lower() for w in re.findall(r"\b[a-zA-Z]+\b", text)]
    word_count = len(words)
    char_count = len(text)
    polarity = round(blob.sentiment.polarity, 3)  # -1..1
    subjectivity = round(blob.sentiment.subjectivity, 3)  # 0..1
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    top_words = Counter(words).most_common(8)

    return {
        "word_count": word_count,
        "char_count": char_count,
        "polarity": polarity,
        "subjectivity": subjectivity,
        "sentiment": sentiment,
        "top_words": top_words
    }

class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path == "/analyze":
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            # body is raw text from client
            result = analyze_text(body)
            response = json.dumps(result).encode('utf-8')

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(response)))
            # allow same-origin requests (not needed if served from same origin)
            self.send_header("Access-Control-Allow-Origin", "null")
            self.end_headers()
            self.wfile.write(response)
        else:
            # fallback to normal static file handling
            super().do_GET()

    # Allow browser preflight if needed (not necessary in same-origin, but safe)
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

if __name__ == "__main__":
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, Handler)
    print(f"Serving on http://127.0.0.1:{PORT}  (Press Ctrl+C to stop)")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        httpd.server_close()
