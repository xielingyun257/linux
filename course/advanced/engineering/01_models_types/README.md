# E01：类、dataclass、类型提示与数据模型

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../../systems/06_incremental_backup/README.md) · [下一课](../02_unittest/README.md)

## 前置知识

[P04](../../../programming/04_functions/README.md)、[P05](../../../programming/05_modules_objects/README.md)、[P06](../../../programming/06_files_errors/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

把校验后的数据组织成对象，区分类型提示与运行时检查。

## 原理与步骤

1. Event 把时间、级别、组件和耗时组织在一起。
2. from_row 是类方法，负责字符串转换与校验。
3. frozen 限制通常的字段赋值，asdict 用于生成结构化输出。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab objects
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `objects` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

耗时字符串 12.5 被转换为浮点数，缺失字段被拒绝。类型提示不会自动检查 CSV，校验来自明确写出的代码。

## 变式练习

新建自己的模型，加一个单位明确的字段；设计正常、缺失、负值与非有限数值样例。说明为何仅写 float 类型提示不够。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

dataclass 自动生成部分方法，不自动验证业务规则。frozen 是浅层的字段限制，内部可变对象仍需单独考虑。

## 自检

1. cls 与普通实例 self 的区别？
2. nan 为什么拒绝？

<details>
<summary>完成后查看参考答案</summary>

1. 类方法收到类，实例方法收到对象。
2. 它不是有限测量值，可能破坏比较和统计。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
