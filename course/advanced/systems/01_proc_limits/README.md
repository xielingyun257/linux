# N01：/proc、资源上限与观察范围

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../../shell/06_lock_atomic/README.md) · [下一课](../02_performance_strace/README.md)

## 前置知识

[S03](../../../lessons/system/03_process_jobs/README.md)、[S06](../../../lessons/system/06_storage_mounts/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

用只读证据区分 CPU、内存、文件描述符和资源上限。

## 原理与步骤

1. /proc/self 指读取者自己，不是整个系统。
2. status 中 Threads、VmRSS 反映不同资源。
3. resource.getrlimit 返回软/硬上限；本课只读，不修改限制。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab proc
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `proc` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

报告保存本次 PID、线程数、驻留内存和文件描述符上限。具体数值随运行变化，不要求与课本或别人电脑一致。

## 变式练习

结合 ps、free、df 和本报告，各选一项解释统计对象与单位。另开终端读 /proc/self/status，说明它为什么可能不是 Python 进程。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

VSZ 不等于实际驻留内存。/proc 中信息会随进程变化或消失；已退出的 PID 可能被复用。

## 自检

1. /proc/self 中的 self 指谁？
2. 软上限和当前占用是一回事吗？

<details>
<summary>完成后查看参考答案</summary>

1. 当前读取该路径的进程。
2. 不是，上限是可使用边界，占用是当前量。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
