// IL-2 process boundary — Java → sh (CWE-78).
// A servlet taints a value interpolated into a shell command run via
// ProcessBuilder("sh","-c", ...), crossing the Java→shell process boundary.
//   (a) command-injection sink at the spawn → expected FIRES
//   (b) taint into the child shell script   → expected LOST (FN-IL)
package com.demo.interop;

import java.io.IOException;
import javax.servlet.http.HttpServletRequest;

public class InteropProcessBuilder {

    public void handle(HttpServletRequest req) throws IOException {
        String host = req.getParameter("host"); // SOURCE (HTTP param)
        // SINK (CWE-78): tainted value interpolated into an sh -c command string.
        new ProcessBuilder("sh", "-c", "ping -c 1 " + host).start();
    }
}
