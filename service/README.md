# IL-4 — Serialization / service boundary

Taint survives a serialize/deserialize hop or an inter-service call. `*.proto` and the
second-service file are stubs documenting the downstream sink.

Planned fixtures (TP + `safe_*` + `benign_*` each):

| Fixture | Boundary | CWE | Expected today |
|---------|----------|-----|----------------|
| `interop_json_deserialize_sink.{py,js,java,go}` | JSON over module boundary → sink | 502/89 | partial |
| `interop_protobuf_grpc.{py,go}` (+ `*.proto`) | protobuf/gRPC field → handler sink | 89/78 | FN (proto field as source not modeled) |
| `interop_svc_a_to_b.py` (+ `svc_b.py`) | HTTP body in svc-A → forwarded → sink in svc-B | 918/89 | FN (cross-service taint) |
