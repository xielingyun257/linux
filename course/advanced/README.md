# Linux 进阶课程：24 节实践

在基础操作之后学习可靠脚本、系统观察、工程工具和可复现实验。可以按顺序，也可按[目标路线](../START_HERE.md)进入；每节明确列出前置知识。

| 系列 | 节数 | 核心能力 |
| --- | --- | --- |
| [Bash 与文本处理](shell/README.md) | 6 | 参数、解析、退出、CLI 与文件锁 |
| [系统与网络](systems/README.md) | 6 | 资源、性能、HTTP、SSH、调度、备份 |
| [程序工程](engineering/README.md) | 8 | 模型、测试、打包、并发、C++、调试、Git、容器 |
| [复现与排错](workflows/README.md) | 4 | 项目阅读、证据包、诊断与巡检工具 |

| 编号 | 课程 | 实验名 |
| --- | --- | --- | --- |
| H01 | [引号、展开与参数边界](shell/01_quoting/README.md) | `quoting` |
| H02 | [sed、awk 与结构化文本](shell/02_sed_awk/README.md) | `text` |
| H03 | [find、xargs 与复杂文件名](shell/03_nul_paths/README.md) | `paths` |
| H04 | [退出状态、信号与资源清理](shell/04_graceful_exit/README.md) | `signals` |
| H05 | [参数化命令行工具与机器可读报告](shell/05_cli_contract/README.md) | `cli` |
| H06 | [文件锁、原子替换与重复运行](shell/06_lock_atomic/README.md) | `atomic` |
| N01 | [/proc、资源上限与观察范围](systems/01_proc_limits/README.md) | `proc` |
| N02 | [性能测量、复杂度与 strace](systems/02_performance_strace/README.md) | `timing` |
| N03 | [HTTP 状态、curl 与分层网络排错](systems/03_http_diagnosis/README.md) | `http` |
| N04 | [SSH 配置、密钥与端口转发](systems/04_ssh_config/README.md) | `ssh-config` |
| N05 | [systemd unit、用户服务与定时器](systems/05_user_timers/README.md) | `systemd` |
| N06 | [rsync、增量快照与恢复](systems/06_incremental_backup/README.md) | `backup` |
| E01 | [类、dataclass、类型提示与数据模型](engineering/01_models_types/README.md) | `objects` |
| E02 | [单元测试、边界输入与失败契约](engineering/02_unittest/README.md) | `tests` |
| E03 | [Python 打包、wheel 与安装入口](engineering/03_offline_packaging/README.md) | `packaging` |
| E04 | [线程池、Future 与任务汇总](engineering/04_concurrency/README.md) | `concurrency` |
| E05 | [C++ 库目标、接口与 CTest](engineering/05_cpp_library_tests/README.md) | `cpp` |
| E06 | [gdb、调用栈与 AddressSanitizer](engineering/06_debug_sanitizer/README.md) | `debugging` |
| E07 | [Git 冲突、abort 与 bisect](engineering/07_git_recovery/README.md) | `git` |
| E08 | [Dockerfile、Compose 与环境边界（选修）](engineering/08_container_build/README.md) | `containers` |
| R01 | [阅读陌生项目：入口、依赖与数据流](workflows/01_read_project/README.md) | `reading` |
| R02 | [种子、参数、源码摘要与复现实验](workflows/02_reproducibility/README.md) | `reproduce` |
| R03 | [故障排查：证据、假设与最小改动](workflows/03_incident_method/README.md) | `incident` |
| R04 | [综合实战：日志巡检、阈值与归档](workflows/04_capstone/README.md) | `capstone` |

## 怎么开始

```bash
bash scripts/advanced.sh doctor
bash scripts/advanced.sh lab quoting
```

每次 45～90 分钟，一节可分两次。先完成自动实验，再做变式；不把“能跑现成命令”当成学会。完整范围见[进阶验收](../../docs/ADVANCED_VALIDATION.md)。

阶段任务见[里程碑](../MILESTONES.md)，实际任务查[场景索引](../SCENARIOS.md)。学习进度由你主动记录，运行实验不会自动打勾。

最后可选做[日志巡检工具](../../projects/cli_inspector/README.md)、[复现实验包](../../projects/reproducible_run/README.md)和[Git 恢复演练](../../projects/git_rescue/README.md)。
