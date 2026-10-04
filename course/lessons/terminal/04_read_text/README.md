# C04：查看文本、日志与文件类型

[课程总览](../../../README.md) · [理论补充](THEORY.md) · [上一课](../03_file_operations/README.md) · [下一课](../05_search_find/README.md)

## 学习目标

按文件大小和用途选择 cat、less、head、tail 与 file。

## 先理解

cat 输出整个文件；less 分页浏览；head/tail 查看开头或末尾。file 根据内容特征猜测类型，wc 可计数。程序输出不一定是 UTF-8 文本，不应把所有二进制文件直接交给 cat。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
bash scripts/study.sh demo text
# 下面用源码文本练习，不改动它
head -n 12 scripts/lab.py
tail -n 8 scripts/lab.py
wc -l scripts/lab.py
file scripts/lab.py
less scripts/lab.py
```

## 观察与完成标准

head 和 tail 显示不同部分，wc -l 输出行数。less 中按 / 搜索 new_run，按 n 继续，按 q 退出。

## 自己动手

在刚生成的 events.log 中分别查首两行、末两行和总行数；说明 tail -f 与一次性的 tail 有何差别。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

tail -f 会持续等待新内容，需 Ctrl+C 结束；wc -l 计的是换行符，最后一行没有换行时可能与肉眼数行不同。

## 自检

1. 大日志先用 cat 还是 less？
2. 扩展名能保证真实文件类型吗？

<details>
<summary>完成后查看参考答案</summary>

1. less 更适合分页查看。
2. 不能，应结合内容和生成方式。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../../docs/RESOURCES.md)。
