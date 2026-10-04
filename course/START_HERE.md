# 从哪里开始：按目标选择路线

[60 节总目录](README.md) · [阶段任务](MILESTONES.md) · [场景索引](SCENARIOS.md)

如果完全零基础，从 U01 开始。已经会操作时先尝试下面的自测；能独立完成、解释原因并处理一个变式，就可以按目标跳到相关课程。无需为了“看完所有页面”而重复已经掌握的内容。

## 五个快速自测

1. 在仓库内建立带空格的目录，写两行文字，找到文件并查看内容。
2. 解释普通文件复制、软链接、归档有什么区别。
3. 指出本机裸 python3 与课程入口分别运行哪个解释器。
4. 从一份日志中统计两类错误，解释管道里每一步的输入输出。
5. 运行一个小程序，给出成功与失败两种输入，并指出结果保存位置。

不会第 1 项：先学 [Ubuntu 与终端](lessons/ubuntu_basics/README.md)。不会第 2～4 项：重点学 [C02～C08](lessons/terminal/README.md)。不会第 3、5 项：进入 [Python 基础](programming/README.md)。自测不替代每课完成标准。

## 路线一：先把 Ubuntu 用顺手

U01～U06 → C01～C08 → S01/S02/S03/S06 → T01/T05。最后做[资料整理与备份](../projects/organize/README.md)。

目标是独立管理文件、查帮助、安装自己理解的软件、识别进程、看日志和空间。暂时不用开始 C++、容器或远程服务器。

## 路线二：Python 与自动化工具

P01～P06 → T02/T03 → P07/P08 → [H01～H06](advanced/shell/README.md) → [E01～E04](advanced/engineering/README.md) → [日志巡检工具](../projects/cli_inspector/README.md)。

重点是解释器与包环境、明确输入输出、异常、CLI、锁、测试和打包。达到“源码目录之外也能调用安装后的工具”，而不只是在编辑器里按运行。

## 路线三：为 ROS、视觉与工程编程打基础

先会终端与 P01～P06，再学 P09/P10 → [E05/E06](advanced/engineering/README.md) → T03/T04/E07 → [R01/R02](advanced/workflows/README.md)。

重点是 C++ 接口与库、构建依赖、断点、环境边界和复现。真正 ROS/CV 操作回到各自仓库入口；本课程不会把系统 Python、Miniforge、ROS overlay 和训练环境混在一起。

## 路线四：Linux 系统与远程工作

S01～S06 → T05 → [N01～N06](advanced/systems/README.md) → H04/H06 → [R03](advanced/workflows/03_incident_method/README.md)。

重点是资源、服务、网络层次、SSH 参数、定时任务和增量备份。SSH 与容器实操需要自己的账号或已可用环境；静态配置检查与真实运行分开记录。

## 记录进度

```bash
bash scripts/learn.sh catalog
bash scripts/learn.sh progress
# 开始学一课：
bash scripts/learn.sh record U01 --status learning --note '正在理解发行版和内核'
# 实际完成变式与自检后再记录 done；需要回顾时记录 review
```

进度存在本机仓库的 scripts/runtime/study_progress.json，被 Git 忽略；运行实验不会自动记录完成，也不会修改你的真实进度。正式笔记和作品可放 scripts/exercises/ 并按自己的意愿提交。

推荐一次聚焦一个任务，基础 30～60 分钟，进阶 45～90 分钟。遇到卡点先保留错误，查课程与故障指南，再把问题缩小成一个可验证步骤。
