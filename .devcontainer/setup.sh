#!/usr/bin/env bash
# Runs once when the dev container is created.
set -euo pipefail

echo "→ Installing gems into ./vendor/bundle"
bundle config set --local path 'vendor/bundle'
bundle install

echo
echo "  Ready. Start the site with:"
echo "    bundle exec jekyll serve --livereload"
echo
