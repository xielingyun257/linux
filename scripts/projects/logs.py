"""生成教学日志，统计合法记录，单独报告格式错误。"""
from collections import Counter
import json
from pathlib import Path
import re
import sys

PATTERN = re.compile(r'^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}) (INFO|WARN|ERROR) (\w+) (.+)$')


def summarize(text):
    levels, components = Counter(), Counter()
    invalid = []
    for number, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        match = PATTERN.fullmatch(line)
        if not match:
            invalid.append(number)
            continue
        _, level, component, _ = match.groups()
        levels[level] += 1
        if level == 'ERROR':
            components[component] += 1
    return {'valid_records': sum(levels.values()), 'levels': dict(levels),
            'error_components': dict(components), 'invalid_lines': invalid}


def main(output):
    entries = [('INFO', 'app', 'start'), ('INFO', 'camera', 'connected'),
               ('ERROR', 'camera', 'timeout'), ('WARN', 'disk', 'slow'),
               ('INFO', 'app', 'retry'), ('ERROR', 'camera', 'timeout'),
               ('ERROR', 'network', 'unreachable'), ('INFO', 'app', 'done')]
    text = '\n'.join(f'2026-10-05T09:00:0{i} {level} {component} {message}'
                     for i, (level, component, message) in enumerate(entries)) + '\nBAD RECORD\n'
    source = output / 'events.log'
    source.write_text(text, encoding='utf-8')
    report = summarize(source.read_text(encoding='utf-8'))
    assert report['valid_records'] == 8
    assert report['levels'] == {'INFO': 4, 'ERROR': 3, 'WARN': 1}
    assert report['error_components'] == {'camera': 2, 'network': 1}
    assert report['invalid_lines'] == [9]
    (output / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main(Path(sys.argv[1]))
