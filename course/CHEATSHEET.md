# 常用命令速查

[课程总览](README.md) · [故障指南](../docs/TROUBLESHOOTING.md)

这张表用于学过之后回顾，不建议把整张表一次运行。路径与文件名是参数，先确认工作目录；完整练习见对应课程。

| 任务 | 命令或操作 | 提醒 |
| --- | --- | --- |
| 查看当前位置 | `pwd` | 文件操作前确认 |
| 查看目录 | `ls -la` | -a 包含隐藏文件 |
| 进入目录 | `cd '带 空格的目录'` | 引号保留路径 |
| 回父目录 | `cd ..` | 与 cd.. 不同 |
| 创建目录 | `mkdir -p scripts/practice/example` | 不创建文件内容 |
| 写文本 | `printf 'hello\n' > 文件` | > 覆盖，>> 追加 |
| 复制 | `cp -i 源文件 目标文件` | -i 提示可能覆盖 |
| 移动/改名 | `mv -i 源路径 目标路径` | 操作目录项 |
| 删除自己的副本 | `rm -i 指定副本` | 先核对路径，不进入回收站 |
| 读短文本 | `cat 文件` | 不宜直接读未知二进制 |
| 分页读文本 | `less 文件` | / 搜索，q 退出 |
| 首尾几行 | `head -n 10 文件`、`tail -n 10 文件` | -f 会等待新内容 |
| 找文件名 | `find course -type f -name '*.md'` | 模式加引号 |
| 搜索文字 | `grep -n '文字' 文件` | -F 固定字符串，-E 扩展正则 |
| 管道计数 | `sort 文件 \| uniq -c` | uniq 合并相邻重复项 |
| 查实际程序 | `command -v python3`、`type -a python3` | 注意 Miniforge 顺序 |
| 查状态 | `printf '%s\n' "$?"` | 紧接要检查的命令 |
| 查帮助 | `命令 --help`、`man 命令` | 手册 q 退出 |
| 看用户与组 | `id` | 文件权限检查起点 |
| 看权限 | `ls -l 文件` | NTFS 实际行为需看挂载 |
| 查已安装包 | `dpkg-query -W 包名` | apt 与 pip 分层 |
| 查包版本来源 | `apt-cache policy 包名` | 查看已装/候选 |
| 看进程 | `ps -p PID -o pid,ppid,stat,comm` | 先确认任务归属 |
| 看作业 | `jobs -l` | 只看当前 Shell |
| 请求结束 | `kill 自己的PID` | 默认 SIGTERM |
| 看服务 | `systemctl status 服务名 --no-pager` | 不等于 enable 状态 |
| 看服务日志 | `journalctl -u 服务名 -n 20 --no-pager` | 权限与时间范围影响结果 |
| 看地址与路由 | `ip -br address`、`ip route` | 公网/内网/回环不同 |
| 看监听端口 | `ss -ltn` | 状态不代表协议认证成功 |
| 看文件系统空间 | `df -h .` | 当前路径所在挂载 |
| 看目录占用 | `du -sh course` | 与 df 统计范围不同 |
| 看挂载 | `findmnt -T .` | 文件系统与参数 |
| 创建归档 | `tar -czf 备份.tar.gz 指定目录` | 确认输入范围 |
| 查看归档 | `tar -tzf 备份.tar.gz` | 恢复前先看清单 |
| 内容摘要 | `sha256sum 文件` | 与已知正确副本比较 |
| Git 状态 | `git status --short --branch` | 提交前检查 |
| Git 差异 | `git diff`、`git diff --staged` | 工作区/暂存区不同 |
| Git 历史 | `git log --oneline --graph --all` | 看分支关系 |
| Python 环境 | `bash scripts/study.sh environment` | 课程固定系统解释器 |
| 本地文档验收 | `bash scripts/study.sh validate` | 不联网 |

桌面：Super 开概览，Ctrl+Alt+T 开终端，Alt+Tab 切换；终端复制粘贴通常为 Ctrl+Shift+C/V，Ctrl+C 中断前台任务。实际绑定以本机设置为准。

## 进阶速查

| 任务 | 入口或命令 | 要点 |
| --- | --- | --- |
| 保留位置参数 | `"$@"` | 每个参数保留独立边界 |
| 安全传递路径列表 | `find 目录 -type f -print0` 与 `xargs -0` | 两端分隔协议一致 |
| 统计字段 | `awk -F, 'NR>1 {sum+=$2; n++} END {print sum/n}' 文件` | 先明确合法记录和分母 |
| 检查 Shell 语法 | `bash -n 脚本` | 不运行，不验证逻辑 |
| 预览同步 | `rsync -av --dry-run 源目录/ 目标目录/` | 先看范围，不默认删文件 |
| SSH 配置解析 | `ssh -G -F 配置文件 别名` | 不建立连接 |
| unit 语法验证 | `systemd-analyze verify --man=no unit文件` | 不代替启用与运行 |
| 日历解析 | `systemd-analyze calendar --iterations=2 hourly` | 看时区与下次触发 |
| Python 边界测试 | `bash scripts/advanced.sh lab tests` | 正常、失败、空输入和覆盖保护 |
| C++ 测试 | `bash scripts/advanced.sh lab cpp` | 编译后实际执行 CTest |
| 调试与内存诊断 | `bash scripts/advanced.sh lab debugging` | 故意错误的非零状态是预期 |
| Git 恢复演练 | `bash scripts/advanced.sh lab git` | 独立示例，主仓库不切换 |
| 复现实验 | `bash scripts/advanced.sh lab reproduce` | 输入、参数、源码和结果摘要 |
| 查全部课程 | `bash scripts/learn.sh catalog` | 基础 36 + 进阶 24 |
| 看本机进度 | `bash scripts/learn.sh progress` | 自动运行不记完成 |
| 全课程检查 | `bash scripts/learn.sh check` | 文档、源码不变、进度往返 |

详细操作与边界见[进阶总览](advanced/README.md)。
