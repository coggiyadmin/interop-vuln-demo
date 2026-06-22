// IL-4 serialization boundary — Java JSON deserialize → sink (CWE-89).
// Untrusted JSON crosses the boundary, is deserialized via Jackson, and a field
// is used in a SQL sink. Tests taint survival through readValue + getter access.
package com.demo.interop;

import com.fasterxml.jackson.databind.ObjectMapper;
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;
import javax.servlet.http.HttpServletRequest;

public class InteropJsonDeserialize {

    static class Dto {
        public String name;
    }

    private final ObjectMapper mapper = new ObjectMapper();

    public void ingest(HttpServletRequest req, Connection conn) throws Exception {
        Dto dto = mapper.readValue(req.getInputStream(), Dto.class); // SOURCE (JSON)
        String name = dto.name; // tainted field survives deserialization
        Statement st = conn.createStatement();
        // SINK (CWE-89): deserialized field concatenated into SQL.
        st.executeQuery("SELECT * FROM users WHERE name = '" + name + "'");
    }
}
