# H01：引号、展开与参数边界

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [下一课](../02_sed_awk/README.md)

## 前置知识

[C01](../../../lessons/terminal/01_shell_commands/README.md)、[C02](../../../lessons/terminal/02_paths_navigation/README.md)、[C07](../../../lessons/terminal/07_environment_paths/README.md)、[P07](../../../programming/07_bash_basics/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

解释 Shell 在启动程序前怎样处理变量、空格和通配符，避免把一个路径传成多个参数。

## 原理与步骤

1. 单引号保留字面字符；双引号允许变量展开但保留空格。
2. 裸 *.txt 由 Shell 匹配路径，"*.txt" 是一个字面参数。
3. 先判断参数数目，再解释目标程序得到什么。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab quoting
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `quoting` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

三行输出依次是 two words、one.txt、*.txt。实验只创建自己的 one.txt；命令日志保留实际传入参数。

## 变式练习

另建脚本，用 set -- "$value" 和 set -- $value 对照 $#；令 value="two words"，预测参数数量分别为 1 与 2。再增加匹配文件，预测通配符结果。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

引号是 Shell 语法，通常不会成为程序收到的字符；字符串中的路径并不会自动检查是否存在。

## 自检

1. 为什么 "$value" 与 $value 不一样？
2. 程序收到引号本身吗？

<details>
<summary>完成后查看参考答案</summary>

1. 未加引号可能发生分词和通配符展开。
2. 用于分组的语法引号会被 Shell 去掉。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
