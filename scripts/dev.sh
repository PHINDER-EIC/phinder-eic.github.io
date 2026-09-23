#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_dir"

export PATH="$project_dir/.local-dev/bin:$project_dir/.local-dev/go/bin:$PATH"
export GOPATH="$project_dir/.local-dev/gopath"
export GOCACHE="$project_dir/.local-dev/cache/go-build"
export HUGO_CACHEDIR="$project_dir/.local-dev/cache/hugo"
mkdir -p "$GOPATH" "$GOCACHE" "$HUGO_CACHEDIR"

for tool in hugo go; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    echo "Missing $tool. See README.md for local development setup." >&2
    exit 1
  fi
done

exec hugo server \
  --bind 127.0.0.1 \
  --port 1313 \
  --baseURL http://localhost:1313/ \
  --disableFastRender \
  "$@"
