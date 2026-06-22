// IL-3 FFI boundary — SAFE mirror of InteropJni.java.
// The user input selects among constant vetted commands; only a literal crosses
// the JNI boundary. ZERO security findings expected.
package com.demo.interop;

import java.util.Map;
import javax.servlet.http.HttpServletRequest;

public class SafeInteropJni {

    public native int runCmd(String cmd);

    static {
        System.loadLibrary("native");
    }

    private static final Map<String, String> ALLOWED = Map.of(
        "status", "systemctl status app",
        "uptime", "uptime");

    public void handle(HttpServletRequest req) {
        String action = req.getParameter("action"); // SOURCE
        String cmd = ALLOWED.get(action);            // allowlist → constant literal
        if (cmd == null) {
            return;
        }
        runCmd(cmd);                                  // only a constant crosses JNI
    }
}
