# Ubuntu 与 Linux 学习仓库

面向零基础，从 Ubuntu 日常操作学到终端、系统管理、编程和开发工具。主环境是本机 **Ubuntu 22.04.5 + 系统 Python 3.10**；不要求升级系统。课程采用 cv 的逐课练习方式与 ROS 的课程、代码分离方式，运行时不依赖这两个仓库。

## 从哪里开始

1. 打开[课程总览](course/README.md)，从 [U01：认识 Linux 与 Ubuntu](course/lessons/ubuntu_basics/01_linux_ubuntu/README.md)开始。
2. 每课先理解、预测，再操作；对照预期结果，做一个变式练习并回答自检。
3. 写程序前学 [P01：Python 环境](course/programming/01_python_environment/README.md)，按需提前学 [VS Code 调试](course/tools/02_vscode_debug/README.md)。
4. 遇到概念查[术语表](course/GLOSSARY.md)，需要命令查[速查表](course/CHEATSHEET.md)，报错查[故障指南](docs/TROUBLESHOOTING.md)。

## 课程地图

| 模块 | 内容 | 节数 |
| --- | --- | --- |
| [Ubuntu 日常操作](course/lessons/ubuntu_basics/README.md) | 桌面、文件管理、输入、设备设置、截图与记录 | 6 |
| [终端与命令行](course/lessons/terminal/README.md) | 命令结构、路径、文件、文本、搜索、管道、环境、归档 | 8 |
| [系统管理基础](course/lessons/system/README.md) | 权限、软件包、进程、服务、网络、磁盘 | 6 |
| [编程基础](course/programming/README.md) | Python、Bash 自动化、C++ 与 CMake | 10 |
| [Linux 配套工具](course/tools/README.md) | 编辑器、VS Code、Git、tmux、Docker 选修 | 6 |

共 **36 节**，每节有操作页、理论页、练习、常见错误和自检答案。建议每次 30～60 分钟，按自己的进度推进；不设强制周作业。

## 先运行一个小实验

在 Ubuntu 终端中进入仓库：

```bash
cd /media/wdros/DataE/learning/Linux
bash scripts/study.sh environment
bash scripts/study.sh demo files
bash scripts/study.sh python variables
```

每次运行打印自己的实验目录，结果保存在 `scripts/runs/` 下，不覆盖上次输出。入口固定使用 `/usr/bin/python3`，本机默认 `python3` 指向 Miniforge，两者差异会在课程中解释。

完整运行说明见 [scripts/README.md](scripts/README.md)。课程建设时已跑通[热身与验收](docs/VALIDATION.md)，桌面、远端和管理员步骤按验证记录区分。

## 综合项目

| 项目 | 要学会什么 | 入口 |
| --- | --- | --- |
| [资料整理与备份](projects/organize/README.md) | 分类、保留原件、归档、恢复校验 | `bash scripts/study.sh project organize` |
| [日志分析](projects/logs/README.md) | 解析记录、计数、报告异常格式 | `bash scripts/study.sh project logs` |
| [平均值程序调试](projects/debug/README.md) | 复现错误、断点观察、检查修复 | `bash scripts/study.sh project debug` |

## 仓库结构

```text
Linux/
├── README.md                     总入口
├── AGENTS.md                     后续协作约定
├── course/
│   ├── README.md                 36 节课程与学习顺序
│   ├── GLOSSARY.md               中英文术语
│   ├── CHEATSHEET.md             命令速查
│   ├── lessons/
│   │   ├── ubuntu_basics/        U01～U06
│   │   ├── terminal/             C01～C08
│   │   └── system/               S01～S06
│   ├── programming/             P01～P10
│   └── tools/                   T01～T06
├── projects/                    项目说明、思路、练习与完成标准
├── docs/                        环境、来源、故障与实测范围
└── scripts/                     所有可执行代码与教学资产
    ├── study.sh / lab.py         运行与验收入口
    ├── warmup.sh                 最小全流程
    ├── programming/             Python、Bash、C++ 源码
    ├── projects/                三个综合项目源码
    ├── editor/                  可选 VS Code 工作区
    ├── templates/               学习记录模板
    ├── assets/                  课程清单
    ├── exercises/               可提交的个人练习（需要时新建）
    ├── practice/                草稿练习，不提交
    ├── runtime/                 环境、临时文件，不提交
    ├── runs/                    自动实验与日志，不提交
    └── memory → ~/.Codex/memory  本机全局记忆链接，不提交
```

新增源码全部放根目录 `scripts/`，课程文档放 `course/`，项目文档放 `projects/`。自动实验使用自己生成的少量数据；真实资料的整理、远程连接和系统设置由学习者在相应课程中手动练习。

## 本机与资料

当前环境与依赖路径见[环境说明](docs/ENVIRONMENT.md)，官方资料与版本差异见[资源说明](docs/RESOURCES.md)。仓库所在文件系统是 `ntfs3`，权限与链接行为以实验报告为准。

远端为 [xielingyun257/linux](https://github.com/xielingyun257/linux)。运行结果与环境目录被忽略；提交自己的学习代码前先检查差异，提交信息使用中文。
