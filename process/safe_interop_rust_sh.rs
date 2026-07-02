// IL-2 process boundary — SAFE mirror of interop_rust_sh.rs.
// No shell: the tainted value is passed as a distinct argv element to a fixed
// program (no "sh -c"). The scanner MUST produce ZERO security findings.
use std::process::Command;

pub fn safe_handle(name: &str) {
    if !name.chars().all(|c| c.is_ascii_alphanumeric() || c == '_') {
        return;
    }
    // Safe: argv form, no "sh -c"; name is a separate operand to id.
    let _ = Command::new("id").arg("--").arg(name).status();
}
