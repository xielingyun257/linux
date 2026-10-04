"""对比整数除法错误与修复结果；提供 VS Code / pdb 调试入口。"""
import argparse
import json
from pathlib import Path


def wrong_mean(values):
    return sum(values) // len(values)


def correct_mean(values):
    if not values:
        raise ValueError('至少需要一个数值')
    return sum(values) / len(values)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('output', type=Path)
    parser.add_argument('--bad', action='store_true', help='仅展示整数除法带来的错误结果')
    args = parser.parse_args()
    values = [10, 11, 12, 14]
    if args.bad:
        print(f'错误算法结果：{wrong_mean(values)}；预期：11.75')
        return
    bad, fixed = wrong_mean(values), correct_mean(values)
    assert bad == 11 and fixed == 11.75
    try:
        correct_mean([])
    except ValueError as error:
        empty = str(error)
    else:
        raise AssertionError('空列表未被正确处理')
    report = {'input': values, 'wrong_mean': bad, 'correct_mean': fixed, 'empty_input': empty}
    (args.output / 'debug.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
