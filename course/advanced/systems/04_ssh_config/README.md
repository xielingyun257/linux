# N04：SSH 配置、密钥与端口转发

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../03_http_diagnosis/README.md) · [下一课](../05_user_timers/README.md)

## 前置知识

[S05](../../../lessons/system/05_network_ssh/README.md)、[C07](../../../lessons/terminal/07_environment_paths/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

用独立配置文件表达连接参数，理解本地端口转发的实际位置。

## 原理与步骤

1. Host 是别名，HostName 是目标地址，Port 是目标 SSH 端口。
2. ssh -G -F 配置 别名 展示解析后的参数，不发起连接。
3. LocalForward 的本地监听端与远端连接目标分别写明。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab ssh-config
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `ssh-config` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

解析结果使用 127.0.0.1、端口 2222 和示例用户 student。配置放本次实验目录；未创建密钥、修改全局配置或登录服务器。

## 变式练习

给自己的配置副本增加另一个别名，用 -G 比较结果。拥有服务器后再练习 ssh -p 与 scp -P；记录主机指纹与实际连接路径。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

隧道里的远端 127.0.0.1 指远程机器。私钥不能作为课程素材提交，公钥与私钥用途不同。

## 自检

1. -G 会验证远端密码吗？
2. 本地 9000 端口与 SSH 2222 端口是同一个吗？

<details>
<summary>完成后查看参考答案</summary>

1. 不会，只计算配置。
2. 不是，分别是隧道监听与 SSH 连接端口。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
