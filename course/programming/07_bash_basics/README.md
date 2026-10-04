# P07：Bash 脚本、变量、参数与条件

[课程总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../06_files_errors/README.md) · [下一课](../08_bash_automation/README.md)

## 学习目标

把手动命令写成脚本，理解脚本参数与返回状态。

## 先理解

Bash 擅长连接系统命令。变量赋值的等号两侧不加空格，使用时通常写 "$变量"；$1 是第一个参数，$# 是参数数目。[[ ]] 作条件判断，$(( )) 作整数运算。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
bash scripts/study.sh bash basics
cat scripts/programming/bash/basics.sh
bash -n scripts/programming/bash/basics.sh
# bash -n 只检查语法，不运行脚本
```

## 观察与完成标准

输出你好与筛选数字之和 19，并保存 result.txt。语法检查通过不等于逻辑正确，所以脚本还校验计算结果。

## 自己动手

在自己的新脚本里接收名字参数并用 printf 打招呼；未提供参数时显示清楚的用法。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

Bash 赋值 name = value 会被解释为命令。裸变量展开可能分词和展开通配符；set -e 有上下文例外，不是完整的错误处理。

## 自检

1. "$1" 指什么？
2. Bash 整数 5/2 是多少？

<details>
<summary>完成后查看参考答案</summary>

1. 脚本第一个位置参数。
2. 在整数算术中为 2，浮点计算交给合适的工具。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../docs/RESOURCES.md)。
