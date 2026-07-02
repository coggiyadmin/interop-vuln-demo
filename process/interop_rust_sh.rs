// IL-2 process boundary — Rust → sh (CWE-78).
// An HTTP handler taints a value interpolated into a shell command run via
// std::process::Command sh -c, crossing the Rust→shell process boundary.
//   (a) command-injection sink at the spawn → expected FIRES
//   (b) taint into the child shell script   → expected LOST (FN-IL)
use std::process::Command;

pub fn handle(name: &str) {
    // SOURCE (HTTP param passed in by caller)
    // SINK (CWE-78): tainted value interpolated into an sh -c command string.
    let _ = Command::new("sh")
        .args(["-c", &format!("id {}", name)])
        .status();
}
