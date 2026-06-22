//! IL-3 FFI boundary — SAFE mirror of interop_extern_c.rs.
//! The user input selects among constant vetted commands; only a literal crosses
//! the extern "C" boundary. ZERO security findings expected.
use std::ffi::CString;
use std::os::raw::c_char;

extern "C" {
    fn run_cmd(cmd: *const c_char) -> i32;
}

pub fn handle() {
    let action = std::env::args().nth(1).unwrap_or_default(); // SOURCE
    let cmd = match action.as_str() {
        "status" => "systemctl status app",
        "uptime" => "uptime",
        _ => return,
    }; // allowlist → constant literal
    let c = CString::new(cmd).unwrap();
    unsafe {
        run_cmd(c.as_ptr()); // only a constant crosses the FFI boundary
    }
}
