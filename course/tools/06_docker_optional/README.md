# T06：Docker 镜像、容器与挂载（选修）

[课程总览](../../README.md) · [理论补充](THEORY.md) · [上一课](../05_tmux/README.md)

## 学习目标

理解容器的环境边界，读懂一个最小 docker run 命令。

## 先理解

镜像提供文件系统和启动配置，容器是镜像的一次运行。容器共享宿主机内核，不能等同于完整虚拟机。挂载把宿主机目录提供给容器；:ro 表示只读。本课不依赖 Docker 完成主线。

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
docker --version
docker context show
# 以下手动实验需 Docker daemon 可用，并会下载镜像：
# mkdir -p scripts/practice/docker
# printf 'hello\n' > scripts/practice/docker/note.txt
# docker run --rm --mount "type=bind,src=$PWD/scripts/practice/docker,dst=/lesson,readonly" python:3.10-slim python -c 'from pathlib import Path; print(Path("/lesson/note.txt").read_text())'
# 更严格复现应记录实际镜像 digest，标签本身可能变化
```

## 观察与完成标准

客户端版本可查询，但这不证明 daemon 可用。手动示例应打印 hello，容器退出后 --rm 清理容器，宿主机 note.txt 保留；本次自动验收不下载镜像。

## 自己动手

画出宿主机路径与容器 /lesson 的映射；解释镜像、容器、挂载目录各在哪里，以及只读限制作用于谁。

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

docker 组通常提供很高的主机权限，不为完成课程自动改用户组。--rm 不删除下载的镜像；镜像标签可能随时间更新。

## 自检

1. 容器有自己的 Linux 内核吗？
2. --rm 会删除绑定挂载的宿主文件吗？

<details>
<summary>完成后查看参考答案</summary>

1. 通常共享宿主内核。
2. 不会，它清理退出后的容器对象。

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明](../../../docs/RESOURCES.md)。

<!-- advanced-transition -->

基础工具课之后，可进入[进阶系列](../../advanced/README.md)，或按[目标路线](../../START_HERE.md)选择下一步。
