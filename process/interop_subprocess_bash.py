"""IL-2 process boundary — Python → bash (CWE-78).

A Flask handler taints an argument that is interpolated into a shell string and
executed by bash via subprocess. Two questions for the engine:
  (a) does the command-injection sink fire at the spawn?  (expected: FIRES)
  (b) is taint into the *child* bash script tracked?       (expected: LOST — FN-IL)
"""
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/backup")
def backup():
    target = request.args.get("dir", "")  # SOURCE (HTTP param)
    # SINK (CWE-78): tainted value interpolated into a bash -c command string,
    # crossing the Python→bash process boundary.
    subprocess.run(["bash", "-c", "tar czf backup.tgz " + target])
    return "ok"
