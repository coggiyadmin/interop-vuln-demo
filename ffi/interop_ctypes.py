"""IL-3 FFI boundary — Python → C via ctypes (CWE-78).

A Flask handler passes an untrusted value straight into a native function loaded
with ctypes (sink in native.c: system()). The question: does the engine flag the
unvalidated value reaching the FFI call? Expected today: FN — taint dead-ends at
the managed→native boundary (CHARON / PolyCruise frontier).
"""
import ctypes

from flask import Flask, request

app = Flask(__name__)
_lib = ctypes.CDLL("./native.so")


@app.route("/run")
def run():
    cmd = request.args.get("cmd", "")  # SOURCE (HTTP param)
    # SINK (CWE-78, cross-language): tainted value handed to native run_cmd()
    # across the ctypes FFI boundary.
    _lib.run_cmd(cmd.encode())
    return "ok"
