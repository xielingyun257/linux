# H06：文件锁、原子替换与重复运行

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../05_cli_contract/README.md) · [下一课](../../systems/01_proc_limits/README.md)

## 前置知识

[P08](../../../programming/08_bash_automation/README.md)、[S03](../../../lessons/system/03_process_jobs/README.md)、[C03](../../../lessons/terminal/03_file_operations/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

理解多个进程写同一文件的竞争，以及完整报告如何对读者可见。

## 原理与步骤

1. 两个进程各执行 20 次“读→加一→写”。
2. 对稳定的 counter.lock 使用排他锁，覆盖整段操作。
3. 在同目录写临时文件，再 os.replace 替换计数文件。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab atomic
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `atomic` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

最终计数 40，两个进程均退出，没有残留 counter-*.tmp。锁只约束遵守同一锁协议的写者。

## 变式练习

另建自己的程序，增加第三个进程，预测 60；解释为什么锁住临时文件而不是稳定锁文件可能失效。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

原子替换让读者看到完整文件，但单独使用它仍会丢失并发更新。原子可见性也不等于断电后的持久性。

## 自检

1. 为什么锁覆盖读和写？
2. 临时文件为什么放同一文件系统？

<details>
<summary>完成后查看参考答案</summary>

1. 避免两个写者读到同一旧值。
2. 跨文件系统无法使用相同的原子重命名语义。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
