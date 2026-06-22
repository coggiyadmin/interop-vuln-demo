"""IL-2 process boundary — SAFE mirror of interop_subprocess_bash.py.
No shell: the tainted value is passed as a distinct argv element to a fixed
program (no `bash -c` string). The scanner MUST produce ZERO security findings.
"""
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/backup")
def backup():
    target = request.args.get("dir", "")  # SOURCE
    # Safe: argv array, no shell — `target` is an operand to tar, never parsed
    # as shell syntax. The "--" terminator also blocks option injection.
    subprocess.run(["tar", "czf", "backup.tgz", "--", target])
    return "ok"
