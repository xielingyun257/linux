# E03 理论：Python 打包、wheel 与安装入口

[回到实验](README.md) · [进阶总览](../../README.md)

## 几个“包”的区别

Python 导入包、pip 分发名与系统 apt 包可以名称不同。本例分发叫 linux-learning-demo，导入包叫 linux_greeting，命令叫 linux-greet。排错要区分正在寻找哪一层。

## 离线可复现边界

构建使用本机已安装后端，禁止下载；允许系统包的 venv 提供 wheel。要复现到另一台电脑，需要记录后端版本及兼容依赖，而不只保存 wheel 文件名。发布到 PyPI 不属于本课实验。

## 本课的输入与结果契约

理解源码目录、构建后端、分发包和安装后命令的关系。

生成一个 wheel，并安装 linux-learning-demo 0.1.0；linux-greet --name Ubuntu 输出“你好，Ubuntu！”。无第三方下载，源码目录不写入打包产物。

## 用变式检验理解

复制为自己的新包，改名称与问候规则；构建、安装到另一新环境，在源码目录以外调用命令，证明运行来自安装包。

先把原理写成可观察的预期，再运行；如果结果不同，保留证据并定位具体步骤。只改变一个条件，才能判断结果为何发生变化。

## 结论的边界

--no-build-isolation 要求所需后端已存在，本机已找到 setuptools/wheel。它不是忽略依赖；现代项目也可用 pyproject 的 project 表声明元数据。

参考[官方资料与本机版本](../../../../docs/ADVANCED_RESOURCES.md)。自动完成的检查与需要手动操作的部分分开记录。
