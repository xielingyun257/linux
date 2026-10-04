# E04：线程池、Future 与任务汇总

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../03_offline_packaging/README.md) · [下一课](../05_cpp_library_tests/README.md)

## 前置知识

[P03](../../../programming/03_control_flow/README.md)、[P04](../../../programming/04_functions/README.md)、[S03](../../../lessons/system/03_process_jobs/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

将独立工作分派给线程池，区分并发、并行和结果顺序。

## 原理与步骤

1. 为 0～11 的每项执行平方计算。
2. ThreadPoolExecutor 限制工作线程数量。
3. map 按输入顺序返回结果，with 在结束时关闭线程池。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab concurrency
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `concurrency` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

结果等于顺序程序的 [0,1,4,...,121]，所有任务完成。这个小例子只验证执行契约，不证明线程让 CPU 计算更快。

## 变式练习

在自己的新程序里让任务等待不同时间，再比较 map 与 as_completed 的呈现顺序；给一个任务制造异常，观察在哪一步被重新抛出。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

不要在同一个受限线程池任务中互相等待依赖，可能死锁；共享可变数据仍需要同步。

## 自检

1. map 的顺序是什么？
2. cancel 能强制中断已运行函数吗？

<details>
<summary>完成后查看参考答案</summary>

1. 输入顺序。
2. 通常不能，应为运行任务设计合作式停止。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
