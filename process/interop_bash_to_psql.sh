#!/bin/bash
# IL-2 process boundary — bash → PostgreSQL (CWE-89).
# A bash script taints a CLI argument interpolated into a SQL string and executed
# by psql -c, crossing the bash→SQL(psql) boundary.
#   (a) SQL-injection sink at the psql call → likely FN (bash→SQL boundary)
#   (b) downstream SQL taint                → expected LOST (FN-IL)

name="$1"   # SOURCE (CLI arg)

# SINK (CWE-89): tainted value concatenated into the SQL passed to psql -c.
psql -d app -c "SELECT * FROM users WHERE name = '$name'"
