# 项目三：平均值程序为什么算错了

[项目总览](../README.md) · [源码](../../scripts/projects/debug.py)

## 要解决的问题

输入 [10,11,12,14]，和为 47，平均值应为 11.75。使用 // 会得到 11，程序能正常运行但结果错误。

## 先预测，再运行

```bash
bash scripts/study.sh project debug
mkdir -p scripts/practice/debug
/usr/bin/python3 -I scripts/projects/debug.py scripts/practice/debug --bad
```

自动项目保存 debug.json，包含错误结果、正确结果和空输入处理。--bad 只展示错误算法，不把错误平均值写成正确输出。

## 用断点定位

打开 [VS Code 工作区](../../scripts/editor/linux-study.code-workspace)，在 wrong_mean 的 return 行设置断点，选择“平均值错误演示”。观察 values、sum(values)、len(values)，单步看到整数除法。

终端调试也可用：

```bash
/usr/bin/python3 -m pdb scripts/projects/debug.py scripts/practice/debug --bad
# pdb：b wrong_mean 设置断点；c 继续；p values 查看；n 单步；q 退出
```

## 自己动手

在自己的新文件中写平均值函数，检查普通输入、单元素和空列表。参考结果分别为 11.75、该元素自身、明确的 ValueError。增加一个非整数样例，说明为什么不能靠打印格式修复计算错误。

## 完成标准

能复现问题并定位到 //；说清显示精度和计算语义的区别；能说明空输入策略；用新输入验证修复。自动检查验证计算与异常，桌面断点需学习者实际完成。
