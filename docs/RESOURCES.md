# 官方资料、参考结构与版本说明

课程为本仓库编写，参考以下原始文档的概念与操作说明；不复制整篇教程。零基础可先读本仓库中文课程，再查对应官方资料。核对日期为 2026-10-05。

| 主题 | 主要原始资料 | 怎么使用 |
| --- | --- | --- |
| Ubuntu 命令行 | [Ubuntu Desktop 官方入门](https://documentation.ubuntu.com/desktop/en/latest/tutorial/the-linux-command-line-for-beginners/) | 已读取；路径、文件、管道与管理员操作概念 |
| Ubuntu 桌面 | [Ubuntu 22.04 帮助](https://help.ubuntu.com/22.04/ubuntu-help/index.html) | 本次页面返回 503；桌面细节以本机设置与实际操作为准 |
| Bash | [Jammy Bash 手册](https://manpages.ubuntu.com/manpages/jammy/en/man1/bash.1.html)、[GNU Bash 手册](https://www.gnu.org/software/bash/manual/bash.html) | Jammy 页面可读；优先本机 man bash，完整 GNU 页面本次读取超时 |
| 权限 | [Jammy chmod 手册](https://manpages.ubuntu.com/manpages/jammy/en/man1/chmod.1.html) | 已访问；结合实际挂载，不只看命令退出状态 |
| 系统包 | [Jammy apt 手册](https://manpages.ubuntu.com/manpages/jammy/en/man8/apt.8.html) | 已访问；apt 与 dpkg 的职责，命令以本机帮助为准 |
| systemd | [Jammy systemctl 手册](https://manpages.ubuntu.com/manpages/jammy/en/man1/systemctl.1.html) | 已读取；服务状态、启动与 enable 的区别 |
| Python | [Python 3.10 教程](https://docs.python.org/3.10/tutorial/)、[venv 文档](https://docs.python.org/3.10/library/venv.html) | 已读取；解释器、语法、模块与虚拟环境 |
| Git | [Pro Git 中文版](https://git-scm.com/book/zh/v2) | 上一轮已读取，本轮直接请求返回 403；本地示例按已安装 Git 实测 |
| VS Code | [Python 环境](https://code.visualstudio.com/docs/python/environments)、[Python 调试](https://code.visualstudio.com/docs/python/debugging) | 环境页已读取；桌面断点需要手动操作 |
| CMake | [CMake 3.22 教程](https://cmake.org/cmake/help/v3.22/guide/tutorial/index.html) | 已访问；用与本机接近的版本，最新页面版本可能不同 |
| tmux | [上游 Getting Started](https://github.com/tmux/tmux/wiki/Getting-Started) | 已读取；会话、窗口、面板与前缀键 |
| Docker | [Ubuntu 安装文档](https://docs.docker.com/engine/install/ubuntu/)、[文档源码](https://github.com/docker/docs/blob/main/content/manuals/engine/install/ubuntu.md) | 网页本次连接重置，官方源码已读取，列有 Jammy 22.04；选修操作前核对当前要求 |

网络可用性和页面更新情况随时间变化；本地验收不依赖这些网页实时可访问。具体命令版本由本机 --help/man 与实验结果支撑。

## 参考结构

- 邻近 cv 仓库：逐课 README、THEORY、练习与输入输出说明。
- 邻近 ROS 仓库：课程集中 course，新增代码集中 scripts，入口明确环境并留下验证证据。

本课程不导入这些仓库的运行依赖，根目录源码布局始终独立。

## 阅读版本差异

在线 Python 3.10 文档的补丁号可比本机 3.10.12 新；CMake 最新文档可能讲 4.x；VS Code 和 Docker 也会更新。课程使用本机已验证的基本命令，涉及新特性或系统安装时先检查自己当前版本，不混用别的发行版命令。
