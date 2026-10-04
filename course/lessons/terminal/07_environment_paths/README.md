# C07：环境变量、PATH 与启动配置

[课程总览](../../../README.md) · [理论补充](THEORY.md) · [上一课](../06_pipes_redirection/README.md) · [下一课](../08_archives_links/README.md)

## 学习目标

查清命令实际来自哪里，理解变量的作用范围。

## 先理解

Shell 变量存在于当前 Shell；export 后子进程可以继承。PATH 决定程序搜索顺序。source 在当前 Shell 执行文件，bash script.sh 使用另一个 Shell，因此二者对环境的影响不同。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
printf '%s\n' "$PATH"
type -a python3
command -v python3
/usr/bin/python3 --version
LINUX_LESSON_MESSAGE='一次命令的环境' /usr/bin/python3 -c 'import os; print(os.environ["LINUX_LESSON_MESSAGE"])'
bash scripts/study.sh environment
```

## 观察与完成标准

本机裸 python3 优先找到 Miniforge，课程入口固定 /usr/bin/python3。单条命令的环境赋值不会永久写入 ~/.bashrc。

## 自己动手

创建一个自己的变量，先不 export 再 export，用子进程读取并比较；完成后 unset 该练习变量。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

不要为一个项目替换系统 /usr/bin/python3 链接。当前终端临时设置与写入启动配置是两种操作。

## 自检

1. source 与 bash 的环境作用范围相同吗？
2. 绝对路径启动程序还需 PATH 查找吗？

<details>
<summary>完成后查看参考答案</summary>

1. 不同。
2. 指定该程序时不需要搜索 PATH。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../../docs/RESOURCES.md)。
