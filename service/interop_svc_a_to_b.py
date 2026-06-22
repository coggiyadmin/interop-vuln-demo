"""IL-4 service-to-service boundary — svc-A → svc-B (CWE-918/89).

Service A receives an untrusted field and forwards it to service B, where it
reaches a sink. Cross-service taint: the source (svc-A request) and sink (svc-B
handler) live in different logical services. Expected today: FN.
"""
import sqlite3

import requests
from flask import Flask, request

app = Flask(__name__)
_conn = sqlite3.connect("app.db")


# --- Service A: edge that receives and forwards untrusted input ---
@app.route("/a/forward", methods=["POST"])
def svc_a_forward():
    user = request.form.get("user", "")  # SOURCE (external request to svc-A)
    # Forward verbatim to svc-B's internal endpoint.
    requests.post("http://svc-b.internal/handle", json={"user": user})
    return "forwarded"


# --- Service B: internal handler that trusts the forwarded value ---
@app.route("/b/handle", methods=["POST"])
def svc_b_handle():
    user = request.json["user"]  # taint arrives from svc-A across the service hop
    # SINK (CWE-89): forwarded value concatenated into SQL in the downstream service.
    return str(_conn.execute("SELECT * FROM accounts WHERE user = '" + user + "'").fetchall())
