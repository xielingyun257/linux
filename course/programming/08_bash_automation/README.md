# P08：遍历文件、批处理与稳健路径

[课程总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../07_bash_basics/README.md) · [下一课](../09_cpp_compilation/README.md)

## 学习目标

自动处理多个文件，并正确保留空格和特殊字符。

## 先理解

遍历文件不能依赖解析 ls 输出。find -print0 用零字节分隔路径，read -r -d "" 逐个读取；IFS= 避免裁剪空白。程序应先明确输入范围，再处理各文件并统计结果。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
bash scripts/study.sh bash automation
cat scripts/programming/bash/automation.sh
bash -n scripts/programming/bash/automation.sh
# 示例自动生成“课程 笔记.txt”和 another.txt
```

## 观察与完成标准

两份文本分别有 2 行与 1 行，总行数是 3。带空格的文件名被当成一个完整路径。

## 自己动手

在自己的新脚本里改成统计三个文件的行数，含一个空文件；手工预测后比较，并解释不使用 for f in $(ls) 的理由。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

wc -l 前后的空白可影响字符串格式，但可用整数算术处理。批处理如果重写输入，失败后可能无法重跑，应保留原件。

## 自检

1. -print0 解决什么问题？
2. 空文件会贡献多少行？

<details>
<summary>完成后查看参考答案</summary>

1. 路径含空格或换行时仍能明确分隔。
2. 零行。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../docs/RESOURCES.md)。
