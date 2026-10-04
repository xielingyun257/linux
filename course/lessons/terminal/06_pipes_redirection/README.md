# C06：管道、标准输出与错误输出

[课程总览](../../../README.md) · [理论补充](THEORY.md) · [上一课](../05_search_find/README.md) · [下一课](../07_environment_paths/README.md)

## 学习目标

将多个命令组合成流程，并分别保存结果和错误。

## 先理解

文件描述符 0、1、2 通常对应标准输入、标准输出、标准错误。| 默认只把前一条的标准输出传给下一条的标准输入。2> 保存错误，> 保存结果，tee 同时显示与写文件。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
mkdir -p scripts/practice/pipes
printf 'INFO start\nERROR camera\nERROR camera\nERROR network\n' > scripts/practice/pipes/events.log
grep '^ERROR' scripts/practice/pipes/events.log | cut -d ' ' -f 2 | sort | uniq -c
ls scripts/practice/pipes/not-created > scripts/practice/pipes/out.txt 2> scripts/practice/pipes/err.txt
cat scripts/practice/pipes/err.txt
bash scripts/study.sh demo text
```

## 观察与完成标准

统计结果是 camera 2 次、network 1 次。指定不存在路径的 ls 故意失败，错误进入 err.txt，out.txt 没有正常列表。

## 自己动手

把错误统计保存到 summary.txt，同时在屏幕显示；解释 uniq -c 前为什么需要 sort。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

2>&1 与 > 的先后次序影响流向；管道默认状态通常来自最后一个命令，自动脚本可用 set -o pipefail。

## 自检

1. | 会默认传递标准错误吗？
2. uniq 能合并不相邻的重复行吗？

<details>
<summary>完成后查看参考答案</summary>

1. 不会。
2. 不能，先排序才能把相同项放在一起。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../../docs/RESOURCES.md)。
