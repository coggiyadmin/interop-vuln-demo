# interop-vuln-demo

**Cross-binary** interoperability fixtures for SAST validation — taint flows that cross a
**language/runtime boundary spanning two artifacts**. Single-language fixtures and
in-language polyglot (templates, SSTI, config) live in the per-language `*-vuln-demo` repos'
`interop/` subdir instead; this repo is only for cases that span two runtimes and therefore
belong to no single-language repo.

Plan & rationale: `cogniumhq/sast-validation/research/cross-language-interop-plan.md`
(families **IL-2 process**, **IL-3 FFI/native**, **IL-4 serialization/service**).

## Layout

| Dir | Family | Boundary | Typical expected verdict |
|-----|--------|----------|--------------------------|
| `process/` | IL-2 | host `exec`/`spawn` → another runtime (py↔bash, node↔py, java↔sh, go↔sh) | cmd-inj sink fires; downstream child-script taint **lost** (FN) |
| `ffi/` | IL-3 | managed → native (ctypes/cffi, JNI, cgo, N-API, PyO3) | **FN** — taint dead-ends at the FFI call (research frontier) |
| `service/` | IL-4 | service→service / serialize→deserialize→sink (JSON, protobuf, gRPC) | partial → FN |

## 4-quadrant contract (same as every vuln-demo repo)

Each boundary case ships the full trio:
- **TP** probe — `interop_*` / `Interop*` — the unvalidated value reaches the boundary sink.
- **FP** mirror — `safe_interop_*` / `SafeInterop*` — boundary crossed with validation/allowlist; must scan to **0** security findings.
- **TN** — `benign_interop_*` — boundary crossed with no untrusted data; must scan to **0**.

Native/second-runtime counterparts (`native.c`, `*.proto`, a second service stub) are
**stubs that document the downstream sink** — the validation question is whether the engine
flags the value *reaching* the boundary, not whether it analyzes the native body.

## Conventions

One flow per file · bind the source to a local var (avoid the #83 inline-source confound) ·
explicit `// SOURCE` and `// SINK (CWE-NNN)` tags · no vendor/campaign names in comments.

## Scan / gate

Scans run from `sast-validation` (`scripts/gate-interop.sh`, planned). Expected MISSes are
tracked as the **FN-IL-NN** series in `research/gate-defect-log.md` and filed as cognium-dev
feature requests only after a confirmed miss (the #86 / supply-chain workflow).
