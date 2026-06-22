# IL-3 — FFI / native boundary

Managed runtime calls native code across an FFI edge. The deepest frontier (CHARON,
PolyCruise, JNI caller-sensitive specs). `native.c` is a **stub documenting the sink**; the
test is whether the engine flags the unvalidated value *reaching* the FFI call.

Planned fixtures (TP + `safe_*` + `benign_*` each):

| Fixture | Boundary | CWE | Expected today |
|---------|----------|-----|----------------|
| `interop_ctypes.py` (+ `native.c`) | Python `ctypes`/`cffi` → C | 78/787 | **FN** — taint dead-ends at FFI |
| `InteropJni.java` (+ `native.c`) | Java JNI → C | 78/787 | **FN** |
| `interop_cgo.go` | Go cgo → C | 78 | **FN** |
| `interop_napi.js` (+ addon stub) | Node N-API / `ffi-napi` → C | 78 | **FN** |
| `interop_pyo3.rs` / `extern_c.rs` | Rust → C / PyO3 | 78 | **FN** (Rust also #82-blocked) |
