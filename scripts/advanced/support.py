"""进阶实验的目录、子进程和证据管理，不改变基础入口。"""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import uuid

ROOT = Path(__file__).resolve().parents[2]
PYTHON = '/usr/bin/python3'


def new_run(label):
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    path = ROOT / 'scripts/runs' / f'{stamp}-adv-{label}-{uuid.uuid4().hex[:6]}'
    path.mkdir(parents=True)
    (path / 'tmp').mkdir()
    print(f'实验目录：{path}', flush=True)
    return path


def environment(path):
    value = os.environ.copy()
    for key in ('PYTHONPATH', 'PYTHONHOME', 'CONDA_PREFIX', 'CONDA_DEFAULT_ENV',
                'VIRTUAL_ENV', 'GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE'):
        value.pop(key, None)
    value.update(PATH='/usr/bin:/bin:/usr/sbin:/sbin', TMPDIR=str(path/'tmp'),
                 PIP_CACHE_DIR=str(path/'pip-cache'), PIP_CONFIG_FILE='/dev/null',
                 PYTHONNOUSERSITE='1', PYTHONDONTWRITEBYTECODE='1', GIT_TERMINAL_PROMPT='0')
    return value


def execute(args, path, expected=(0,), cwd=None, echo=True, timeout=45):
    result = subprocess.run([str(x) for x in args], cwd=cwd or path,
                            env=environment(path), capture_output=True,
                            text=True, timeout=timeout)
    with (path/'commands.jsonl').open('a', encoding='utf-8') as stream:
        stream.write(json.dumps({'argv':[str(x) for x in args], 'cwd':str(cwd or path),
                                'returncode':result.returncode, 'stdout':result.stdout,
                                'stderr':result.stderr}, ensure_ascii=False)+'\n')
    if expected is not None and result.returncode not in expected:
        raise RuntimeError(f'命令失败：{args}\n{result.stdout}{result.stderr}')
    if echo and result.stdout:
        print(result.stdout.rstrip())
    return result


def save(path, name, data):
    (path/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def fixture(path):
    rows = ['timestamp,level,component,duration_ms']
    for i, (level, component) in enumerate((('INFO','app'),('INFO','camera'),
                                          ('ERROR','camera'),('WARN','disk'),
                                          ('INFO','app'),('ERROR','camera'),
                                          ('ERROR','network'),('INFO','app'))):
        rows.append(f'2026-10-05T09:00:0{i},{level},{component},{(i+1)*10}')
    rows.append('BROKEN,ROW')
    target = path/'events.csv'
    target.write_text('\n'.join(rows)+'\n', encoding='utf-8')
    return target
