// IL-2 process boundary — Node.js → Python (CWE-78/94).
// An Express handler taints a value interpolated into a `python -c` snippet and
// executed via child_process.exec, crossing the Node→Python process boundary.
//   (a) command-injection sink at the spawn  → expected FIRES
//   (b) taint into the child Python script   → expected LOST (FN-IL)
const express = require('express');
const { exec } = require('child_process');

const app = express();

app.get('/calc', (req, res) => {
  const expr = req.query.expr; // SOURCE (HTTP param)
  // SINK (CWE-78): tainted value built into a python -c program string.
  exec('python3 -c "print(' + expr + ')"', (err, stdout) => {
    res.send(stdout);
  });
});

module.exports = app;
