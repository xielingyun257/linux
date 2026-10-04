#!/usr/bin/bash
# 先运行最小全流程。所有文件、环境和构建均留在本仓库。
set -euo pipefail
linux_repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
linux_warmup_dir="${linux_repo_root}/scripts/runtime/warmup-$(date -u +%Y%m%dT%H%M%S)-${BASHPID}"
mkdir -p -- "$linux_warmup_dir"
mkdir -p -- "$linux_warmup_dir/tmp"
export TMPDIR="$linux_warmup_dir/tmp"
printf '仓库：%s\n热身目录：%s\n' "$linux_repo_root" "$linux_warmup_dir"
printf '系统解释器：'; /usr/bin/python3 --version
printf '默认解释器：'; command -v python3
printf 'Bash：'; command -v bash
printf 'Git：'; command -v git
printf '编译器：'; command -v g++
printf 'CMake：'; command -v cmake
printf '挂载：\n'; findmnt -T "$linux_repo_root" -o TARGET,FSTYPE
/usr/bin/python3 -I - "$linux_warmup_dir" <<'PY'
from pathlib import Path
import json, subprocess, sys, tarfile
root = Path(sys.argv[1])
fixture = root / 'sample.txt'
fixture.write_text('INFO start\nERROR example\nINFO done\n', encoding='utf-8')
result = subprocess.run(['/usr/bin/bash', '--noprofile', '--norc', '-c',
    'grep ERROR sample.txt | wc -l'], cwd=root, check=True, capture_output=True, text=True)
assert result.stdout.strip() == '1'
subprocess.run(['/usr/bin/python3', '-I', '-m', 'venv', '--system-site-packages', str(root / 'venv')], check=True)
probe = subprocess.run([str(root / 'venv/bin/python'), '-I', '-c',
    'import sys; print(sys.executable); print(sys.prefix); print(sys.base_prefix)'],
    check=True, capture_output=True, text=True)
print('仓库内 venv：\n' + probe.stdout, end='')
source = root / 'hello.cpp'
source.write_text('#include <iostream>\nint main(){std::cout << 2+3 << "\\n";}\n', encoding='utf-8')
subprocess.run(['/usr/bin/g++', '-std=c++17', str(source), '-o', str(root / 'hello')], check=True)
cpp = subprocess.run([str(root / 'hello')], check=True, capture_output=True, text=True)
assert cpp.stdout.strip() == '5'
with tarfile.open(root / 'sample.tar.gz', 'w:gz') as archive:
    archive.add(fixture, arcname='sample.txt')
with tarfile.open(root / 'sample.tar.gz', 'r:gz') as archive:
    assert archive.extractfile('sample.txt').read() == fixture.read_bytes()
report = {'python':sys.executable, 'shell_pipeline':'passed', 'venv':'passed',
          'cpp':'passed', 'archive':'passed'}
(root / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print('热身通过：终端管道 → Python → venv → C++ 编译运行 → 归档校验。')
PY
