# H04：退出状态、信号与资源清理

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../03_nul_paths/README.md) · [下一课](../05_cli_contract/README.md)

## 前置知识

[S03](../../../lessons/system/03_process_jobs/README.md)、[P07](../../../programming/07_bash_basics/README.md)、[P06](../../../programming/06_files_errors/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

为任务设计可检查的停止过程，区分请求退出与强制结束。

## 原理与步骤

1. 子进程完成准备后写 ready.json，父进程确认 PID。
2. 父进程发送 SIGTERM，子进程用事件结束循环。
3. finally 保存 stopped.json，父进程 wait 回收。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab signals
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `signals` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

子进程状态为 0，clean_exit=true，且已经回收。这个结果来自程序主动处理 SIGTERM，并非所有程序收到信号都返回 0。

## 变式练习

在自己的新脚本里用 trap 为 EXIT/INT/TERM 登记清理动作；启动后停止，只清理自己创建的临时资源，并保留一条退出日志。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

SIGKILL 无法被捕获。trap 和 finally 不能保证断电后运行；应同时设计可恢复的数据写入方式。

## 自检

1. ready 标记为什么有用？
2. wait 负责什么？

<details>
<summary>完成后查看参考答案</summary>

1. 避免父进程过早停止尚未初始化的任务。
2. 等待结束并回收子进程状态。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
