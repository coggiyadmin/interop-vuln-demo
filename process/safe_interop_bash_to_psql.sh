#!/bin/bash
# IL-2 process boundary — SAFE mirror of interop_bash_to_psql.sh.
# The tainted value is bound as a psql variable and quoted via quote_literal in
# the SQL, never concatenated into the statement text. The scanner MUST produce
# ZERO security findings.
set -euo pipefail

name="$1"   # SOURCE (CLI arg)

# Safe: value passed out-of-band with -v and bound through quote_literal(), so it
# is treated strictly as data — no SQL string concatenation.
psql -d app -v name="$name" -c \
  'SELECT * FROM users WHERE name = quote_literal(:''name'')'
