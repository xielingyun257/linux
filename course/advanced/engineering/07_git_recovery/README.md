# E07：Git 冲突、abort 与 bisect

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../06_debug_sanitizer/README.md) · [下一课](../08_container_build/README.md)

## 前置知识

[T03](../../../tools/03_git_basics/README.md)、[T04](../../../tools/04_git_branches/README.md)、[E02](../02_unittest/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

在可丢弃示例仓库中练习真正的冲突和回归定位。

## 原理与步骤

1. 两个分支修改同一行，merge 产生未合并状态。
2. 先 merge --abort 确认恢复，再重新合并并保留双方意图。
3. 另一示例仓库用 bisect run 查出首个坏提交，最后 reset 结束二分状态。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab git
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `git` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

冲突出现并恢复，解决后状态干净；五个演示版本中第 3 版（从 0 开始）是首个坏版本。全部在独立仓库，不改课程主分支。

## 变式练习

在自己的示例分支设计另一冲突，先记录共同祖先与两边意图再解决；给 bisect 的探针制造不稳定结果，解释它为何会误导二分。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

bisect 需要可重复的好/坏判断，状态 125 可跳过无法测试的提交。不要靠强推或硬重置处理未理解的历史。

## 自检

1. abort 会完成合并吗？
2. 二分为什么比逐个提交试快？

<details>
<summary>完成后查看参考答案</summary>

1. 不会，它终止当前合并并尝试恢复之前状态。
2. 每次缩小区间，所需检查次数通常对数增长。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
