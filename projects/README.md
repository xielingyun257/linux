# 综合练习

项目文档在这里，基础源码放 scripts/projects/，进阶源码放 scripts/advanced/ 并通过独立入口运行。输入是自动生成的教学资料，每次运行用新的输出目录；不用自己的重要文件试跑。

| 项目 | 前置知识 | 核心完成标准 |
| --- | --- | --- |
| [资料整理与备份](organize/README.md) | 路径、文件、归档、文件读写 | 原件保留，3 个文件恢复校验一致 |
| [日志分析](logs/README.md) | 搜索、管道、循环、结构化文本 | 8 条合法记录、3 条错误、1 条格式问题 |
| [平均值程序调试](debug/README.md) | 函数、异常、断点 | 解释 11 与 11.75 差异，空输入明确报错 |
| [参数化日志巡检](cli_inspector/README.md) | H05、E01/E02、R04 | 正常、超限、坏记录与空输入状态明确 |
| [可复现实验包](reproducible_run/README.md) | R02、C08、P06 | 摘要、归档恢复、同环境重跑一致 |
| [Git 故障恢复](git_rescue/README.md) | T03/T04、E07 | 冲突恢复、语义合并、首个坏提交定位 |

基础源码保留在 scripts/projects/；进阶项目复用 scripts/advanced/ 和独立 advanced_lab.py，不修改原有项目源码。

先预测，再运行；阅读对应脚本，最后在 scripts/ 下另建自己的变式程序。可用[学习模板](../scripts/templates/study_record.md)记录。
