# T01：nano、Vim 与文本编辑模式

[课程总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../../programming/10_cmake_debug/README.md) · [下一课](../02_vscode_debug/README.md)

## 学习目标

在终端新建并保存练习文件，掌握退出方式。

## 先理解

编辑器修改文本，Shell 执行命令。nano 的界面底部提示 ^ 代表 Ctrl；Vim 的普通模式执行动作，插入模式输入文字。先练习保存与退出，再增加快捷键。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
mkdir -p scripts/practice/editor
nano scripts/practice/editor/nano-note.txt
# nano：输入文字，Ctrl+O 保存，Enter 确认，Ctrl+X 退出
vim scripts/practice/editor/vim-note.txt
# Vim：i 插入，Esc 回普通模式，:wq 保存退出
cat scripts/practice/editor/nano-note.txt
```

## 观察与完成标准

两份新笔记保存成功。Vim 放弃尚未保存的修改可用 :q!，普通退出 :q 可能因有改动而拒绝。

## 自己动手

给笔记新增三行，在 Vim 中查找其中一个词，再保存；用 cat 确认文件内容与编辑器显示一致。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

在 Vim 普通模式敲字母可能触发操作；想输入文字先确认模式。保存前确认路径，课程示例源码只阅读，自己的练习另建。

## 自检

1. nano 的 ^O 表示什么？
2. Vim 的 Esc 做什么？

<details>
<summary>完成后查看参考答案</summary>

1. Ctrl+O 保存。
2. 返回普通模式。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../docs/RESOURCES.md)。
