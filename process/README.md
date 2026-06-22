# IL-2 — Process boundary

Host runtime taints an argument; the spawned process is a **different language**. Two
questions per fixture: (a) does the cmd-injection sink fire at the spawn? (b) is taint into
the child script tracked at all?

Planned fixtures (TP + `safe_*` + `benign_*` each):

| Fixture | Host → child | CWE | Expected today |
|---------|--------------|-----|----------------|
| `interop_subprocess_bash.py` (+ `child.sh`) | Python `subprocess` → bash `-c` | 78 | sink fires; child-script taint lost |
| `interop_child_process_py.js` (+ `child.py`) | Node `child_process` → `python -c` | 78/94 | sink fires; child taint lost |
| `InteropProcessBuilder.java` (+ `child.sh`) | Java `ProcessBuilder` → sh | 78 | sink fires; child taint lost |
| `interop_osexec_sh.go` (+ `child.sh`) | Go `os/exec` → sh | 78 | sink fires; child taint lost |
| `interop_bash_to_psql.sh` | bash → `psql -c "$q"` | 89 | likely FN (bash→SQL) |
