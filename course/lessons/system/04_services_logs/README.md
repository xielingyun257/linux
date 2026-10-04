# S04：systemd 服务、启动项与日志

[课程总览](../../../README.md) · [理论补充](THEORY.md) · [上一课](../03_process_jobs/README.md) · [下一课](../05_network_ssh/README.md)

## 学习目标

区分普通进程和受服务管理器管理的服务，查服务状态与日志。

## 先理解

systemd 用 unit 描述服务、定时器等资源。start 是现在启动，enable 是配置未来开机或目标激活时启动；active 与 enabled 描述不同状态。journalctl 查询 systemd 收集的日志。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
systemctl --version
systemctl list-units --type=service --state=running --no-pager
systemctl status cron.service --no-pager
journalctl -u cron.service -n 20 --no-pager
# 用户服务另用 systemctl --user；本节先只读观察
```

## 观察与完成标准

看到正在运行的服务和 cron 状态；服务未安装时可显示 unit not found，日志权限不足或无记录时也应记录。自动检查未执行服务启停。

## 自己动手

选择列表中的一个实际服务，记录 active 状态、是否 enabled 及最近三条日志；不要把示例服务名当成本机必然存在的服务。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

status 的非零状态可能表示服务未运行。journalctl 可因权限或日志保留策略看不到历史；不能据此断言从未发生事件。

## 自检

1. enable 会立刻启动服务吗？
2. --user 与系统服务作用范围一样吗？

<details>
<summary>完成后查看参考答案</summary>

1. 单独 enable 通常不会；enable --now 才兼顾立即启动。
2. 不同，前者管理用户会话的 unit。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../../docs/RESOURCES.md)。
