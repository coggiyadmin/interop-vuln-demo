// IL-3 FFI boundary — SAFE mirror of interop_napi.js.
// The user input selects among constant vetted commands; only a literal crosses
// the FFI boundary. ZERO security findings expected.
const express = require('express');
const ffi = require('ffi-napi');

const native = ffi.Library('./native', { run_cmd: ['int', ['string']] });
const app = express();

const ALLOWED = { status: 'systemctl status app', uptime: 'uptime' };

app.get('/run', (req, res) => {
  const action = req.query.action; // SOURCE
  const cmd = ALLOWED[action];     // allowlist → constant literal
  if (!cmd) {
    res.status(400).end();
    return;
  }
  native.run_cmd(cmd); // only a constant crosses the FFI boundary
  res.end();
});

module.exports = app;
