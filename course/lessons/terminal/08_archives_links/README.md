# C08：压缩归档、校验与软链接

[课程总览](../../../README.md) · [理论补充](THEORY.md) · [上一课](../07_environment_paths/README.md) · [下一课](../../system/01_users_permissions/README.md)

## 学习目标

列出压缩包内容，解释归档与压缩的区别，认识软链接。

## 先理解

tar 把多个路径组织成归档；gzip 压缩字节。tar -czf 创建 gzip 归档，-tzf 查看清单。软链接保存目标路径，目标移走后链接可能失效；它不是文件内容的副本。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
bash scripts/study.sh demo archives
mkdir -p scripts/practice/links
printf '链接目标\n' > scripts/practice/links/target.txt
ln -s target.txt scripts/practice/links/shortcut.txt
ls -l scripts/practice/links
cat scripts/practice/links/shortcut.txt
sha256sum scripts/practice/links/target.txt
```

## 观察与完成标准

归档实验得到 notes.tar.gz 和 restored.txt，并验证字节一致。软链接显示 shortcut.txt -> target.txt；本机 NTFS 挂载能否建链接以实际结果为准。链接已存在时 ln 会报错。

## 自己动手

对归档内容先列清单，再在一个新目录恢复；比较恢复文件与原文件的校验值。给软链接画出指向关系。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

软链接目标的相对路径相对链接所在目录。压缩成功不等于备份可恢复，还需要实际读取或恢复校验。

## 自检

1. 归档必须压缩吗？
2. SHA-256 相同在这里说明什么？

<details>
<summary>完成后查看参考答案</summary>

1. 不必，tar -cf 可只归档。
2. 支持两份文件内容一致的判断；不是来源真实性证明。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../../docs/RESOURCES.md)。
