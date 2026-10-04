"""CSV 日志巡检工具：明确输入、拒绝覆盖、用退出状态表达检查结果。"""
import argparse
from collections import Counter
import csv
from dataclasses import asdict
import json
from pathlib import Path
import sys
from event_model import Event

ROOT = Path(__file__).resolve().parents[2]


def summarize(source):
    events, invalid = [], []
    with source.open(encoding='utf-8', newline='') as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != ['timestamp', 'level', 'component', 'duration_ms']:
            raise ValueError('表头应为 timestamp,level,component,duration_ms')
        for row in reader:
            try:
                if None in row:
                    raise ValueError('多余字段')
                events.append(Event.from_row(row))
            except ValueError as error:
                invalid.append({'line':reader.line_num, 'reason':str(error)})
    levels = Counter(item.level for item in events)
    total = len(events)
    return {'valid_records':total, 'levels':dict(levels), 'invalid_records':invalid,
            'error_rate':levels['ERROR']/total if total else None,
            'mean_duration_ms':sum(item.duration_ms for item in events)/total if total else None,
            'events':[asdict(item) for item in events]}


def rate(value):
    result = float(value)
    if not 0 <= result <= 1:
        raise argparse.ArgumentTypeError('阈值应在 0～1 之间')
    return result


def main():
    parser = argparse.ArgumentParser(description='读取教学 CSV 日志并生成巡检报告。')
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--max-error-rate', type=rate, default=1.0)
    parser.add_argument('--strict', action='store_true', help='有格式错误时返回状态 3')
    args = parser.parse_args()
    try:
        output = args.output.resolve()
        if ROOT not in output.parents:
            raise ValueError('输出必须位于本仓库内')
        report = summarize(args.input)
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open('x', encoding='utf-8') as stream:
            json.dump(report, stream, ensure_ascii=False, indent=2)
            stream.write('\n')
    except (OSError, ValueError, csv.Error) as error:
        print(f'输入或输出错误：{error}', file=sys.stderr)
        return 2
    print(f'合法记录 {report["valid_records"]}，格式问题 {len(report["invalid_records"])}，错误率 {report["error_rate"]}')
    if args.strict and report['invalid_records']:
        return 3
    if not report['valid_records']:
        return 5
    if report['error_rate'] is not None and report['error_rate'] > args.max_error_rate:
        return 4
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
