# 运行入口与示例

从仓库根目录运行 `bash scripts/study.sh ...`。脚本自身定位仓库，因此也可用绝对路径从其他目录调用。主入口用系统 Python 的 `-I` 隔离模式，局部模块示例用 `-E -s` 保留同目录导入。

## 命令表

| 命令 | 内容 | 主要输出 |
| --- | --- | --- |
| `environment` | 系统、解释器、工具与挂载 | environment.json |
| `demo files` | 空格/中文路径、复制与重命名 | 笔记与 renamed.txt |
| `demo text` | 错误日志管道计数 | events.log、counts.json |
| `demo permissions` | 请求与实际权限位比较 | permissions.json |
| `demo processes` | 查看并回收自己的子进程 | process.json |
| `demo network` | 本机 HTTP 请求与关闭 | network.json |
| `demo archives` | 归档和字节一致性 | notes.tar.gz、archive.json |
| `demo git` | 独立仓库提交、分支与合并 | example-repository/ |
| `demo tmux` | 独立 socket 会话与关闭 | commands.jsonl |
| `python variables/flow/functions/modules/files/errors` | 六种标准库示例 | result.json、部分含 CSV |
| `bash basics/automation` | 变量与稳健文件遍历 | result.txt |
| `cpp intro/cmake` | 直接编译或 CMake 构建 | angle、cpp.json |
| `project organize/logs/debug` | 三个综合项目 | 清单、统计、调试报告 |
| `validate` | 课程结构、链接、源码语法 | validation.json |
| `smoke` | 全部 23 项验收 | smoke.json 与各实验目录 |

表中 `/` 是选择项说明，不能原样当成一个参数。完整例子：

```bash
bash scripts/study.sh python files
bash scripts/study.sh cpp cmake
bash scripts/study.sh project logs
```

## 依赖和输出

主线无需 pip 安装。需要系统 `bash`、`git`、`g++`、`cmake`、`make`、`tar`、`findmnt` 与 Python 3.10；tmux 验收还需 tmux。本机均已找到，详见[环境说明](../docs/ENVIRONMENT.md)。编辑器和 Docker 是手动工具课的依赖，不参与 smoke。

每次实验在 `scripts/runs/` 下创建 UTC 时间、主题与随机后缀组成的唯一目录。命令记录保存 argv、工作目录、退出状态、标准输出和标准错误。编译器临时文件的 TMPDIR 也指向本次仓库内目录。

`scripts/runtime/` 放热身、可选 venv 与运行准备。`scripts/practice/` 是被 Git 忽略的草稿；想提交自己的练习，放 `scripts/exercises/`。这些目录不替代真正备份，重要资料应另有独立副本。

进程演示只结束自己创建的子进程；HTTP 只监听 127.0.0.1 随机端口，结束时关闭；tmux 使用自己的 socket，结束时清理自己的服务器。自动程序不加载 ROS。

## 重建文档与检查

```bash
/usr/bin/python3 -I scripts/build_course_docs.py
bash scripts/study.sh validate
bash scripts/study.sh smoke
```

构建器维护操作课、理论页、课程导航和清单。术语、来源、项目说明和验证记录单独维护。smoke 的完成标准包括文件字节、数值容差、日志计数、Git 历史、资源回收与文档完整性，详见[验证记录](../docs/VALIDATION.md)。

最小热身可用 `bash scripts/warmup.sh`；会另建目录和一个允许系统包的 venv，不安装第三方包。
