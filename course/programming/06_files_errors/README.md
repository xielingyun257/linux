# P06：文件、CSV、JSON、异常与输入检查

[课程总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../05_modules_objects/README.md) · [下一课](../07_bash_basics/README.md)

## 学习目标

读取结构化数据，区分格式错误、输入错误与程序错误。

## 先理解

with 管理文件打开与关闭，encoding 明确字符编码。CSV 行中的字段通常先是字符串，需要转数值；JSON 保存列表、字典等结构。try/except 只处理预期异常，其他错误保留上下文便于排查。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
bash scripts/study.sh python files
bash scripts/study.sh python errors
# 每条命令打印各自实验目录；打开对应 result.json 比较
# CSV 示例含表头 time_s,value 和三条数值记录
```

## 观察与完成标准

文件课得到 rows=3、mean=20.0。异常课先报告空输入错误，再正常计算 [3,9] 的平均值 6.0，程序没有把错误结果伪装成零。

## 自己动手

给自己的 CSV 增加第四条值 40，预测平均值 25；再尝试非数值字符串，记录报错类型与行号。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

不要用 except: pass 隐藏问题。相对路径依赖当前目录，跨机器路径应由 Path 组合；Windows 与 Linux 路径分隔方式不同。

## 自检

1. CSV 中 "20" 如何用于算术？
2. 空输入返回 0 为什么可能误导？

<details>
<summary>完成后查看参考答案</summary>

1. 显式转换为 int 或 float。
2. 会把“没有数据”混成“测得零”。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../docs/RESOURCES.md)。
