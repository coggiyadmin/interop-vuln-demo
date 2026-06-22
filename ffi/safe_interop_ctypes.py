"""IL-3 FFI boundary — SAFE mirror of interop_ctypes.py.
The user input only selects among constant, vetted commands; the value handed to
the native call is a literal, never the tainted string. ZERO findings expected.
"""
import ctypes

from flask import Flask, request

app = Flask(__name__)
_lib = ctypes.CDLL("./native.so")

_ALLOWED = {"status": b"systemctl status app", "uptime": b"uptime"}


@app.route("/run")
def run():
    action = request.args.get("action", "")  # SOURCE
    cmd = _ALLOWED.get(action)                # allowlist → constant literal
    if cmd is None:
        return "unknown action", 400
    _lib.run_cmd(cmd)                         # only a constant reaches the FFI call
    return "ok"
