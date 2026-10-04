# R04：综合实战：日志巡检、阈值与归档

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../03_incident_method/README.md)

## 前置知识

[H05](../../shell/05_cli_contract/README.md)、[H06](../../shell/06_lock_atomic/README.md)、[E02](../../engineering/02_unittest/README.md)、[R02](../02_reproducibility/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

串联参数化工具、结构化报告、巡检结论与结果留存。

## 原理与步骤

1. 自动生成 8 条合法与 1 条坏格式记录。
2. 用两个阈值运行巡检，保存各自报告与退出状态。
3. 将输入和报告归档，读取归档内容验证一致。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab capstone
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `capstone` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

错误率 0.375；阈值 0.5 时通过，0.2 时超限。inspection.tar.gz 中报告字节与原报告一致；坏记录仍在报告中。

## 变式练习

在自己的新项目中加组件筛选、耗时阈值或文本摘要三者之一；为新行为写测试，再创建一次可恢复的结果包和说明。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

不应为了让巡检绿灯而丢弃坏记录。调度、报告和归档分属不同环节，失败时应指出具体阶段与保留的文件。

## 自检

1. 严格格式检查与错误率检查可以互相替代吗？
2. 综合项目什么时候算完成？

<details>
<summary>完成后查看参考答案</summary>

1. 不能，检查不同问题。
2. 输入明确、结果正确、失败分支可解释、归档可读且变式通过。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
