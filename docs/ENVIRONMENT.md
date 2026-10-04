# 本机环境与依赖路径

核对日期：2026-10-05（Asia/Shanghai）。系统报告与运行路径保存在每次 environment 实验目录，环境发生变化后重新运行，不把这里的版本当成永远固定。

```bash
bash scripts/study.sh environment
```

| 对象 | 已核对值 |
| --- | --- |
| 操作系统 | Ubuntu 22.04.5 LTS，Jammy |
| 仓库 | /media/wdros/DataE/learning/Linux |
| 挂载 | /media/wdros/DataE，ntfs3 |
| 课程解释器 | /usr/bin/python3，3.10.12 |
| 默认 python3 | /home/wdros/miniforge3/bin/python3 |
| Bash | /usr/bin/bash，5.1.16 |
| Git | /usr/bin/git，2.34.1 |
| C++ 编译器 | /usr/bin/g++，11.4.0 |
| CMake | /usr/bin/cmake，3.22.1 |
| tmux | /usr/bin/tmux，3.2a |
| Docker 客户端 | /usr/bin/docker，29.8.1；不代表 daemon 已验证 |
| 其他已找到工具 | gdb、make、nano、vim、code、curl、wget、ssh、rsync、tar、unzip |

## 课程如何选环境

study.sh 固定系统解释器并使用 -I，不读取 PYTHONPATH 或用户 site-packages。子命令使用系统工具 PATH，清理 Python/Conda 路径变量，只影响自己的子进程。模块课使用 -E -s，让同目录模块可以正常导入。

Python 标准库已经足够完成主线。可选 venv 通过系统 Python 加 --system-site-packages 创建在 scripts/runtime/，允许系统包可见；新安装 pip 包时明确使用该 venv 的 python -m pip。

不更改用户全局 PATH，不替换系统 Python 链接，不借用 ROS overlay、cv 环境或训练环境。ROS 项目仍通过它自己的入口运行。

## 文件系统与运行产物

NTFS 的权限、链接与文件名行为受驱动和挂载选项影响。权限演示会同时记录请求的模式与实际 stat 结果；2026-10-05 此挂载实测 chmod 600 后 stat 为 0600。这个观察只对应当前挂载，不推广到所有 NTFS 配置。

自动实验创建 scripts/runs/ 唯一目录，热身与 venv 放 scripts/runtime/。编译子进程的 TMPDIR 指向仓库内，Git 忽略这些产物。热身已验证创建 venv、C++ 编译执行和归档读取。

图形桌面操作、远端 SSH、管理员安装与 Docker daemon 不属于 environment 检查。具体已验证范围见[验证记录](VALIDATION.md)。
