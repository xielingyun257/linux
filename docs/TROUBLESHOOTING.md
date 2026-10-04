# 按证据排查常见问题

[课程总览](../course/README.md) · [环境说明](ENVIRONMENT.md)

先记录目标、完整命令、当前目录、退出状态与错误全文。按下面顺序缩小范围，不要一上来重装或提高所有权限。

## 找不到文件或入口

```bash
pwd
ls -la
ls scripts/study.sh
```

仓库根目录应有 README、course、scripts。带空格的路径加引号；教程路径中的占位文字要换成真实值。自动入口可从任意目录用绝对路径调用。

## command not found

```bash
command -v 命令名
type -a 命令名
printf '%s\n' "$PATH"
```

先确认拼写，再确认软件是否安装和 PATH 是否包含它。程序存在但找不到，不代表必须重装。主线缺工具时查系统包课；自动入口不会替你安装。

## Python 与 pip 用错环境

```bash
command -v python3
/usr/bin/python3 -c 'import sys; print(sys.executable)'
bash scripts/study.sh environment
```

本机裸 python3 默认来自 Miniforge。课程用 bash scripts/study.sh，不要通过改系统解释器链接“修复”。venv 安装包使用 venv/bin/python -m pip；同目录模块导入需普通脚本搜索路径，-I 会改变它。

## Permission denied 或 chmod 与预期不同

```bash
id
ls -ld . scripts
findmnt -T . -o TARGET,FSTYPE,OPTIONS
bash scripts/study.sh demo permissions
```

检查文件及父目录、执行位、挂载选项和实际所有者。课程入口用 bash 启动，不需要 study.sh 自身执行位；NTFS 权限呈现与 ext4 可能不同。先说明缺哪项权限，再决定是否需要管理员操作。

## 命令卡住、进程没结束

交互浏览器 less/man 用 q 退出，sleep/tail -f 可用 Ctrl+C。jobs -l 看当前 Shell 作业，ps 检查自己的 PID；Ctrl+Z 是暂停。先正常退出，再对属于自己的任务发送 SIGTERM。自动进程、网络、tmux 演示会回收自己创建的资源。

## 编译错误与程序错误

编译器报错先看第一个错误和源文件行号。能编译不等于结果正确；确认运行的是新生成的可执行文件。更换编译器或环境时新建构建目录，避免旧 CMake 缓存。

## 服务、SSH、Docker 不可用

systemctl 先确定本机实际服务名，再看日志和时间范围。SSH 分别判断地址解析、端口连接与认证问题；本地 HTTP 实验不证明外网可用。Docker 客户端版本可见不证明 daemon 工作，不为选修课自动开启服务或改用户组。

## Git 无法提交或推送

先看 git status、git remote -v 与当前分支。缺身份时使用用户自己的身份，不猜测；认证失败时保留本地提交，通过自己的 GitHub 凭证或已授权认证渠道解决。远端有新提交时先获取并查看差异，不强推覆盖。

## 怎样重新验收

```bash
bash scripts/study.sh validate
bash scripts/study.sh smoke
```

失败时找到本次 scripts/runs/ 目录中的 commands.jsonl 和 smoke.json。它们保存实际命令与状态，便于区分环境缺失、输入问题和结果不符。
