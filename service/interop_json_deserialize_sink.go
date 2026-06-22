// IL-4 serialization boundary — Go JSON deserialize → sink (CWE-89).
// Untrusted JSON crosses the boundary, is unmarshalled, and a field is used in a
// SQL sink. Tests taint survival through json.Unmarshal + struct-field access.
package service

import (
	"database/sql"
	"encoding/json"
	"io"
	"net/http"
)

type dto struct {
	Name string `json:"name"`
}

func Ingest(w http.ResponseWriter, r *http.Request, db *sql.DB) {
	body, _ := io.ReadAll(r.Body)
	var d dto
	json.Unmarshal(body, &d) // SOURCE (untrusted JSON over the boundary)
	name := d.Name           // tainted field survives deserialization
	// SINK (CWE-89): deserialized field concatenated into SQL.
	db.Query("SELECT * FROM users WHERE name = '" + name + "'")
}
