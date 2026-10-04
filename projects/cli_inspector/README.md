# 进阶项目：参数化日志巡检工具

[项目总览](../README.md) · [R04 综合课](../../course/advanced/workflows/04_capstone/README.md) · [工具源码](../../scripts/advanced/log_cli.py)

目标是把解析、模型、统计、判定和结果留存连起来。CSV 含 timestamp、level、component、duration_ms 四列；坏记录单独保存，错误率只使用合法记录作分母。

```bash
bash scripts/advanced.sh lab capstone
/usr/bin/python3 -E -s scripts/advanced/log_cli.py --help
```

教学输入有 8 条合法记录与 1 条坏记录，错误率为 0.375。阈值 0.5 返回 0，0.2 返回 4；输出归档中的报告与原件字节一致。报告存在时拒绝覆盖并返回 2，strict 模式遇坏记录为 3，没有合法记录为 5。

## 自己扩展

另建新项目，在组件筛选、耗时阈值、文本摘要中选一项实现。先定义输入和输出规则，再写边界测试。空输入与坏记录要能解释，不以放宽阈值或丢弃记录假装修复问题。

## 完成标准

给出正常、缺文件、坏格式、空数据、超限五类例子；解释各状态；证明旧输出未被覆盖；保存输入、报告、实际命令和归档。最后用新的数据运行，检查手算预期。
