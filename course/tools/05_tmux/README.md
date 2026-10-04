# T05：tmux 会话、窗口与面板

[课程总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../04_git_branches/README.md) · [下一课](../06_docker_optional/README.md)

## 学习目标

理解终端窗口与 tmux 会话分离，掌握分离和重新连接。

## 先理解

tmux 服务器维护会话，会话有窗口，窗口有面板。关闭终端客户端不一定结束会话；Ctrl+b 是默认前缀，需要先按前缀，再按动作键。socket 决定连接哪一个 tmux 服务器。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
bash scripts/study.sh demo tmux
# 自己在桌面终端练习：
# tmux new -s linux-study
# Ctrl+b 再按 %：左右分屏；Ctrl+b 再按 "：上下分屏
# Ctrl+b 再按 d：分离
# tmux attach -t linux-study
# 在练习 Shell 输入 exit 结束相应面板
```

## 观察与完成标准

自动演示在独立 socket 上建立 lesson，会话列表可见，最后关闭自己的服务器。手动练习需要自己确认窗口、面板和分离状态。

## 自己动手

一个面板阅读日志，另一个执行命令；分离后重新连接，解释哪些任务仍在运行。只清理自己的练习会话。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

tmux 不保证机器关机后程序继续运行。不要执行不带限定范围的 kill-server 去清理不明会话。

## 自检

1. 分离等于退出 Shell 吗？
2. 独立 socket 的意义？

<details>
<summary>完成后查看参考答案</summary>

1. 不等于，只断开客户端。
2. 分隔服务器与会话范围，避免干扰现有任务。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../docs/RESOURCES.md)。
