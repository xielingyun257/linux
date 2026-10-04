# N02：性能测量、复杂度与 strace

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../01_proc_limits/README.md) · [下一课](../03_http_diagnosis/README.md)

## 前置知识

[P03](../../../programming/03_control_flow/README.md)、[S03](../../../lessons/system/03_process_jobs/README.md)、[C04](../../../lessons/terminal/04_read_text/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

在正确结果的基础上测量，区分算法耗时与系统调用观察。

## 原理与步骤

1. 对同一输入比较重复扫描和预先计数，两者结果应一致。
2. perf_counter 记录三次时长，保存原值而不只说“更快”。
3. strace -c 汇总自己的短进程系统调用，输出留在实验目录。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab timing
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `timing` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

两种算法结果相同，报告列三次耗时；strace 若可用生成汇总，否则保留原因。速度比随机器与负载变化，课程不规定固定倍率。

## 变式练习

另建程序，把输入量扩大两倍再测；解释线性和平方增长的预期。先验证数值相同，再比较时间，避免用错误算法换速度。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

一次测量会受调度、缓存与初始化影响。strace 会扰动程序，它不等于没有开销的性能基准。

## 自检

1. 比较速度之前先检查什么？
2. strace 主要看哪一层？

<details>
<summary>完成后查看参考答案</summary>

1. 输入与计算结果一致。
2. 程序与内核之间的系统调用。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
