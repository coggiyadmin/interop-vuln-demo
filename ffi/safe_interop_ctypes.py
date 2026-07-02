"""IL-3 FFI boundary — SAFE mirror of interop_ctypes.py.

Strict allowlist before handing data to native code; scanner MUST stay clean.
"""
import ctypes
import re

from flask import Flask, request

app = Flask(__name__)
_lib = ctypes.CDLL("./native.so")
_CMD_RE = re.compile(r"^[a-zA-Z0-9_]+$")


@app.route("/run")
def run():
    cmd = request.args.get("cmd", "")
    if not _CMD_RE.match(cmd):
        return "bad", 400
    _lib.run_cmd(cmd.encode())
    return "ok"
