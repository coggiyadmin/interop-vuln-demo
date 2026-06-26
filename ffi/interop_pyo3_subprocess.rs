// IL-35 — Rust PyO3 boundary stub: foreign string → shell (IL-3).
use std::process::Command;

pub fn pyo3_handle(user_supplied: &str) {
    let arg = user_supplied.to_string(); // SOURCE FFI
    let _ = Command::new("sh")
        .arg("-c")
        .arg(format!("echo {}", arg)) // SINK CWE-78
        .spawn();
}
