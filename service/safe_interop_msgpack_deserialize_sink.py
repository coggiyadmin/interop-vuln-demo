"""SAFE mirror — IL-4 msgpack: schema-validated dict before sink."""
import msgpack
from flask import Flask, request

app = Flask(__name__)
ALLOWED = {"user", "active"}


@app.route("/ingest")
def ingest():
    data = msgpack.unpackb(request.data, raw=False)
    if not isinstance(data, dict) or not set(data.keys()) <= ALLOWED:
        return "bad", 400
    user = data.get("user", "")
    _ = user
    return "ok"
