# T03：Git 工作区、暂存区与提交

[课程总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../02_vscode_debug/README.md) · [下一课](../04_git_branches/README.md)

## 学习目标

理解 status、diff、add、commit、log 与远端的关系。

## 先理解

工作区是当前文件，暂存区是准备提交的快照，提交是本地历史。add 不上传，commit 不上传，push 才向远端传递提交。Git 记录版本，GitHub 提供远端托管。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
git status --short --branch
git log -3 --oneline
git diff
git remote -v
bash scripts/study.sh demo git
# 想保存自己的代码时，新建 scripts/exercises/ 下的文件
# 只 add 你准备提交的文件，再用中文写 commit message
```

## 观察与完成标准

主仓库 origin 指向用户提供的地址；自动演示在独立示例仓库创建历史，没有改动主仓库分支或推送演示内容。

## 自己动手

进入本次 example-repository，新增自己的 notes2.md；依次观察未跟踪、已暂存、已提交三个状态，用中文提交。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

.gitignore 主要影响未跟踪文件，不会自动移除已跟踪文件。运行结果、虚拟环境和临时练习被忽略，正式练习可放 scripts/exercises/。

## 自检

1. commit 是否必须联网？
2. git diff 与 git diff --staged 有何不同？

<details>
<summary>完成后查看参考答案</summary>

1. 不必，本地操作。
2. 前者看未暂存修改，后者看暂存区相对上次提交的变化。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../docs/RESOURCES.md)。
