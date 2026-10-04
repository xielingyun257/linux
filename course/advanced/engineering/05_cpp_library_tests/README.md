# E05：C++ 库目标、接口与 CTest

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../04_concurrency/README.md) · [下一课](../06_debug_sanitizer/README.md)

## 前置知识

[P09](../../../programming/09_cpp_compilation/README.md)、[P10](../../../programming/10_cmake_debug/README.md)、[E02](../02_unittest/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

把头文件、实现、程序与测试组织成工程目标。

## 原理与步骤

1. units.hpp 声明接口，units.cpp 实现换算。
2. main.cpp 与 test_units.cpp 分别链接 units 库。
3. CMake 定义依赖，CTest 执行数值检查。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab cpp
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `cpp` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

Debug 构建成功，angle_conversion 测试通过；30 度输出约 0.523599。测试含 0 和 30 度，不用终端显示格式作为数学真值。

## 变式练习

另建自己的工程，增加 radians_to_degrees 及负角度测试；故意改错公式，确认 CTest 失败，再修复。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

头文件声明不等于实现已被链接。生成文件留在独立 build 目录，不能把旧二进制当作新源码结果。

## 自检

1. target_link_libraries 做什么？
2. 构建成功等于测试通过吗？

<details>
<summary>完成后查看参考答案</summary>

1. 声明程序与库的链接依赖。
2. 不等于，还需实际执行测试。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
