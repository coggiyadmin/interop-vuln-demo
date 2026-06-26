/** SAFE mirror — IL-2 ts spawn: fixed script path, tainted value as argv only. */
import { spawn } from 'child_process';
import express from 'express';

const app = express();
app.get('/run', (req, res) => {
  const arg = String(req.query.arg ?? '');
  spawn('node', ['-e', 'console.log(process.argv[2])', arg]);
  res.end('ok');
});
export default app;
