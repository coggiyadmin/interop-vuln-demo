"""IL-44 — YAML config value → os exec (CWE-94 frontier)."""
import os
import yaml

def load_and_run(raw: bytes):
    cfg = yaml.safe_load(raw)  # SOURCE
    cmd = cfg.get("cmd", "echo")
    os.system(cmd)  # SINK CWE-78
