// SAFE mirror — IL-4 protobuf: bound field used only in parameterized query shape.
package main

import "net/http"

func safeProtobufSink(w http.ResponseWriter, r *http.Request) {
	user := r.FormValue("user")
	_ = user
}
