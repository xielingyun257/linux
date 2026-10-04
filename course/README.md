# 课程总览与学习路线

面向零基础，主环境为 Ubuntu 22.04。共 36 节，T06 Docker 为选修。课程与运行示例各自独立，不需要加载 ROS 或 cv 的环境。

从 U01 开始，依次完成 Ubuntu、终端、系统管理、编程与工具课。开始写程序时可提前学习 T01/T02；需要记录自己的版本时穿插 T03/T04。

每节按“理解→预测→运行→观察→改一个条件→解释→自检”学习。自动命令从仓库根目录运行；运行前查看本课目标，不必一口气执行全部代码。

| 顺序 | 课程 |
| --- | --- |
| U01 | [Linux、Ubuntu 与电脑里的几层软件](lessons/ubuntu_basics/01_linux_ubuntu/README.md) |
| U02 | [桌面、窗口与快捷键](lessons/ubuntu_basics/02_desktop_windows/README.md) |
| U03 | [文件管理器、目录与隐藏文件](lessons/ubuntu_basics/03_file_manager/README.md) |
| U04 | [中文输入、复制粘贴与终端快捷键](lessons/ubuntu_basics/04_input_clipboard/README.md) |
| U05 | [系统设置、设备与软件入口](lessons/ubuntu_basics/05_settings_devices/README.md) |
| U06 | [截图、求助与记录一次操作](lessons/ubuntu_basics/06_screenshots_learning/README.md) |
| C01 | [终端、Shell 与一条命令的结构](lessons/terminal/01_shell_commands/README.md) |
| C02 | [绝对路径、相对路径与目录导航](lessons/terminal/02_paths_navigation/README.md) |
| C03 | [创建、复制、移动与删除练习文件](lessons/terminal/03_file_operations/README.md) |
| C04 | [查看文本、日志与文件类型](lessons/terminal/04_read_text/README.md) |
| C05 | [查文件与查内容：find、grep、rg](lessons/terminal/05_search_find/README.md) |
| C06 | [管道、标准输出与错误输出](lessons/terminal/06_pipes_redirection/README.md) |
| C07 | [环境变量、PATH 与启动配置](lessons/terminal/07_environment_paths/README.md) |
| C08 | [压缩归档、校验与软链接](lessons/terminal/08_archives_links/README.md) |
| S01 | [用户、组、权限与 sudo](lessons/system/01_users_permissions/README.md) |
| S02 | [apt、dpkg、Snap 与软件安装](lessons/system/02_packages_software/README.md) |
| S03 | [进程、前后台与任务结束](lessons/system/03_process_jobs/README.md) |
| S04 | [systemd 服务、启动项与日志](lessons/system/04_services_logs/README.md) |
| S05 | [IP、端口、HTTP、SSH 与文件传输](lessons/system/05_network_ssh/README.md) |
| S06 | [磁盘空间、挂载与备份排错](lessons/system/06_storage_mounts/README.md) |
| P01 | [Python、解释器、venv 与 Miniforge](programming/01_python_environment/README.md) |
| P02 | [变量、类型、单位与容器](programming/02_variables_containers/README.md) |
| P03 | [条件、循环与算法步骤](programming/03_control_flow/README.md) |
| P04 | [函数、参数、返回值与作用域](programming/04_functions/README.md) |
| P05 | [模块、import 与对象的入口](programming/05_modules_objects/README.md) |
| P06 | [文件、CSV、JSON、异常与输入检查](programming/06_files_errors/README.md) |
| P07 | [Bash 脚本、变量、参数与条件](programming/07_bash_basics/README.md) |
| P08 | [遍历文件、批处理与稳健路径](programming/08_bash_automation/README.md) |
| P09 | [C++ 源码、编译、链接与可执行文件](programming/09_cpp_compilation/README.md) |
| P10 | [CMake、构建目录与调试信息](programming/10_cmake_debug/README.md) |
| T01 | [nano、Vim 与文本编辑模式](tools/01_editors/README.md) |
| T02 | [VS Code 工作区、解释器与断点](tools/02_vscode_debug/README.md) |
| T03 | [Git 工作区、暂存区与提交](tools/03_git_basics/README.md) |
| T04 | [Git 分支、合并与同步](tools/04_git_branches/README.md) |
| T05 | [tmux 会话、窗口与面板](tools/05_tmux/README.md) |
| T06 | [Docker 镜像、容器与挂载（选修）](tools/06_docker_optional/README.md) |

## 综合练习

- [资料整理与备份](../projects/organize/README.md)：C03/C08、S06、P06 之后。
- [日志分析](../projects/logs/README.md)：C05/C06、P03/P06 之后。
- [平均值程序调试](../projects/debug/README.md)：P04/P06、T02 之后。

## 节奏与完成标准

建议每次 30～60 分钟学一节，分两次完成较长实验；可用 8～12 周推进，不设强制周作业。第一轮掌握日常与终端，再学系统排错和 Python，最后串联工具与项目。

一节完成意味着：能解释命令或代码的输入与输出；能独立重做核心步骤；改一个条件后能预测变化；能回答自检并保存自己的记录。一次命令成功不能代替理解。

## 学习辅助

- [术语表](GLOSSARY.md)
- [命令速查](CHEATSHEET.md)
- [练习记录模板](../scripts/templates/study_record.md)
- [运行指南](../scripts/README.md)
- [故障处理](../docs/TROUBLESHOOTING.md)
- [验证范围](../docs/VALIDATION.md)
