#!/usr/bin/bash
# 固定系统 Python，仅在子进程使用隔离参数，不改用户的 Shell 配置。
set -euo pipefail
linux_repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
exec /usr/bin/python3 -I "$linux_repo_root/scripts/lab.py" "$@"
