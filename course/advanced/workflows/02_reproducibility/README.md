# R02：种子、参数、源码摘要与复现实验

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../01_read_project/README.md) · [下一课](../03_incident_method/README.md)

## 前置知识

[P06](../../../programming/06_files_errors/README.md)、[C08](../../../lessons/terminal/08_archives_links/README.md)、[E03](../../engineering/03_offline_packaging/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

把一次结果组织成可检查的实验包，区分可重跑与可复现。

## 原理与步骤

1. 输入保存 seed=71、count=10，复制自包含源码。
2. 保存环境版本、实际命令和源码/输入/输出摘要。
3. 归档、恢复到新目录，再运行并比较结果字节。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab reproduce
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `reproduce` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

源码与资料摘要相同；同一环境重跑输出逐字节一致。归档包含实验脚本、参数、结果和清单，不包含整个 Python 环境或 GPU 栈。

## 变式练习

另建实验，把种子换成另一个值，验证结果变化；再只改变输出格式，解释内容等价与字节相同的区别。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

固定种子不能单独保证跨版本、跨硬件的随机或数值行为。只保存图表而不保存参数和输入，很难复核。

## 自检

1. 为什么保存源码摘要？
2. 结果一致的结论范围是什么？

<details>
<summary>完成后查看参考答案</summary>

1. 确认实际执行的代码版本。
2. 本课验证的是同环境、同源码、同输入的结果。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
