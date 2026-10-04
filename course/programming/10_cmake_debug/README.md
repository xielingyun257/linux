# P10：CMake、构建目录与调试信息

[课程总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../09_cpp_compilation/README.md) · [下一课](../../tools/01_editors/README.md)

## 学习目标

解释 CMake 配置与构建两个阶段，找到生成的程序。

## 先理解

CMake 读取 CMakeLists.txt 生成构建规则，再由 make 等后端调用编译器。源码目录与构建目录分开，避免生成文件混入源码。Debug 构建通常便于调试，不等于程序已经正确。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
bash scripts/study.sh cpp cmake
cat scripts/programming/cpp/CMakeLists.txt
gdb --version | head -n 1
# 手动调试：gdb 本次实验目录/build/angle
# 在 gdb 输入：break main；run 30；next；print argc；quit
```

## 观察与完成标准

能看到配置、编译和运行三个阶段；build/angle 输出相同换算结果。gdb 交互步骤需在自己的终端完成，自动验收没有宣称已验证桌面调试。

## 自己动手

在自己的新源码中增加打印，重新构建，说明配置文件变化和源文件变化分别可能触发什么步骤。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

改用另一编译器或环境时，不应复用含旧缓存的构建目录。CMake 不是 C++ 编译器；cmake --build 不会自动运行生成程序。

## 自检

1. -S 与 -B 各指定什么？
2. CMakeCache.txt 属于源码吗？

<details>
<summary>完成后查看参考答案</summary>

1. 源码目录与构建目录。
2. 不属于，它是配置阶段的生成文件。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../docs/RESOURCES.md)。
