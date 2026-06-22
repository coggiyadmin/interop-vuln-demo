// IL-3 FFI boundary — Go → C via cgo (CWE-78).
// An HTTP handler passes an untrusted value into a C function via cgo (run_cmd in
// native.c → system()). Expected today: FN — Go taint dead-ends at the cgo call.
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

func Handle(w http.ResponseWriter, r *http.Request) {
	cmd := r.URL.Query().Get("cmd") // SOURCE (HTTP param)
	c := C.CString(cmd)
	defer C.free(unsafe.Pointer(c))
	// SINK (CWE-78, cross-language): tainted value crosses the cgo boundary.
	C.run_cmd(c)
}
