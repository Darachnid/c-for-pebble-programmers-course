#!/usr/bin/env bash
# Manual dual-emulator smoke script. Does not prove physical sensor behavior.
set -euo pipefail
if [[ $# -ne 1 ]]; then
  echo "Usage: bash scripts/test_dual_platform.sh lessons/12A/starter" >&2
  exit 2
fi
repo="$(cd "$(dirname "$0")/.." && pwd)"
project="$repo/$1"
if [[ ! -f "$project/package.json" || ! -f "$project/wscript" ]]; then
  echo "Not a standalone Pebble C project: $project" >&2
  exit 2
fi
if ! command -v pebble >/dev/null 2>&1; then
  echo "Pebble CLI unavailable; install/activate SDK 4.33.1 first" >&2
  exit 127
fi
(
 cd "$project"
 echo "Building both platform binaries in $project"
 pebble build
 for platform in emery gabbro; do
   echo "Installing and checking $platform emulator (must be configured)"
   pebble install --emulator "$platform"
 done
)
echo "Both installs returned successfully. Inspect both screens, run input tests and save logs manually."
