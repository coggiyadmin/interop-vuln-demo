"""IL-30 — msgpack deserialize then SQL sink (service boundary)."""
import sqlite3

def handle(raw: bytes) -> None:
    import msgpack  # type: ignore
    obj = msgpack.unpackb(raw, raw=False)  # SOURCE IL-4
    q = obj.get("q", "")
    sqlite3.connect(":memory:").execute("SELECT * FROM t WHERE n='" + str(q) + "'")  # SINK
