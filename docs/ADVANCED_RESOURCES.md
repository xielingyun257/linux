# 进阶资料与版本依据

核对日期：2026-10-05。具体参数优先本机 --help/man，网页以原作者或上游文档为准。教学正文由本仓库编写，详细命令同时通过本机实验检查。

| 主题 | 官方资料 | 本轮依据 |
| --- | --- | --- |
| 参数解析 | [Python 3.10 argparse](https://docs.python.org/3.10/library/argparse.html) | 已访问；工具按输入契约和状态测试 |
| 数据对象 | [dataclasses](https://docs.python.org/3.10/library/dataclasses.html) | 已访问；frozen 不等于完整业务校验 |
| 测试 | [unittest](https://docs.python.org/3.10/library/unittest.html) | 已访问；实际执行 discover 与边界测试 |
| 并发 | [concurrent.futures](https://docs.python.org/3.10/library/concurrent.futures.html) | 已访问；区分任务完成顺序和返回顺序 |
| 打包 | [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/) | 本次返回 403；离线 setuptools 后端、wheel 和安装命令以本机验证为依据 |
| Bash、awk、sed | [Jammy Bash](https://manpages.ubuntu.com/manpages/jammy/en/man1/bash.1.html)、[GNU gawk](https://www.gnu.org/software/gawk/manual/gawk.html)、[GNU sed](https://www.gnu.org/software/sed/manual/sed.html) | 不假定本机 awk 就是 gawk；本课使用常见基本语法 |
| 文件锁与资源 | [fcntl](https://docs.python.org/3.10/library/fcntl.html)、[resource](https://docs.python.org/3.10/library/resource.html) | Linux 专用行为，结合当前文件系统与进程观察 |
| systemd 验证 | [Jammy systemd-analyze](https://manpages.ubuntu.com/manpages/jammy/en/man1/systemd-analyze.1.html) | 已访问；静态验证不代替运行日志 |
| timer | [Jammy systemd.timer](https://manpages.ubuntu.com/manpages/jammy/en/man5/systemd.timer.5.html) | 已访问；Persistent 与 calendar 边界 |
| 增量传输 | [Jammy rsync](https://manpages.ubuntu.com/manpages/jammy/en/man1/rsync.1.html) | 已访问；link-dest 硬链接与恢复实际检查 |
| SSH | [OpenSSH 手册](https://www.openssh.com/manual.html) | 本地 ssh -G 解析，不代表远端认证已验证 |
| 调试 | [GDB 官方手册](https://sourceware.org/gdb/current/onlinedocs/gdb.html/)、[GCC instrumentation](https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html) | 本机 gdb/AddressSanitizer 演示，以运行证据为准 |
| CMake/CTest | [CMake 3.22](https://cmake.org/cmake/help/v3.22/)、[CTest](https://cmake.org/cmake/help/v3.22/manual/ctest.1.html) | 基于本机 3.22 工具和实际测试 |
| Compose | [Compose 应用模型源码](https://github.com/docker/docs/blob/main/content/manuals/compose/intro/compose-application-model.md) | 上游原文已读取；仅解析配置，不运行容器 |

已经验证的边界见[进阶记录](ADVANCED_VALIDATION.md)。基础资料继续见[原资源页](RESOURCES.md)。在线版本可能更新，跨机器运行时重新记录工具路径、版本与文件系统。
