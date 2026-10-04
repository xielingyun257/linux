"""六节 Python 课程中的五个示例；每个例子解释输入与结果。"""
import argparse
import json
from pathlib import Path


def mean(values):
    if not values:
        raise ValueError('至少需要一个数值')
    return sum(values) / len(values)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('topic', choices=('variables', 'flow', 'functions', 'files', 'errors'))
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    if args.topic == 'variables':
        distance = 150
        speed = 60.0
        samples = [10, 20, 30]
        record = {'distance_mm': distance, 'speed_mm_s': speed, 'time_s': distance / speed,
                  'samples': samples, 'name': '实验 A'}
        assert record['time_s'] == 2.5 and samples[0] == 10
        print('类型：', type(distance).__name__, type(speed).__name__, type(samples).__name__)
    elif args.topic == 'flow':
        values = [2, 5, 8, 11]
        selected = []
        for value in values:
            if value >= 6:
                selected.append(value)
        record = {'values': values, 'selected': selected, 'sum': sum(selected)}
        assert selected == [8, 11] and record['sum'] == 19
    elif args.topic == 'functions':
        result = mean([10, 20, 30])
        record = {'function': 'mean', 'input': [10, 20, 30], 'result': result}
        assert result == 20.0
    elif args.topic == 'files':
        source = args.output / 'measurements.csv'
        source.write_text('time_s,value\n0,10\n1,20\n2,30\n', encoding='utf-8')
        import csv
        with source.open(encoding='utf-8', newline='') as stream:
            rows = list(csv.DictReader(stream))
        values = [float(row['value']) for row in rows]
        record = {'rows': len(rows), 'mean': mean(values), 'input': source.name}
        assert record['rows'] == 3 and record['mean'] == 20.0
    else:
        messages = []
        for values in ([], [3, 9]):
            try:
                result = mean(values)
                messages.append(f'平均值：{result}')
            except ValueError as error:
                messages.append(f'输入错误：{error}')
        record = {'messages': messages}
        assert messages == ['输入错误：至少需要一个数值', '平均值：6.0']
    payload = json.dumps(record, ensure_ascii=False, indent=2) + '\n'
    (args.output / 'result.json').write_text(payload, encoding='utf-8')
    print(payload, end='')


if __name__ == '__main__':
    main()
