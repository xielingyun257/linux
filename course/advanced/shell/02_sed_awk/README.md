# H02：sed、awk 与结构化文本

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../01_quoting/README.md) · [下一课](../03_nul_paths/README.md)

## 前置知识

[C04](../../../lessons/terminal/04_read_text/README.md)、[C05](../../../lessons/terminal/05_search_find/README.md)、[C06](../../../lessons/terminal/06_pipes_redirection/README.md)、[P03](../../../programming/03_control_flow/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

按行选择、替换和聚合文本，判断什么时候应改用 CSV 解析器。

## 原理与步骤

1. sed 的 s/模式/替换/ 改变输出文本，本实验不使用 -i。
2. awk -F, 用逗号分字段；NR>1 跳过表头。
3. 累加第二字段，最后用总和除以合法记录数。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab text
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `text` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

三条值 10、20、30 的均值为 20；sed 输出 beta,20，原文件仍是 b,20。不要把过滤后输出与原输入混淆。

## 变式练习

增加一条 d,40，预测均值 25。再加入空值，讨论它是否应计入分母；自己写明处理规则，不默认把所有坏值当零。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

简单 -F, 不能完整处理带引号且字段内部有逗号的 CSV；多列真实数据优先用 csv 模块。

## 自检

1. NR>1 为什么放在这里？
2. sed 默认会改原文件吗？

<details>
<summary>完成后查看参考答案</summary>

1. 跳过表头，避免把列名参与算术。
2. 不会，默认写标准输出。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
