/** IL-31 — TypeScript spawns Node child with tainted argv. */
import { spawn } from 'child_process';

export function run(userArg: string) {
  spawn('node', ['-e', 'console.log(' + userArg + ')']); // SOURCE/SINK IL-2
}
