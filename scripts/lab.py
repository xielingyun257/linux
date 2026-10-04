"""Linux 课程入口。实验使用独立目录，校验真实结果，产物不进入 Git。"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import math
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tarfile
import threading
import urllib.request
import uuid

ROOT = Path(__file__).resolve().parent.parent
PYTHON = Path('/usr/bin/python3')
DEMO_NAMES = ('files', 'text', 'permissions', 'processes', 'network', 'archives', 'git', 'tmux')
PYTHON_NAMES = ('variables', 'flow', 'functions', 'modules', 'files', 'errors')


def new_run(label: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    path = ROOT / 'scripts' / 'runs' / f'{stamp}-{label}-{uuid.uuid4().hex[:8]}'
    path.mkdir(parents=True)
    (path / 'tmp').mkdir()
    print(f'实验目录：{path}', flush=True)
    return path


def child_env(path: Path) -> dict[str, str]:
    env = os.environ.copy()
    for key in ('PYTHONPATH', 'PYTHONHOME', 'VIRTUAL_ENV', 'CONDA_PREFIX',
                'CONDA_DEFAULT_ENV', 'GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE'):
        env.pop(key, None)
    env.update(PATH='/usr/bin:/bin:/usr/sbin:/sbin', TMPDIR=str(path / 'tmp'),
               PYTHONNOUSERSITE='1', GIT_TERMINAL_PROMPT='0')
    return env


def command(args: list[str], path: Path, *, cwd: Path | None = None,
            expected: int = 0, timeout: int = 60) -> str:
    result = subprocess.run([str(a) for a in args], cwd=cwd or path,
                            env=child_env(path), capture_output=True, text=True,
                            timeout=timeout)
    with (path / 'commands.jsonl').open('a', encoding='utf-8') as stream:
        stream.write(json.dumps({'argv': [str(a) for a in args], 'cwd': str(cwd or path),
                                'returncode': result.returncode,
                                'stdout': result.stdout, 'stderr': result.stderr},
                               ensure_ascii=False) + '\n')
    if result.returncode != expected:
        raise RuntimeError(f'命令失败：{args}\n{result.stdout}{result.stderr}')
    if result.stdout:
        print(result.stdout.rstrip())
    return result.stdout


def save_json(path: Path, name: str, value: object) -> None:
    (path / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def environment() -> Path:
    path = new_run('environment')
    tools = {}
    for name in ('bash', 'git', 'g++', 'gdb', 'cmake', 'make', 'nano', 'vim',
                 'code', 'tmux', 'curl', 'wget', 'ssh', 'rsync', 'tar', 'docker'):
        tools[name] = shutil.which(name)
    report = {'repository': str(ROOT), 'system': Path('/etc/os-release').read_text(),
              'course_python': sys.executable, 'python_version': sys.version.split()[0],
              'default_python': shutil.which('python3'), 'tools': tools,
              'inherited_paths': {k: os.environ.get(k) for k in ('CONDA_PREFIX', 'VIRTUAL_ENV', 'PYTHONPATH')},
              'mount': command(['/usr/bin/findmnt', '-T', str(ROOT), '-o', 'TARGET,FSTYPE'], path)}
    save_json(path, 'environment.json', report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return path


def demo(name: str) -> Path:
    path = new_run(name)
    if name == 'files':
        folder = path / '练习 文件'
        folder.mkdir()
        original = folder / '笔记.txt'
        original.write_text('Ubuntu\nLinux\n', encoding='utf-8')
        copied = path / 'copy.txt'
        shutil.copy2(original, copied)
        copied.rename(path / 'renamed.txt')
        assert original.read_bytes() == (path / 'renamed.txt').read_bytes()
        command(['/usr/bin/ls', '-l', str(folder)], path)
        print('中文、空格路径与复制/重命名校验通过。')
    elif name == 'text':
        (path / 'events.log').write_text('INFO start\nERROR camera\nINFO sample\nERROR camera\nERROR network\n', encoding='utf-8')
        result = command(['/usr/bin/bash', '--noprofile', '--norc', '-o', 'pipefail', '-c',
                          "grep '^ERROR' events.log | cut -d ' ' -f 2 | sort | uniq -c"], path)
        counts = {line.split()[1]: int(line.split()[0]) for line in result.splitlines()}
        assert counts == {'camera': 2, 'network': 1}
        save_json(path, 'counts.json', counts)
    elif name == 'permissions':
        fixture = path / 'private.txt'
        fixture.write_text('这是本实验的文件\n', encoding='utf-8')
        before = stat.S_IMODE(fixture.stat().st_mode)
        fixture.chmod(0o600)
        after = stat.S_IMODE(fixture.stat().st_mode)
        report = {'requested': '0600', 'before': oct(before), 'observed': oct(after),
                  'mode_preserved': after == 0o600,
                  'mount': command(['/usr/bin/findmnt', '-T', str(fixture), '-o', 'TARGET,FSTYPE,OPTIONS'], path)}
        save_json(path, 'permissions.json', report)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if after != 0o600:
            print('当前挂载未呈现请求的权限位；请对照文件系统与挂载选项解释。')
    elif name == 'processes':
        process = subprocess.Popen([str(PYTHON), '-I', '-c', 'import time; time.sleep(30)'],
                                   cwd=path, env=child_env(path))
        try:
            observed = command(['/usr/bin/ps', '-p', str(process.pid), '-o', 'pid,ppid,stat,comm'], path)
            assert str(process.pid) in observed
        finally:
            process.terminate()
            try:
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=3)
        assert process.poll() is not None
        save_json(path, 'process.json', {'pid': process.pid, 'returncode': process.returncode,
                                        'reaped': True})
        print('只结束了本实验创建的进程，已回收。')
    elif name == 'network':
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                payload = b'Linux local HTTP lesson\n'
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain')
                self.send_header('Content-Length', str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)

            def log_message(self, format, *args):
                pass

        server = HTTPServer(('127.0.0.1', 0), Handler)
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()
        try:
            url = f'http://127.0.0.1:{server.server_port}/'
            with urllib.request.urlopen(url, timeout=5) as response:
                body = response.read().decode()
                assert response.status == 200 and body == 'Linux local HTTP lesson\n'
            save_json(path, 'network.json', {'url': url, 'status': 200, 'body': body})
            print(f'{url} → HTTP 200\n{body}', end='')
        finally:
            server.shutdown()
            server.server_close()
            worker.join(timeout=3)
        assert not worker.is_alive()
    elif name == 'archives':
        fixture = path / 'notes.txt'
        fixture.write_text('需要保留的练习笔记\n', encoding='utf-8')
        command(['/usr/bin/tar', '-czf', 'notes.tar.gz', 'notes.txt'], path)
        command(['/usr/bin/tar', '-tzf', 'notes.tar.gz'], path)
        with tarfile.open(path / 'notes.tar.gz', 'r:gz') as archive:
            restored = archive.extractfile('notes.txt').read()
        (path / 'restored.txt').write_bytes(restored)
        assert restored == fixture.read_bytes()
        save_json(path, 'archive.json', {'sha256': hashlib.sha256(restored).hexdigest(),
                                       'verified': True})
        print('归档内容与原文件逐字节相同。')
    elif name == 'git':
        repo = path / 'example-repository'
        repo.mkdir()
        command(['/usr/bin/git', 'init', '-b', 'main'], path, cwd=repo)
        command(['/usr/bin/git', 'config', 'user.name', '课程示例作者'], path, cwd=repo)
        command(['/usr/bin/git', 'config', 'user.email', 'student@example.invalid'], path, cwd=repo)
        command(['/usr/bin/git', 'config', 'commit.gpgsign', 'false'], path, cwd=repo)
        (repo / 'notes.md').write_text('# 示例笔记\n', encoding='utf-8')
        command(['/usr/bin/git', 'add', 'notes.md'], path, cwd=repo)
        command(['/usr/bin/git', 'commit', '-m', '添加示例笔记'], path, cwd=repo)
        command(['/usr/bin/git', 'switch', '-c', 'practice'], path, cwd=repo)
        (repo / 'practice.md').write_text('分支练习\n', encoding='utf-8')
        command(['/usr/bin/git', 'add', 'practice.md'], path, cwd=repo)
        command(['/usr/bin/git', 'commit', '-m', '记录分支练习'], path, cwd=repo)
        command(['/usr/bin/git', 'switch', 'main'], path, cwd=repo)
        command(['/usr/bin/git', 'merge', '--no-ff', 'practice', '-m', '合并练习分支'], path, cwd=repo)
        assert not command(['/usr/bin/git', 'status', '--porcelain'], path, cwd=repo).strip()
        log = command(['/usr/bin/git', 'log', '--oneline', '--graph', '--all'], path, cwd=repo)
        assert '合并练习分支' in log and '记录分支练习' in log
        print('示例仓库的本地分支与合并通过。')
    elif name == 'tmux':
        if not Path('/usr/bin/tmux').exists():
            raise RuntimeError('缺少 tmux；先阅读工具课 T05 的安装说明。')
        socket = str(path / 'lesson.sock')
        try:
            command(['/usr/bin/tmux', '-S', socket, 'new-session', '-d', '-s', 'lesson', 'sleep 30'], path)
            sessions = command(['/usr/bin/tmux', '-S', socket, 'list-sessions'], path)
            assert 'lesson:' in sessions
        finally:
            subprocess.run(['/usr/bin/tmux', '-S', socket, 'kill-server'], cwd=path,
                           env=child_env(path), capture_output=True)
        print('独立 tmux 服务已关闭，未使用现有会话的 socket。')
    return path


def python_lesson(name: str) -> Path:
    path = new_run('python-' + name)
    script = ROOT / 'scripts/programming/python' / ('modules/main.py' if name == 'modules' else 'examples.py')
    args = [str(PYTHON), '-E', '-s', str(script)]
    args.extend([str(path)] if name == 'modules' else [name, str(path)])
    command(args, path)
    return path


def bash_lesson(name: str) -> Path:
    path = new_run('bash-' + name)
    command(['/usr/bin/bash', '--noprofile', '--norc',
             str(ROOT / f'scripts/programming/bash/{name}.sh'), str(path)], path)
    return path


def cpp_lesson(name: str) -> Path:
    path = new_run('cpp-' + name)
    source = ROOT / 'scripts/programming/cpp'
    if name == 'intro':
        binary = path / 'angle'
        command(['/usr/bin/g++', '-std=c++17', '-g', '-Wall', '-Wextra', '-pedantic',
                 str(source / 'angle.cpp'), '-o', str(binary)], path)
    else:
        build = path / 'build'
        command(['/usr/bin/cmake', '-S', str(source), '-B', str(build), '-DCMAKE_BUILD_TYPE=Debug'], path)
        command(['/usr/bin/cmake', '--build', str(build), '--parallel', '2'], path)
        binary = build / 'angle'
    output = command([str(binary), '30'], path)
    assert math.isclose(float(output.strip()), math.pi / 6, abs_tol=1e-6)
    command([str(binary), 'invalid'], path, expected=2)
    save_json(path, 'cpp.json', {'degrees': 30, 'radians': float(output.strip()), 'bad_input_exit': 2})
    return path


def project(name: str) -> Path:
    path = new_run('project-' + name)
    command([str(PYTHON), '-I', str(ROOT / f'scripts/projects/{name}.py'), str(path)], path)
    return path


def validate() -> Path:
    path = new_run('validate')
    command([str(PYTHON), '-I', str(ROOT / 'scripts/validate_course.py'), str(path)], path)
    return path


def smoke() -> Path:
    summary = new_run('smoke')
    tasks = [('environment', environment)]
    tasks.extend((f'demo {name}', lambda n=name: demo(n)) for name in DEMO_NAMES)
    tasks.extend((f'python {name}', lambda n=name: python_lesson(n)) for name in PYTHON_NAMES)
    tasks.extend((f'bash {name}', lambda n=name: bash_lesson(n)) for name in ('basics', 'automation'))
    tasks.extend((f'cpp {name}', lambda n=name: cpp_lesson(n)) for name in ('intro', 'cmake'))
    tasks.extend((f'project {name}', lambda n=name: project(n)) for name in ('organize', 'logs', 'debug'))
    tasks.append(('validate', validate))
    results = []
    for label, function in tasks:
        print(f'\n运行：{label}', flush=True)
        try:
            path = function()
            results.append({'task': label, 'status': 'passed', 'path': str(path)})
        except Exception as error:
            results.append({'task': label, 'status': 'failed', 'error': str(error)})
            save_json(summary, 'smoke.json', results)
            raise
    save_json(summary, 'smoke.json', results)
    print(f'\n全部 {len(results)} 项通过。证据：{summary / "smoke.json"}')
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description='Ubuntu / Linux 学习入口；每次生成独立实验目录。')
    sub = parser.add_subparsers(dest='action', required=True)
    for name in ('environment', 'validate', 'smoke'):
        sub.add_parser(name)
    for action, choices in (('demo', DEMO_NAMES), ('python', PYTHON_NAMES),
                            ('bash', ('basics', 'automation')), ('cpp', ('intro', 'cmake')),
                            ('project', ('organize', 'logs', 'debug'))):
        item = sub.add_parser(action)
        item.add_argument('name', choices=choices)
    args = parser.parse_args()
    simple = {'environment': environment, 'validate': validate, 'smoke': smoke}
    named = {'demo': demo, 'python': python_lesson, 'bash': bash_lesson,
             'cpp': cpp_lesson, 'project': project}
    if args.action in simple:
        simple[args.action]()
    else:
        named[args.action](args.name)


if __name__ == '__main__':
    try:
        main()
    except (OSError, RuntimeError, subprocess.SubprocessError, AssertionError) as error:
        print(f'实验未通过：{error}', file=sys.stderr)
        raise SystemExit(1)
