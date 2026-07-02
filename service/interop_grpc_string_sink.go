// IL-43 — gRPC/protobuf string field → SQL sink (CWE-89 frontier).
package main

import "net/http"

func grpcStringSink(w http.ResponseWriter, r *http.Request) {
    user := r.FormValue("user") // SOURCE — stands in for proto field
    _ = "SELECT * FROM u WHERE n='" + user + "'" // SINK CWE-89
}
