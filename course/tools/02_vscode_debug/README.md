# T02：VS Code 工作区、解释器与断点

[课程总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../01_editors/README.md) · [下一课](../03_git_basics/README.md)

## 学习目标

打开课程工作区，选择解释器并单步观察变量。

## 先理解

VS Code 是编辑器，Python 扩展提供语言与运行功能，Python Debugger 扩展提供调试。解释器选择、终端激活环境和运行配置可能分别决定运行入口，要查看 sys.executable 确认。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
mkdir -p scripts/practice/debug
# 在 Ubuntu 桌面终端打开：
code scripts/editor/linux-study.code-workspace
# 扩展：Microsoft Python、Python Debugger
# 命令面板：Python: Select Interpreter → /usr/bin/python3
# 在 wrong_mean 的 return 行设断点；运行“平均值错误演示”
bash scripts/study.sh project debug
```

## 观察与完成标准

自动项目展示错误平均值 11 与正确值 11.75。桌面断点应看到 values=[10,11,12,14]，sum=47，// 导致向下取整。

## 自己动手

用 Step Into 进入函数，用变量面板检查输入；比较 Step Over 和 Continue。把自己的修复放新文件，说明为什么 / 合适。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

编辑器选中的解释器不必与一个已打开的终端一致。图形断点操作由学习者实际完成；自动脚本只验证数值与入口。

## 自检

1. 断点会修改源代码吗？
2. 47//4 与 47/4 各是多少？

<details>
<summary>完成后查看参考答案</summary>

1. 不会，调试器在执行时暂停。
2. 11 与 11.75。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../docs/RESOURCES.md)。
