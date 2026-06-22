// IL-2 process boundary — SAFE mirror of interop_osexec_sh.go.
// No shell: the tainted value is passed as a distinct argv element to a fixed
// program (no "sh -c"). The scanner MUST produce ZERO security findings.
package process

import (
	"net/http"
	"os/exec"
	"regexp"
)

var nameRe = regexp.MustCompile(`^[a-zA-Z0-9_]+$`)

func SafeHandle(w http.ResponseWriter, r *http.Request) {
	name := r.URL.Query().Get("name") // SOURCE
	if !nameRe.MatchString(name) {
		return // strict allowlist — no shell metacharacters possible
	}
	// Safe: argv form, no "sh -c"; name is a separate operand to id.
	exec.Command("id", "--", name).Run()
}
