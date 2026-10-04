# P05：模块、import 与对象的入口

[课程总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../04_functions/README.md) · [下一课](../06_files_errors/README.md)

## 学习目标

把算法与入口分开，区分函数、模块、包和对象。

## 先理解

一个 .py 文件通常可作为模块导入；包组织多个模块。main.py 调用 converter.py 中的函数。对象把状态和操作关联起来，列表、路径也是对象；不必先创建复杂类才能理解对象。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
bash scripts/study.sh python modules
cat scripts/programming/python/modules/converter.py
cat scripts/programming/python/modules/main.py
/usr/bin/python3 -c 'from pathlib import Path; p=Path("scripts"); print(p.name, p.exists())'
```

## 观察与完成标准

30 度约等于 0.523599 弧度；Path 对象的 name 为 scripts，exists() 返回 True。导入 converter 不会自己启动实验。

## 自己动手

在自己的新目录建立 unit_converter.py 和 main.py；前者定义 mm_to_m，后者导入调用。解释为何文件名不要叫 json.py。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

模块名可能遮蔽标准库；执行入口与被导入时的 __name__ 不同。包、apt 包与 Python 虚拟环境不是同一层。

## 自检

1. if __name__ == "__main__" 的作用？
2. Path("scripts").exists() 是函数还是对象方法调用？

<details>
<summary>完成后查看参考答案</summary>

1. 直接执行文件时运行入口，被导入时不自动执行该块。
2. 对象方法调用。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../docs/RESOURCES.md)。
