# T04：Git 分支、合并与同步

[课程总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../03_git_basics/README.md) · [下一课](../05_tmux/README.md)

## 学习目标

读懂分支历史，区分 fetch、pull、merge 与 push。

## 先理解

分支是指向提交的可移动名字。switch 切换工作状态，merge 整合历史，fetch 下载远端历史，pull 再整合到当前分支。冲突是需要选择最终内容的情况，不代表 Git 丢失全部资料。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
bash scripts/study.sh demo git
# 在本次 example-repository 中执行以下只读观察
# git branch -av
# git log --oneline --graph --all
# git show HEAD
# 本地示例没有配置远端，因此不演示真实 pull/push
```

## 观察与完成标准

看到 main、practice 和一次合并提交；主仓库 main 没被切换。--no-ff 保留演示中的合并节点，便于观察历史结构。

## 自己动手

在示例仓库创建另一分支，新增一个独立文件并提交，再合并回 main；预测提交图变化。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

不要用强制推送或硬重置处理看不懂的同步问题。合并前确认工作区状态；真实远端操作要针对正确仓库与分支。

## 自检

1. fetch 会直接修改当前文件吗？
2. 分支一定是一个复制出来的目录吗？

<details>
<summary>完成后查看参考答案</summary>

1. 通常只更新远端历史引用，不直接整合工作区。
2. 不是，它是历史引用，工作目录随切换呈现相应内容。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../docs/RESOURCES.md)。
