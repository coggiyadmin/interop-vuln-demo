package interop.service;

import java.util.Properties;

/** SAFE mirror — IL-5: allowlisted property keys only. */
public class SafeInteropPropertiesExec {
    private static final java.util.Set<String> ALLOWED = java.util.Set.of("cmd", "timeout");

    public void load(Properties p) throws Exception {
        for (String k : p.stringPropertyNames()) {
            if (!ALLOWED.contains(k)) throw new SecurityException(k);
        }
        String cmd = p.getProperty("cmd", "echo");
        Runtime.getRuntime().exec(new String[]{cmd});
    }
}
