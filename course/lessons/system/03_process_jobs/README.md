# S03：进程、前后台与任务结束

[课程总览](../../../README.md) · [理论补充](THEORY.md) · [上一课](../02_packages_software/README.md) · [下一课](../04_services_logs/README.md)

## 学习目标

识别 PID、父进程与状态，结束自己创建的任务。

## 先理解

程序是文件，进程是程序的一次运行。PID 是当前进程标识；& 让 Shell 不等待任务；jobs 显示本 Shell 管理的作业。Ctrl+C 通常中断前台任务，kill 默认发送 SIGTERM，程序可以处理这个信号后退出。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
ps -p $$ -o pid,ppid,stat,comm
sleep 60 &
linux_lesson_pid=$!
jobs -l
ps -p "$linux_lesson_pid" -o pid,ppid,stat,comm
kill "$linux_lesson_pid"
wait "$linux_lesson_pid"
bash scripts/study.sh demo processes
```

## 观察与完成标准

看到自己创建的 sleep PID；kill 后 wait 可能返回非零，因为进程被信号结束。自动实验会回收自己的子进程并保存 reaped=true。

## 自己动手

在同一终端启动 sleep，再使用 Ctrl+Z、jobs、bg、fg，最后 Ctrl+C；解释“暂停”和“退出”。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

jobs 只看本 Shell 的作业。不要按常见程序名全局杀进程；PID 也可能被复用，应确认归属。

## 自检

1. Ctrl+Z 会删除进程吗？
2. 为何优先正常退出或 SIGTERM？

<details>
<summary>完成后查看参考答案</summary>

1. 通常暂停前台作业。
2. 给程序清理资源、保存数据的机会，SIGKILL 无法被处理。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../../docs/RESOURCES.md)。
