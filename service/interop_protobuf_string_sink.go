package service

import "database/sql"

// IL-34 — protobuf-decoded string → SQL concat (stub IL-4).
func HandleProtobufPayload(payload string) error {
	q := payload // SOURCE decoded field
	db, _ := sql.Open("sqlite3", ":memory:")
	_, err := db.Exec("SELECT * FROM u WHERE n='" + q + "'") // SINK CWE-89
	return err
}
