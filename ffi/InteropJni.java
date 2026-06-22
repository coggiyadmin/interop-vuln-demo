// IL-3 FFI boundary — Java → C via JNI (CWE-78).
// A servlet passes an untrusted value into a `native` method whose implementation
// lives in native.c (system() sink). Expected today: FN — Java taint dead-ends at
// the JNI call unless a native-callee taint spec is generated (JNI-spec research).
package com.demo.interop;

import javax.servlet.http.HttpServletRequest;

public class InteropJni {

    // JNI declaration; implemented natively in native.c as Java_..._runCmd.
    public native int runCmd(String cmd);

    static {
        System.loadLibrary("native");
    }

    public void handle(HttpServletRequest req) {
        String cmd = req.getParameter("cmd"); // SOURCE (HTTP param)
        // SINK (CWE-78, cross-language): tainted value crosses the JNI boundary
        // into the native run_cmd().
        runCmd(cmd);
    }
}
