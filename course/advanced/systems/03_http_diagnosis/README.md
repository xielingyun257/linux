# N03：HTTP 状态、curl 与分层网络排错

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../02_performance_strace/README.md) · [下一课](../04_ssh_config/README.md)

## 前置知识

[S05](../../../lessons/system/05_network_ssh/README.md)、[C06](../../../lessons/terminal/06_pipes_redirection/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

区分连接故障、HTTP 返回失败和应用数据错误。

## 原理与步骤

1. 本机临时服务提供 /health、/missing、/protected。
2. curl -f 把 HTTP 400 及以上响应作为失败。
3. 同时看状态、正文和退出值，结束时关闭服务器。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab http
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `http` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

/health 返回 200 且正文正确；404 和 401 在 curl -f 下返回 22。全部监听 127.0.0.1，测试后线程关闭，不证明外网可达。

## 变式练习

在自己的新服务器中加 /slow 路由，用 curl --max-time 设置等待上限。把超时、401、404 分别写成不同诊断，不把它们都称为网络断了。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

未用 -f 时，curl 能成功收到 404 响应并返回 0；HTTP 状态与命令状态不能简单等同。

## 自检

1. 401 通常属于哪层问题？
2. HTTP 200 足以验证内容吗？

<details>
<summary>完成后查看参考答案</summary>

1. 协议上的认证要求，连接已经建立。
2. 不够，还需内容与业务规则检查。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
