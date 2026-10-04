# P02：变量、类型、单位与容器

[课程总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../01_python_environment/README.md) · [下一课](../03_control_flow/README.md)

## 学习目标

用变量表达测量值，区分整数、浮点数、字符串、列表与字典。

## 先理解

变量名指向对象；类型决定支持的操作。列表按位置索引，从 0 开始；字典按键访问。物理单位要写进名称或记录，150 mm / 60 mm/s 才能解释为 2.5 s。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
bash scripts/study.sh python variables
# 阅读源码中的 variables 分支
sed -n '1,45p' scripts/programming/python/examples.py
mkdir -p scripts/practice/python
# 自己的新程序放 scripts/practice/python/ 下
```

## 观察与完成标准

打印 int、float、list，并保存 time_s=2.5、samples=[10,20,30]。JSON 是结构化文本，不能只靠终端格式判断数值类型。

## 自己动手

新建自己的变量练习，计算 240 mm 以 80 mm/s 运动所需时间；取 samples 的最后一个值，并记录类型。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

字符串 "10" 与整数 10 不同；列表越界会报 IndexError；毫米与米混用会产生数量级错误。

## 自检

1. [10,20,30][0] 是多少？
2. 240/80 的物理结果是什么？

<details>
<summary>完成后查看参考答案</summary>

1. 10。
2. 3 秒，前提是单位按题目一致。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../docs/RESOURCES.md)。
