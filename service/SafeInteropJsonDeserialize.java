// IL-4 — SAFE mirror of InteropJsonDeserialize.java.
// The deserialized field is bound via a PreparedStatement, never concatenated.
// ZERO security findings expected.
package com.demo.interop;

import com.fasterxml.jackson.databind.ObjectMapper;
import java.sql.Connection;
import java.sql.PreparedStatement;
import javax.servlet.http.HttpServletRequest;

public class SafeInteropJsonDeserialize {

    static class Dto {
        public String name;
    }

    private final ObjectMapper mapper = new ObjectMapper();

    public void ingest(HttpServletRequest req, Connection conn) throws Exception {
        Dto dto = mapper.readValue(req.getInputStream(), Dto.class); // SOURCE
        // Safe: PreparedStatement with a bound parameter — no concatenation.
        PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE name = ?");
        ps.setString(1, dto.name);
        ps.executeQuery();
    }
}
