# C01：终端、Shell 与一条命令的结构

[课程总览](../../../README.md) · [理论补充](THEORY.md) · [上一课](../../ubuntu_basics/06_screenshots_learning/README.md) · [下一课](../02_paths_navigation/README.md)

## 学习目标

读懂命令名、选项、参数、提示符和退出状态。

## 先理解

终端传递键盘输入并显示结果，Bash 解析命令，具体程序完成任务。ls -la scripts 中 ls 是程序，-la 是短选项组合，scripts 是路径参数。Shell 内建命令 cd 会改变当前 Shell 的状态。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
pwd
type cd
type ls
ls -la scripts
false
printf '上一条退出状态：%s\n' "$?"
```

## 观察与完成标准

cd 被识别为内建命令，ls 通常是程序或别名；false 的状态是 1。printf 成功后再看 $?，看到的是 printf 的状态。

## 自己动手

将 ls -la scripts 拆成三部分，尝试 ls -l -a scripts 并解释结果为何相同。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

Shell 区分大小写；命令提示符中的用户名、路径和 $ 不属于要输入的命令。

## 自检

1. 退出状态 0 通常表示什么？
2. 为什么另一个终端的 cd 不影响本终端？

<details>
<summary>完成后查看参考答案</summary>

1. 命令成功。
2. 每个 Shell 有自己的当前目录等状态。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../../docs/RESOURCES.md)。
