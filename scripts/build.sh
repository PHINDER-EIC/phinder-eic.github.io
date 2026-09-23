#!/usr/bin/env bash
# Build and validate an isolated production artifact; does not publish anything.
set -euo pipefail
project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_dir"
export PATH="$project_dir/.local-dev/bin:$project_dir/.local-dev/go/bin:$PATH"
export GOPATH="$project_dir/.local-dev/gopath"
export GOCACHE="$project_dir/.local-dev/cache/go-build"
export HUGO_CACHEDIR="$project_dir/.local-dev/cache/hugo"
mkdir -p "$GOPATH" "$GOCACHE" "$HUGO_CACHEDIR"
hugo --gc --minify --environment production --cleanDestinationDir \
  --destination "$project_dir/.local-dev/release-build"
python3 scripts/check-site.py "$project_dir/.local-dev/release-build"
