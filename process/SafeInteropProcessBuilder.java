// IL-2 process boundary — SAFE mirror of InteropProcessBuilder.java.
// No shell: the tainted host is passed as a distinct argv element to a fixed
// program after a strict allowlist check. The scanner MUST produce ZERO findings.
package com.demo.interop;

import java.io.IOException;
import javax.servlet.http.HttpServletRequest;

public class SafeInteropProcessBuilder {

    public void handle(HttpServletRequest req) throws IOException {
        String host = req.getParameter("host"); // SOURCE
        if (host == null || !host.matches("[a-zA-Z0-9.-]+")) {
            return; // strict hostname allowlist — no shell metacharacters possible
        }
        // Safe: argv array, no "sh -c"; host is a separate operand to ping.
        new ProcessBuilder("ping", "-c", "1", "--", host).start();
    }
}
