# E08：Dockerfile、Compose 与环境边界（选修）

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../07_git_recovery/README.md) · [下一课](../../workflows/01_read_project/README.md)

## 前置知识

[T06](../../../tools/06_docker_optional/README.md)、[P01](../../../programming/01_python_environment/README.md)、[H05](../../shell/05_cli_contract/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

读懂镜像构建上下文、COPY、启动命令与 Compose 服务配置。

## 原理与步骤

1. Dockerfile 从 Python 镜像复制自己的 app.py。
2. Compose 定义只读、无网络的教学服务。
3. 有 Compose 插件时用 config 解析模型，不启动容器。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab containers
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `containers` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

检查 Dockerfile 入口；插件可用时解析 JSON 模型并验证 read_only。报告明确记录未启动 daemon、未下载或构建镜像、未运行容器。

## 变式练习

在自己确认 Docker 可用后，从模板副本手动 build/run，记录实际镜像 digest 与结果。比较镜像里的文件和绑定挂载后的文件优先关系。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

构建上下文决定 COPY 能读哪些文件；.dockerignore 过滤上下文。镜像标签可更新，不能把标签当作固定内容摘要。

## 自检

1. docker compose config 会启动服务吗？
2. 容器内只读是否限制全部宿主机？

<details>
<summary>完成后查看参考答案</summary>

1. 不会，它解析配置。
2. 不会，它描述该容器的根文件系统。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
