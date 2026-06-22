// IL-4 — SAFE mirror of interop_json_deserialize_sink.js.
// The deserialized field is bound as a $1 parameter, never concatenated.
// ZERO security findings expected.
const express = require('express');
const { Pool } = require('pg');

const app = express();
const pool = new Pool();

app.post('/ingest', express.text(), (req, res) => {
  const payload = JSON.parse(req.body); // SOURCE
  const name = payload.name;
  // Safe: parameterized query — deserialized field bound, not interpolated.
  pool.query('SELECT * FROM users WHERE name = $1', [name]).then((r) => res.json(r.rows));
});

module.exports = app;
