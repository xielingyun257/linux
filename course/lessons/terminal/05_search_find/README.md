# C05：查文件与查内容：find、grep、rg

[课程总览](../../../README.md) · [理论补充](THEORY.md) · [上一课](../04_read_text/README.md) · [下一课](../06_pipes_redirection/README.md)

## 学习目标

区分按名称找文件与在文件中搜索文字。

## 先理解

find 遍历目录并按条件选择路径；grep 搜索文本行；rg 是可选的快速文本搜索工具。Shell 通配符和正则表达式是两套语法：*.md 选文件名，^ERROR 匹配行首文字。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
find course -type f -name '*.md'
grep -n 'def main' scripts/lab.py
grep -R -n '平均值' scripts/programming/python --include='*.py'
command -v rg
# 已安装 rg 时可试：
# rg -n '平均值' scripts/programming/python
```

## 观察与完成标准

find 返回 Markdown 路径，grep -n 返回行号和匹配行。没有安装 rg 时仍可用 grep 与 find 完成本课。

## 自己动手

找到全部 C++ 源文件；查出哪些 Python 文件包含 raise ValueError，解释两个任务为何使用不同工具。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

find 的 *.md 应加引号，否则可能先被当前 Shell 展开。grep 搜不到时状态为 1，这不必然是运行错误。

## 自检

1. -type f 排除了什么？
2. ^ERROR 与 ERROR 匹配范围相同吗？

<details>
<summary>完成后查看参考答案</summary>

1. 目录等非普通文件。
2. 不同，前者要求出现在行首。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../../docs/RESOURCES.md)。
