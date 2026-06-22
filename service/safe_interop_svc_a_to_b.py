"""IL-4 — SAFE mirror of interop_svc_a_to_b.py.
The forwarded value reaches svc-B's sink as a bound query parameter, never
concatenated into SQL. ZERO security findings expected.
"""
import sqlite3

import requests
from flask import Flask, request

app = Flask(__name__)
_conn = sqlite3.connect("app.db")


@app.route("/a/forward", methods=["POST"])
def svc_a_forward():
    user = request.form.get("user", "")  # SOURCE
    requests.post("http://svc-b.internal/handle", json={"user": user})
    return "forwarded"


@app.route("/b/handle", methods=["POST"])
def svc_b_handle():
    user = request.json["user"]
    # Safe: parameterized query in the downstream service.
    return str(_conn.execute("SELECT * FROM accounts WHERE user = ?", (user,)).fetchall())
