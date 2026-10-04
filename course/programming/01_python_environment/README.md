# P01：Python、解释器、venv 与 Miniforge

[课程总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../../lessons/system/06_storage_mounts/README.md) · [下一课](../02_variables_containers/README.md)

## 学习目标

明确自己运行哪套 Python，创建仓库内的学习虚拟环境。

## 先理解

Python 文件是源代码，解释器负责执行；包安装到某个解释器的环境。venv 有独立包目录；--system-site-packages 允许读取系统包，降低与 Ubuntu/ROS 依赖的隔阂，但它不等于完全与系统隔离。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
command -v python3
/usr/bin/python3 --version
mkdir -p scripts/runtime
/usr/bin/python3 -m venv --system-site-packages scripts/runtime/venv
scripts/runtime/venv/bin/python -c 'import sys; print(sys.executable); print(sys.prefix); print(sys.base_prefix)'
scripts/runtime/venv/bin/python -m pip --version
bash scripts/study.sh environment
```

## 观察与完成标准

venv 的 sys.prefix 在仓库内，sys.base_prefix 指向系统环境。本机默认 python3 来自 Miniforge；study.sh 明确使用系统 Python。无需 pip 安装即可完成本课程。

## 自己动手

用系统解释器和 venv 解释器分别打印 sys.executable，写出安装包时应使用哪个 python -m pip。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

source 激活并非必要，可直接调用 venv/bin/python。不要混用 Miniforge 的 pip 与系统解释器；ROS 构建继续遵循 ROS 仓库入口。

## 自检

1. --system-site-packages 是否只读取 venv 包？
2. python -m pip 有什么好处？

<details>
<summary>完成后查看参考答案</summary>

1. 不是，还允许系统包参与搜索。
2. 明确 pip 属于所指定的解释器。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../docs/RESOURCES.md)。
