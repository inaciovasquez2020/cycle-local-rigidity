#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
if command -v sha256sum >/dev/null 2>&1; then
sha256sum -c certificate.sha256
elif command -v shasum >/dev/null 2>&1; then
shasum -a 256 -c certificate.sha256
else
echo "ERROR: need sha256sum or shasum."
exit 1
fi

echo "OK: certificate verified."
