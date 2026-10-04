# N05：systemd unit、用户服务与定时器

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../04_ssh_config/README.md) · [下一课](../06_incremental_backup/README.md)

## 前置知识

[S04](../../../lessons/system/04_services_logs/README.md)、[P07](../../../programming/07_bash_basics/README.md)、[H05](../../shell/05_cli_contract/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

读懂 oneshot 服务与 calendar 定时器，并在启用前检查语法。

## 原理与步骤

1. service 描述命令，timer 描述何时触发相应 unit。
2. systemd-analyze verify 检查文件，calendar 解析 hourly。
3. ExecStart 不是默认交给 Shell 的字符串，管道需显式解释器。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab systemd
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `systemd` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

两个 unit 静态验证通过，hourly 显示未来两次时间。实验仅在仓库内生成文件，没有安装、启用或启动系统或用户服务。

## 变式练习

修改自己的 timer 副本为每天 20:00，用 systemd-analyze calendar 预测下次时间；解释时区与 Persistent 的意义。真实部署作为后续手动练习。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

enable 与 start 不同；用户服务还取决于用户会话生命周期。Persistent 主要服务于日历触发的补执行，不代表每一次遗漏都补跑。

## 自检

1. timer 与 service 分工是什么？
2. verify 通过代表任务真的跑过吗？

<details>
<summary>完成后查看参考答案</summary>

1. 定义触发时间与定义执行动作。
2. 不代表，还需启用、执行和日志证据。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
