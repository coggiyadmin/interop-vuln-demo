"""IL-4 serialization boundary — Python JSON deserialize → sink (CWE-89).

Untrusted JSON crosses a module/service boundary, is deserialized, and a field is
used in a SQL sink. Tests whether taint survives the json.loads + field-access hop.
Expected today: partial → FN (deserialized-field-as-source not always modeled).
"""
import json
import sqlite3

from flask import Flask, request

app = Flask(__name__)
_conn = sqlite3.connect("app.db")


@app.route("/ingest", methods=["POST"])
def ingest():
    payload = json.loads(request.data)  # SOURCE (untrusted JSON over the boundary)
    name = payload["name"]              # tainted field survives deserialization
    # SINK (CWE-89): deserialized field concatenated into SQL.
    return str(_conn.execute("SELECT * FROM users WHERE name = '" + name + "'").fetchall())
