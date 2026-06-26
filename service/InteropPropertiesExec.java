package interop.service;

import java.io.*;
import java.util.*;

/** IL-32 — Java Properties load → Runtime.exec */
public class InteropPropertiesExec {
    public void loadAndRun(InputStream in) throws Exception {
        Properties p = new Properties();
        p.load(in); // SOURCE IL-5 config
        String cmd = p.getProperty("cmd", "");
        Runtime.getRuntime().exec(cmd); // SINK CWE-78
    }
}
