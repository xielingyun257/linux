# N06：rsync、增量快照与恢复

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../05_user_timers/README.md) · [下一课](../../engineering/01_models_types/README.md)

## 前置知识

[C08](../../../lessons/terminal/08_archives_links/README.md)、[S06](../../../lessons/system/06_storage_mounts/README.md)、[H06](../../shell/06_lock_atomic/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

保留多个资料版本，理解 --link-dest、校验比较与硬链接约束。

## 原理与步骤

1. 先复制版本 1 的文件形成 snapshot1。
2. 修改源内容并增加文件，用 --checksum 和 --link-dest 生成 snapshot2。
3. 检查旧内容仍在，再观察未变文件的 inode 是否共享。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab backup
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `backup` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

snapshot1 保留 version 1，snapshot2 保存 version 2 和新文件。报告记录 unchanged_hardlink 的实际值，不凭文件名断定硬链接已生效。

## 变式练习

从第一份快照恢复到新的目录并核对内容。解释为什么不能直接修改快照中共享硬链接的文件；设计保留周期，先只列候选，不自动删除。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

大小和时间相同不保证内容相同，本实验专门用 --checksum。共享 inode 的快照不是独立介质备份，也不能被原地编辑。

## 自检

1. 源目录末尾 / 表示什么？
2. --link-dest 为什么节省空间？

<details>
<summary>完成后查看参考答案</summary>

1. 复制目录内容。
2. 条件满足时对未变文件使用硬链接，而非重写完整数据。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
