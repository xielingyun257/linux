#!/usr/bin/bash
set -euo pipefail
linux_learning_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
case "${1:-}" in
  base) shift; exec /usr/bin/bash "$linux_learning_root/scripts/study.sh" "$@" ;;
  advanced) shift; exec /usr/bin/bash "$linux_learning_root/scripts/advanced.sh" "$@" ;;
  *) exec /usr/bin/python3 -I "$linux_learning_root/scripts/learn.py" "$@" ;;
esac
