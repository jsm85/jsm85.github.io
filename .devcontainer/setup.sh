#!/usr/bin/env bash
# Runs once, when the dev container is created.
set -euo pipefail

# script/contrast-audit.py is part of the normal workflow, but the Ruby image
# doesn't guarantee a Python. Install one only if it's actually missing.
if ! command -v python3 >/dev/null 2>&1; then
  echo "→ Installing python3 (needed by script/contrast-audit.py)"
  sudo apt-get update -qq
  sudo apt-get install -y -qq --no-install-recommends python3
fi

echo "→ Installing gems into ./vendor/bundle"
bundle config set --local path 'vendor/bundle'
bundle install

cat <<'EOF'

  Ready.

    bundle exec jekyll serve --livereload   # http://localhost:4000
    python3 script/contrast-audit.py        # re-check colour contrast

EOF
