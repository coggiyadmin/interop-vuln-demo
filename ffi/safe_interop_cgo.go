// IL-3 FFI boundary — SAFE mirror of interop_cgo.go.
// The user input selects among constant vetted commands; only a literal crosses
// the cgo boundary. ZERO security findings expected.
package ffi

/*
#include <stdlib.h>
int run_cmd(const char *cmd);
*/
import "C"
import (
	"net/http"
	"unsafe"
)

var allowed = map[string]string{
	"status": "systemctl status app",
	"uptime": "uptime",
}

func SafeHandle(w http.ResponseWriter, r *http.Request) {
	action := r.URL.Query().Get("action") // SOURCE
	cmd, ok := allowed[action]            // allowlist → constant literal
	if !ok {
		return
	}
	c := C.CString(cmd)
	defer C.free(unsafe.Pointer(c))
	C.run_cmd(c) // only a constant crosses cgo
}
