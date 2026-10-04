"""使用同目录模块；入口以 -E -s 启动，保留正常的脚本目录搜索。"""
import json
import math
from pathlib import Path
import sys
from converter import degrees_to_radians


if __name__ == '__main__':
    result = degrees_to_radians(30)
    assert math.isclose(result, math.pi / 6)
    report = {'degrees': 30, 'radians': result, 'module': 'converter.py'}
    (Path(sys.argv[1]) / 'result.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(f'30 度 = {result:.6f} 弧度')
