# U01：Linux、Ubuntu 与电脑里的几层软件

[课程总览](../../../README.md) · [理论补充](THEORY.md) · [下一课](../02_desktop_windows/README.md)

## 学习目标

区分硬件、内核、发行版、桌面、终端与应用；查出本机系统版本。

## 先理解

CPU 执行指令，内存保存正在使用的数据，磁盘保存文件。Linux 内核管理硬件与进程；Ubuntu 把内核、软件包和桌面组合成可使用的系统。GNOME 是桌面环境，Bash 是命令解释器，它们负责不同的交互方式。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
cat /etc/os-release
uname -r
bash scripts/study.sh environment
```

## 观察与完成标准

本机 VERSION_ID 为 22.04，课程解释器是 /usr/bin/python3。uname 输出内核版本，不能拿它当 Ubuntu 版本号。环境报告的路径会随每次运行变化。

## 自己动手

在 scripts/practice/ 下新建自己的学习笔记，画出“硬件→内核→桌面/终端→应用”的关系，并记录两个版本号的含义。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

Ubuntu、Linux 和终端不是同一个软件；网上不同发行版的安装命令不能直接混用。

## 自检

1. Bash 属于内核吗？
2. 系统版本与内核版本为什么不同？

<details>
<summary>完成后查看参考答案</summary>

1. 不属于，它是用户空间程序。
2. Ubuntu 发行版和 Linux 内核分别维护、分别编号。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../../docs/RESOURCES.md)。
