# R03：故障排查：证据、假设与最小改动

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../02_reproducibility/README.md) · [下一课](../04_capstone/README.md)

## 前置知识

[S03](../../../lessons/system/03_process_jobs/README.md)、[S05](../../../lessons/system/05_network_ssh/README.md)、[H05](../../shell/05_cli_contract/README.md)、[N03](../../systems/03_http_diagnosis/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

从失败现象提出可验证假设，每次只改变相关条件。

## 原理与步骤

1. 输入不存在时，记录状态 2 与完整错误。
2. 同一合法数据在阈值 0.2 下返回 4。
3. 将阈值改为 0.5 后返回 0，保留三次命令与报告。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab incident
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `incident` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

区分输入问题、巡检超限和规则通过。改变阈值只改变判定规则，没有修复日志里的错误；不能把“变成 0”冒充根因解决。

## 变式练习

给自己的工具制造表头错误，再写“现象→证据→假设→验证→结果→下一步”。每次只改变一个条件，并说明何时应回到原配置。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

异常等级与根因不是同一概念。重装、全局改环境或提高权限会引入新变量，先用更小的检查缩小范围。

## 自检

1. 非零退出必然表示代码缺陷吗？
2. 放宽阈值修复了什么？

<details>
<summary>完成后查看参考答案</summary>

1. 不必，也可能是输入或业务判定。
2. 只改变接受规则，未消除实际错误。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
