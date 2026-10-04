# S06：磁盘空间、挂载与备份排错

[课程总览](../../../README.md) · [理论补充](THEORY.md) · [上一课](../05_network_ssh/README.md) · [下一课](../../../programming/01_python_environment/README.md)

## 学习目标

区分磁盘、分区、文件系统、目录占用和 inode。

## 先理解

df 从文件系统角度查看容量；du 累加路径占用；lsblk 查看块设备；findmnt 查看实际挂载。文件系统决定文件名、权限、链接等行为，本机仓库位于 ntfs3。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS
df -h .
df -i .
du -sh course scripts
findmnt -T . -o TARGET,FSTYPE,OPTIONS
bash scripts/study.sh project organize
```

## 观察与完成标准

能把仓库目录对应到挂载和设备。整理项目生成 3 个文件，保留原资料，并校验归档恢复内容；只是同一磁盘上的教学备份。

## 自己动手

比较 df 与 du 的对象，解释为何结果不必相等；为自己的重要资料写一份备份位置和恢复验证计划。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

容量未满仍可能出现 inode 或配额限制。课程不格式化分区，也不把同盘副本描述成抗磁盘故障的备份。

## 自检

1. du -sh course 衡量什么？
2. 同盘备份能应对整盘损坏吗？

<details>
<summary>完成后查看参考答案</summary>

1. 该目录树的占用。
2. 不能，重要资料需要独立介质或可信远端副本。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../../docs/RESOURCES.md)。
