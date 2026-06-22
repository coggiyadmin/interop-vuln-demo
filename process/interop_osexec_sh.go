// IL-2 process boundary — Go → sh (CWE-78).
// An HTTP handler taints a value interpolated into a shell command run via
// os/exec sh -c, crossing the Go→shell process boundary.
//   (a) command-injection sink at the spawn → expected FIRES
//   (b) taint into the child shell script   → expected LOST (FN-IL)
package process

import (
	"net/http"
	"os/exec"
)

func Handle(w http.ResponseWriter, r *http.Request) {
	name := r.URL.Query().Get("name") // SOURCE (HTTP param)
	// SINK (CWE-78): tainted value interpolated into an sh -c command string.
	exec.Command("sh", "-c", "id "+name).Run()
}
