from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import os

app = Flask(__name__)
hits = Counter("app_hits_total", "Total hits")

@app.get("/")
def index():
    hits.inc()
    return jsonify(ok=True, env=os.getenv("ENV","dev"))

@app.get("/healthz")
def health():
    return "ok", 200

@app.get("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

