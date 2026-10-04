"""自包含可复现实验：随机种子和样本数来自输入 JSON。"""
import json
from pathlib import Path
import random
import sys


def run(parameters):
    count = parameters['count']
    if type(count) is not int or count <= 0:
        raise ValueError('count 必须为正整数')
    generator = random.Random(parameters['seed'])
    values = [generator.randint(1, 100) for _ in range(count)]
    return {'values':values, 'mean':sum(values)/len(values)}


if __name__ == '__main__':
    parameters = json.loads(Path(sys.argv[1]).read_text())
    result = run(parameters)
    Path(sys.argv[2]).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
