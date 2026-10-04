# 完整课程总览：基础 36 + 进阶 24

共 **60 节**，主环境 Ubuntu 22.04。基础与进阶都有操作、理论、变式和自检；容器实操与真实远程操作按依赖选择。

先看[从哪里开始](START_HERE.md)选择路线；想解决当前问题查[场景索引](SCENARIOS.md)，想验证独立能力做[阶段任务](MILESTONES.md)。

## 基础课程（36 节）

| 编号 | 课程 |
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

## 进阶课程（24 节）

[系列导览](advanced/README.md)。需要哪一课可按其前置知识进入，不要求先逐页读完。

| 编号 | 课程 |
| --- | --- |
| H01 | [引号、展开与参数边界](advanced/shell/01_quoting/README.md) |
| H02 | [sed、awk 与结构化文本](advanced/shell/02_sed_awk/README.md) |
| H03 | [find、xargs 与复杂文件名](advanced/shell/03_nul_paths/README.md) |
| H04 | [退出状态、信号与资源清理](advanced/shell/04_graceful_exit/README.md) |
| H05 | [参数化命令行工具与机器可读报告](advanced/shell/05_cli_contract/README.md) |
| H06 | [文件锁、原子替换与重复运行](advanced/shell/06_lock_atomic/README.md) |
| N01 | [/proc、资源上限与观察范围](advanced/systems/01_proc_limits/README.md) |
| N02 | [性能测量、复杂度与 strace](advanced/systems/02_performance_strace/README.md) |
| N03 | [HTTP 状态、curl 与分层网络排错](advanced/systems/03_http_diagnosis/README.md) |
| N04 | [SSH 配置、密钥与端口转发](advanced/systems/04_ssh_config/README.md) |
| N05 | [systemd unit、用户服务与定时器](advanced/systems/05_user_timers/README.md) |
| N06 | [rsync、增量快照与恢复](advanced/systems/06_incremental_backup/README.md) |
| E01 | [类、dataclass、类型提示与数据模型](advanced/engineering/01_models_types/README.md) |
| E02 | [单元测试、边界输入与失败契约](advanced/engineering/02_unittest/README.md) |
| E03 | [Python 打包、wheel 与安装入口](advanced/engineering/03_offline_packaging/README.md) |
| E04 | [线程池、Future 与任务汇总](advanced/engineering/04_concurrency/README.md) |
| E05 | [C++ 库目标、接口与 CTest](advanced/engineering/05_cpp_library_tests/README.md) |
| E06 | [gdb、调用栈与 AddressSanitizer](advanced/engineering/06_debug_sanitizer/README.md) |
| E07 | [Git 冲突、abort 与 bisect](advanced/engineering/07_git_recovery/README.md) |
| E08 | [Dockerfile、Compose 与环境边界（选修）](advanced/engineering/08_container_build/README.md) |
| R01 | [阅读陌生项目：入口、依赖与数据流](advanced/workflows/01_read_project/README.md) |
| R02 | [种子、参数、源码摘要与复现实验](advanced/workflows/02_reproducibility/README.md) |
| R03 | [故障排查：证据、假设与最小改动](advanced/workflows/03_incident_method/README.md) |
| R04 | [综合实战：日志巡检、阈值与归档](advanced/workflows/04_capstone/README.md) |

## 项目与辅助资料

- [六个综合项目](../projects/README.md)
- [术语表](GLOSSARY.md)与[命令速查](CHEATSHEET.md)
- [学习记录模板](../scripts/templates/study_record.md)
- [基础运行](../scripts/README.md)与[进阶运行](../scripts/ADVANCED.md)
- [故障指南](../docs/TROUBLESHOOTING.md)与[进阶验收](../docs/ADVANCED_VALIDATION.md)

每课按“理解→预测→操作→观察→变式→解释”学习。基础每次约 30～60 分钟，进阶约 45～90 分钟，按自己的节奏推进。

```bash
bash scripts/learn.sh catalog
bash scripts/learn.sh progress
```
