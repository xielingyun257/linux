# H05：参数化命令行工具与机器可读报告

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../04_graceful_exit/README.md) · [下一课](../06_lock_atomic/README.md)

## 前置知识

[P04](../../../programming/04_functions/README.md)、[P05](../../../programming/05_modules_objects/README.md)、[P06](../../../programming/06_files_errors/README.md)、[C06](../../../lessons/terminal/06_pipes_redirection/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

将一次性脚本改成有明确参数、输入检查、报告格式和退出状态的工具。

## 原理与步骤

1. argparse 明确 --input、--output、--strict 与阈值。
2. CSV 用 Event 模型逐行校验，坏记录另列。
3. 报告落盘后，用状态 3 表达严格格式检查失败，4 表达错误率超限；路径或覆盖问题是 2。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab cli
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `cli` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

合法 8 条，错误率 3/8=0.375，平均耗时 45 ms，坏记录 1 条。四种运行验证正常、格式问题、阈值超限与拒绝覆盖；已有报告字节不变。

## 变式练习

查看 log_cli.py 的 --help。复制为自己的工具，增加一个筛选组件参数；明确错误率分母是在筛选前还是筛选后，并设计输入。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

非零状态也可能是预期的巡检结论，报告仍会生成。不要把“没有记录”当错误率 0；本工具返回 null，并以状态 5 表达无合法数据。

## 自检

1. --strict 的失败状态是什么？
2. 已有输出为什么拒绝覆盖？

<details>
<summary>完成后查看参考答案</summary>

1. 3。
2. 保留可审查的既有结果，调用者需指定新文件。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
