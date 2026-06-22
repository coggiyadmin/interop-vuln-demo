// IL-4 — SAFE mirror of interop_json_deserialize_sink.go.
// The deserialized field is bound as a $1 parameter, never concatenated.
// ZERO security findings expected.
package service

import (
	"database/sql"
	"encoding/json"
	"io"
	"net/http"
)

type safeDto struct {
	Name string `json:"name"`
}

func SafeIngest(w http.ResponseWriter, r *http.Request, db *sql.DB) {
	body, _ := io.ReadAll(r.Body)
	var d safeDto
	json.Unmarshal(body, &d) // SOURCE
	// Safe: parameterized query — deserialized field bound, not interpolated.
	db.Query("SELECT * FROM users WHERE name = $1", d.Name)
}
