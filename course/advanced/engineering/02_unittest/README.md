# E02：单元测试、边界输入与失败契约

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../01_models_types/README.md) · [下一课](../03_offline_packaging/README.md)

## 前置知识

[P04](../../../programming/04_functions/README.md)、[P06](../../../programming/06_files_errors/README.md)、[E01](../01_models_types/README.md)、[H05](../../shell/05_cli_contract/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

把手工预期写成独立检查，测试结果与错误分支。

## 原理与步骤

1. unittest discover 查找 test_*.py。
2. 模型测试合法转换、缺失和非法输入。
3. CLI 测试报告、状态 2/3/4 与拒绝覆盖；空记录不能伪装成零错误率。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab tests
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `tests` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

10 个测试通过，非法值包含 nan、inf、负数、未知级别等子样例。测试只使用仓库内临时目录，完成后清理自己的测试输入。

## 变式练习

给自己模型增加一个字段后，先写一个会失败的预期检查，再实现校验使其通过；保存失败和成功两次记录。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

测试应检查用户可见的行为，不只重复实现公式。全部通过只说明已测试场景，不能保证任意输入都正确。

## 自检

1. 为什么要测试空输入？
2. assertRaises 在检查什么？

<details>
<summary>完成后查看参考答案</summary>

1. 防止无数据被当成正常零值。
2. 指定情况会产生预期异常。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
