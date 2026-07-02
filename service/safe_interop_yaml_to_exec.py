"""SAFE — allowlisted command only."""
import os
import yaml

ALLOWED = {"echo", "date"}

def load_and_run(raw: bytes):
    cfg = yaml.safe_load(raw)
    cmd = cfg.get("cmd", "echo")
    if cmd not in ALLOWED:
        raise ValueError(cmd)
    os.execvp(cmd, [cmd])
