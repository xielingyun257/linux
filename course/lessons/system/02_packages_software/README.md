# S02：apt、dpkg、Snap 与软件安装

[课程总览](../../../README.md) · [理论补充](THEORY.md) · [上一课](../01_users_permissions/README.md) · [下一课](../03_process_jobs/README.md)

## 学习目标

查出软件包来源，理解安装、更新索引、升级和卸载的区别。

## 先理解

dpkg 管理本地 Debian 软件包，apt 处理仓库索引与依赖。apt update 更新可用软件信息，apt upgrade 升级已安装包。Snap 是另一套打包与分发机制；pip 管 Python 包，不能替代系统包管理。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
apt-cache policy git
dpkg-query -W git
dpkg -L git | head -n 12
command -v snap
# 以下是手动安装流程，自动实验不会执行：
# sudo apt update
# sudo apt install tree
# tree --version
```

## 观察与完成标准

显示 git 已安装版本与候选版本；dpkg -L 列出系统包管理器登记的路径。注释中的命令只在自己决定安装 tree 时执行。

## 自己动手

用 command -v 与 dpkg -S 查 git 可执行文件所属包，解释“可执行文件位置”和“包名”的区别。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

sudo pip install 可能污染系统 Python。添加第三方源之前应核对发行版代号和官方步骤；删除包不一定删除用户配置。

## 自检

1. apt update 会直接升级所有软件吗？
2. pip 包和 apt 包是同一层吗？

<details>
<summary>完成后查看参考答案</summary>

1. 不会，它更新索引。
2. 不是，分别服务于 Python 环境和系统包管理。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../../docs/RESOURCES.md)。
