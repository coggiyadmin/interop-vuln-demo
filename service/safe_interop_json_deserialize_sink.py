"""IL-4 — SAFE mirror of interop_json_deserialize_sink.py.
The deserialized field is bound as a query parameter, never concatenated into the
SQL. ZERO security findings expected.
"""
import json
import sqlite3

from flask import Flask, request

app = Flask(__name__)
_conn = sqlite3.connect("app.db")


@app.route("/ingest", methods=["POST"])
def ingest():
    payload = json.loads(request.data)  # SOURCE
    name = payload["name"]
    # Safe: parameterized query — deserialized field bound, not interpolated.
    return str(_conn.execute("SELECT * FROM users WHERE name = ?", (name,)).fetchall())
