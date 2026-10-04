# E06：gdb、调用栈与 AddressSanitizer

[进阶总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../05_cpp_library_tests/README.md) · [下一课](../07_git_recovery/README.md)

## 前置知识

[P10](../../../programming/10_cmake_debug/README.md)、[E05](../05_cpp_library_tests/README.md)。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

区别编译、逻辑和内存错误，使用断点与运行时诊断定位。

## 原理与步骤

1. Debug 构建供 gdb 在 main 断点观察 argc。
2. 单独编译故意越界的 bounds_error.cpp，启用 AddressSanitizer。
3. 保存错误报告，找到访问位置与分配范围。

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab debugging
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码](../../../../scripts/advanced_lab.py)中定位 `debugging` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

支持 ptrace 的环境会记录 argc=2；否则明确保留限制。越界进程应非零退出，asan.txt 包含 heap-buffer-overflow；它是预期失败，不是课程验收失败。

## 变式练习

阅读调用栈找到源码行，在自己的新文件用合法索引或 at() 改写，再比较结果。不要通过屏蔽诊断掩盖访问越界。

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

优化可能使变量被消除；sanitizer 改变开销与运行布局。一次未报错不能证明不存在其他内存问题。

## 自检

1. -g 与 -fsanitize=address 分别作用？
2. 堆越界为什么不能靠“程序能退出”判断？

<details>
<summary>完成后查看参考答案</summary>

1. 调试信息与运行时内存诊断。
2. 未定义行为可能正常结束也可能崩溃。

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明](../../../../docs/ADVANCED_RESOURCES.md)。
