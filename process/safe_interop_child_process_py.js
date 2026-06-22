// IL-2 process boundary — SAFE mirror of interop_child_process_py.js.
// Uses execFile with an argument array (no shell) and a numeric guard, so the
// tainted value can never be interpreted as code or shell syntax. The scanner
// MUST produce ZERO security findings.
const express = require('express');
const { execFile } = require('child_process');

const app = express();

app.get('/calc', (req, res) => {
  const expr = String(req.query.expr ?? ''); // SOURCE
  if (!/^[0-9+\-*/(). ]+$/.test(expr)) {      // strict numeric-expression allowlist
    res.status(400).end();
    return;
  }
  // Safe: execFile passes args as a distinct array; no shell, validated input.
  execFile('python3', ['-c', 'import ast,sys;print(ast.literal_eval(sys.argv[1]))', expr], (err, stdout) => {
    res.send(stdout);
  });
});

module.exports = app;
