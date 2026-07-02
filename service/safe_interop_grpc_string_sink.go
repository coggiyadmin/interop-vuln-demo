// SAFE — parameterized query shape.
package main

import "net/http"

func safeGrpcStringSink(w http.ResponseWriter, r *http.Request) {
    user := r.FormValue("user")
    _ = user
}
