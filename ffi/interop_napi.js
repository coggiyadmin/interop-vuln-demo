// IL-3 FFI boundary — Node.js → C via ffi-napi / N-API (CWE-78).
// An Express handler passes an untrusted value into a native addon function
// (run_cmd in native.c → system()). Expected today: FN — taint dead-ends at the
// N-API/FFI call.
const express = require('express');
const ffi = require('ffi-napi');

const native = ffi.Library('./native', { run_cmd: ['int', ['string']] });
const app = express();

app.get('/run', (req, res) => {
  const cmd = req.query.cmd; // SOURCE (HTTP param)
  // SINK (CWE-78, cross-language): tainted value crosses the FFI boundary into
  // native run_cmd().
  native.run_cmd(cmd);
  res.end();
});

module.exports = app;
