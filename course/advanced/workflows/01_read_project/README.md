# R01：阅读陌生项目：入口、依赖与数据流

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../../engineering/08_container_build/README.md) · [下一课](../02_reproducibility/README.md)

## 前置知识

[P05](../../../programming/05_modules_objects/README.md)、[P10](../../../programming/10_cmake_debug/README.md)、[T03](../../../tools/03_git_basics/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

从文件证据建立项目地图，避免见到脚本就直接运行。

## 原理与步骤

1. 先读 README，再找构建和依赖声明。
2. 读取 setup.cfg 的 console_scripts 定位 cli:main。
3. 追踪输入、调用、输出与环境，最后选择最小可验证入口。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab reading
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `reading` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

实验列出打包示例文件，明确 pyproject、setup.cfg 与 src/linux_greeting/cli.py 的关系。只读取源码和声明，不触发安装或外部项目任务。

## 变式练习

选自己的 ROS 或 cv 项目，写一页项目地图：正式入口、依赖、输入、输出、环境和验证方式。遇到设备或训练入口先解释作用，不凭名称猜运行条件。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

README 可能过时，应对照实际配置与源码。环境脚本、构建脚本和训练脚本责任不同，不能都当成启动入口。

## 自检

1. 包元数据为何值得先看？
2. 最小运行应该证明什么？

<details>
<summary>完成后查看参考答案</summary>

1. 它声明构建后端、依赖与安装入口。
2. 一个明确输入到预期输出的最短流程可用。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
