//! IL-3 FFI boundary — Rust → C via extern "C" (CWE-78).
//! Passes an untrusted process arg into a C function declared `extern "C"`
//! (run_cmd in native.c → system()). Expected today: FN — taint dead-ends at the
//! FFI call (and Rust taint is also #82-adjacent).
use std::ffi::CString;
use std::os::raw::c_char;

extern "C" {
    fn run_cmd(cmd: *const c_char) -> i32;
}

pub fn handle() {
    let cmd = std::env::args().nth(1).unwrap_or_default(); // SOURCE
    let c = CString::new(cmd).unwrap();
    // SINK (CWE-78, cross-language): tainted value crosses the extern "C" boundary.
    unsafe {
        run_cmd(c.as_ptr());
    }
}
