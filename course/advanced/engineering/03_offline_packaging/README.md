# E03：Python 打包、wheel 与安装入口

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../02_unittest/README.md) · [下一课](../04_concurrency/README.md)

## 前置知识

[P01](../../../programming/01_python_environment/README.md)、[P05](../../../programming/05_modules_objects/README.md)、[H05](../../shell/05_cli_contract/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

理解源码目录、构建后端、分发包和安装后命令的关系。

## 原理与步骤

1. pyproject.toml 声明 setuptools 构建后端；本例用 setup.cfg 兼容本机工具版本。
2. 复制源码到本次目录，离线构建 wheel。
3. 在本次 venv 安装 wheel，再调用 linux-greet 验证入口。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab packaging
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `packaging` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

生成一个 wheel，并安装 linux-learning-demo 0.1.0；linux-greet --name Ubuntu 输出“你好，Ubuntu！”。无第三方下载，源码目录不写入打包产物。

## 变式练习

复制为自己的新包，改名称与问候规则；构建、安装到另一新环境，在源码目录以外调用命令，证明运行来自安装包。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

--no-build-isolation 要求所需后端已存在，本机已找到 setuptools/wheel。它不是忽略依赖；现代项目也可用 pyproject 的 project 表声明元数据。

## 自检

1. wheel 与源码文件夹相同吗？
2. console_scripts 指向哪里？

<details>
<summary>完成后查看参考答案</summary>

1. 不同，它是可安装分发物。
2. 指向包内某个可调用入口，如 cli:main。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
