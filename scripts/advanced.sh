#!/usr/bin/bash
set -euo pipefail
linux_advanced_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
exec /usr/bin/python3 -I "$linux_advanced_root/scripts/advanced_lab.py" "$@"
