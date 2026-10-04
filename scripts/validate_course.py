"""验证课程交付完整性、本地链接和示例语法，不访问外网。"""
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
EXCLUDED = {'.git', 'runs', 'runtime', 'practice', 'memory', '__pycache__'}


def included(path):
    return not any(part in EXCLUDED for part in path.relative_to(ROOT).parts)


def main(output):
    manifest = json.loads((ROOT / 'scripts/assets/course_manifest.json').read_text(encoding='utf-8'))
    assert len(manifest) == 36, '课程数量必须为 36'
    assert len({row['id'] for row in manifest}) == 36, '课程编号重复'
    counts = Counter(row['group'] for row in manifest)
    assert counts == {'ubuntu': 6, 'terminal': 8, 'system': 6, 'programming': 10, 'tools': 6}, counts
    requirements = ('学习目标', '先理解', '预测，再操作', '观察与完成标准', '自己动手', '常见错误', '自检')
    for row in manifest:
        readme, theory = ROOT / row['readme'], ROOT / row['theory']
        assert readme.is_file() and theory.is_file(), row['id']
        text = readme.read_text(encoding='utf-8')
        for heading in requirements:
            assert f'## {heading}' in text, f'{row["id"]} 缺少 {heading}'
        assert len(theory.read_text(encoding='utf-8')) > 220, f'{row["id"]} 理论页过短'
    documents = [path for path in ROOT.rglob('*.md') if included(path)]
    links, failures, bash_blocks = 0, [], 0
    for path in documents:
        text = path.read_text(encoding='utf-8')
        fences = re.findall(r'^\s*```', text, re.M)
        if len(fences) % 2:
            failures.append(f'{path.relative_to(ROOT)}：代码围栏未闭合')
        for block in re.findall(r'^```bash\n(.*?)^```\s*$', text, re.M | re.S):
            bash_blocks += 1
            result = subprocess.run(['/usr/bin/bash', '-n'], input=block,
                                    capture_output=True, text=True)
            if result.returncode:
                failures.append(f'{path.relative_to(ROOT)}：命令块语法错误 {result.stderr}')
        # 移除代码块，避免把示例语法当作链接。
        prose = re.sub(r'^\s*```[^\n]*\n.*?^\s*```\s*$', '', text, flags=re.M | re.S)
        for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^\s)]+)\)', prose):
            parsed = urlsplit(target.strip('<>'))
            if parsed.scheme or not parsed.path:
                continue
            links += 1
            destination = path.parent / unquote(parsed.path)
            if not destination.exists():
                failures.append(f'{path.relative_to(ROOT)}：链接不存在 {target}')
    python_files, shell_files = [], []
    for path in ROOT.rglob('*'):
        if not path.is_file() or not included(path):
            continue
        if path.suffix in {'.py', '.sh', '.cpp', '.hpp', '.h', '.js', '.ts'}:
            assert path.relative_to(ROOT).parts[0] == 'scripts', f'代码必须在 scripts：{path}'
        if path.suffix == '.py':
            compile(path.read_text(encoding='utf-8'), str(path), 'exec')
            python_files.append(str(path.relative_to(ROOT)))
        elif path.suffix == '.sh':
            subprocess.run(['/usr/bin/bash', '-n', str(path)], check=True)
            shell_files.append(str(path.relative_to(ROOT)))
    assert not failures, '\n'.join(failures)
    report = {'lessons': len(manifest), 'theory_pages': len(manifest), 'groups': dict(counts),
              'markdown_files': len(documents), 'local_links': links, 'bash_blocks': bash_blocks,
              'python_syntax': python_files, 'bash_syntax': shell_files,
              'broken_links': failures}
    (output / 'validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'完整性通过：36 节、36 理论页、{len(documents)} 个 Markdown、{links} 个本地链接。')
    print(f'语法通过：{len(python_files)} 个 Python、{len(shell_files)} 个 Bash。')
    print(f'文档命令块语法通过：{bash_blocks} 个。')


if __name__ == '__main__':
    main(Path(sys.argv[1]))
