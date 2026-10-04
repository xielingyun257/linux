# P04：函数、参数、返回值与作用域

[课程总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../03_control_flow/README.md) · [下一课](../05_modules_objects/README.md)

## 学习目标

把重复逻辑写成函数，区分打印与返回。

## 先理解

函数为一个有名字的计算步骤定义输入与输出。参数在调用时取得值，return 把结果交给调用者；print 只是显示。局部变量通常只在函数作用域内可见。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
bash scripts/study.sh python functions
grep -n -A 5 '^def mean' scripts/programming/python/examples.py
# 在自己的练习文件里定义并调用 mean，不改原示例
```

## 观察与完成标准

mean([10,20,30]) 返回 20.0，结果被写入 JSON。空列表在求和前被检查，避免以零为除数。

## 自己动手

新建一个 mm_to_m(value) 函数，输入 250 返回 0.25；调用两次并说明参数、返回值和局部变量。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

只 print 而未 return 的函数通常返回 None。默认参数如果使用可变列表，会在多次调用间共享对象。

## 自检

1. print(结果) 可以替代 return 吗？
2. mean([]) 应怎么办？

<details>
<summary>完成后查看参考答案</summary>

1. 不能，显示和返回用途不同。
2. 明确拒绝空输入或设计并说明专门语义。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../docs/RESOURCES.md)。
