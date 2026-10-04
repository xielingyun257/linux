# 进阶运行、进度与课程维护

[60 节课程](../course/README.md) · [进阶导览](../course/advanced/README.md)

原基础入口 study.sh 保留原样。新增 advanced.sh 提供 24 个实验，learn.sh 汇总目录、进度与检查，也可以转发两套入口。

```bash
bash scripts/learn.sh catalog
bash scripts/learn.sh progress
bash scripts/learn.sh base python variables
bash scripts/learn.sh advanced lab quoting
```

## 实验命令

统一格式是 `bash scripts/advanced.sh lab 实验名`，实验名如下。不要将表中多个选择合成一个参数。

| 系列 | 实验名 |
| --- | --- |
| H01～H06 | quoting、text、paths、signals、cli、atomic |
| N01～N06 | proc、timing、http、ssh-config、systemd、backup |
| E01～E08 | objects、tests、packaging、concurrency、cpp、debugging、git、containers |
| R01～R04 | reading、reproduce、incident、capstone |

```bash
bash scripts/advanced.sh doctor
bash scripts/advanced.sh lab cli
bash scripts/advanced.sh lab reproduce
```

每次新建 scripts/runs/ 下的目录，包含 lab.json 和实际子命令日志。失败任务同样保留证据。编译、测试、pip 缓存与临时文件均留在仓库内；自动任务不连接远端、不启用服务或 Docker daemon。

## 记录学习进度

```bash
bash scripts/learn.sh record H01 --status learning --note '正在比较引号和参数'
# 真正完成变式和自检后：
bash scripts/learn.sh record H01 --status done --note '能解释 1 个与 2 个参数的区别'
# 以后要复习：
bash scripts/learn.sh record H01 --status review --note '需要再练习通配符'
bash scripts/learn.sh progress
```

状态由自己判断，实验运行不会自动记完成。默认记录在 scripts/runtime/study_progress.json，仅本机使用、不推送；学习笔记和正式源码可放 scripts/exercises/。未知课程编号或格式错误不会覆盖既有记录。

## 参数化日志工具

```bash
/usr/bin/python3 -E -s scripts/advanced/log_cli.py --help
# 先运行 lab cli 取得教学 events.csv，再替换真实的实验路径
# /usr/bin/python3 -E -s scripts/advanced/log_cli.py --input 输入.csv --output 新报告.json --max-error-rate 0.5
```

输出必须在仓库内，且不覆盖已有文件。状态 0 为按当前规则通过，2 为输入输出问题，3 为 strict 格式问题，4 为超限，5 为没有合法数据。报告中的错误率只以合法记录为分母，空数据为 null。

## 依赖与完整验收

系统 Python 标准库负责主线；awk/sed/find/xargs、rsync、ssh、curl、systemd-analyze、strace、gdb、g++、CMake/CTest 是对应工具实验依赖。离线打包使用系统已安装的 setuptools/wheel，并在仓库内创建 --system-site-packages venv。缺工具时先读对应课与官方资料，不自动下载或安装。

```bash
bash scripts/advanced.sh smoke
bash scripts/learn.sh check
```

smoke 检查 doctor、24 个实验和完整课程。check 还核对课程目录、文档链接、命令块、新记录的往返行为，以及原有 15 个源码文件的摘要。详细结果见[进阶验证记录](../docs/ADVANCED_VALIDATION.md)。

## 重建所有课程文档

```bash
/usr/bin/python3 -I scripts/build_all_docs.py
bash scripts/learn.sh check
```

新增总构建器顺序调用原基础生成器和进阶生成器，最后生成 60 节导航。只运行旧基础生成器会暂时恢复为 36 节总览，需要随后执行完整构建器。根 README、路线、里程碑、项目说明和验证记录单独维护。
