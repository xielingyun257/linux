"""用于对象、参数化工具和测试课程的领域数据模型。"""
from dataclasses import dataclass
from datetime import datetime
import math


@dataclass(frozen=True)
class Event:
    timestamp: str
    level: str
    component: str
    duration_ms: float

    @classmethod
    def from_row(cls, row):
        try:
            timestamp = row['timestamp']
            datetime.fromisoformat(timestamp)
            level = row['level']
            component = row['component']
            duration = float(row['duration_ms'])
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError('字段缺失、时间或耗时格式错误') from error
        if level not in {'INFO', 'WARN', 'ERROR'}:
            raise ValueError('未知日志级别')
        if not component or not component.strip():
            raise ValueError('组件名为空')
        if not math.isfinite(duration) or duration < 0:
            raise ValueError('耗时必须为非负有限数值')
        return cls(timestamp, level, component, duration)
