# C03：创建、复制、移动与删除练习文件

[课程总览](../../../README.md) · [理论补充](THEORY.md) · [上一课](../02_paths_navigation/README.md) · [下一课](../04_read_text/README.md)

## 学习目标

理解 mkdir、touch、cp、mv、rm 和重定向各自做什么。

## 先理解

touch 更新时间戳，文件不存在时会创建空文件；cp 复制，mv 移动或重命名。> 写入文件会截断已有内容，>> 追加。rm 删除指定目录项，终端删除通常不进入桌面回收站。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
mkdir -p scripts/practice/files
printf '第一条笔记\n' > scripts/practice/files/original.txt
cp -i scripts/practice/files/original.txt scripts/practice/files/copy.txt
mv -i scripts/practice/files/copy.txt scripts/practice/files/renamed.txt
cat scripts/practice/files/renamed.txt
# 确认这是刚建立的副本，再删除它；提示时输入 y
rm -i scripts/practice/files/renamed.txt
bash scripts/study.sh demo files
```

## 观察与完成标准

副本改名后内容仍是“第一条笔记”；删除副本后 original.txt 仍在。自动实验会额外验证复制后的内容。

## 自己动手

给 original.txt 追加第二行；解释追加与覆盖的区别，列出目录确认最终只保留原文件。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

mkdir -p 可重复建立目录，但 > 会覆盖文件内容；cp 到已存在的同名目标也可能覆盖。

## 自检

1. touch 会写入文字吗？
2. rm 副本会删除原文件吗？

<details>
<summary>完成后查看参考答案</summary>

1. 不会。
2. 普通复制生成不同文件，删除副本不删除原文件。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../../docs/RESOURCES.md)。
