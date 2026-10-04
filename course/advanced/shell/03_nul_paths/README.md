# H03：find、xargs 与复杂文件名

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../02_sed_awk/README.md) · [下一课](../04_graceful_exit/README.md)

## 前置知识

[C02](../../../lessons/terminal/02_paths_navigation/README.md)、[C05](../../../lessons/terminal/05_search_find/README.md)、[P08](../../../programming/08_bash_automation/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

正确处理空格、中文和以连字符开头的文件名，理解 NUL 分隔。

## 原理与步骤

1. find 选择输入路径，-print0 在路径之间写零字节。
2. xargs -0 按相同分隔约定组合参数。
3. Python 将实际参数列表保存为 JSON，避免用肉眼猜路径数量。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab paths
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `paths` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

至少 3 个完整路径，包括“课程 笔记.txt”和“-option.txt”。若当前文件系统允许换行文件名，还验证第四个；否则记录具体限制。

## 变式练习

给自己的练习目录增加包含多个空格的文件，预测路径数量。比较普通换行分隔与 NUL 分隔；程序参数中的 -- 可用于结束许多工具的选项解析。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

不能解析 ls 输出来可靠遍历文件。Linux 的 Shell 支持某类字符，不代表当前 NTFS 挂载也允许它出现在文件名中。

## 自检

1. 为什么空格不再拆开路径？
2. NUL 可以存在于普通文件名中吗？

<details>
<summary>完成后查看参考答案</summary>

1. 生产和消费两端使用零字节分隔。
2. 不可以，因此适合作无歧义分隔。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
