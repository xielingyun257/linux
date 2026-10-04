# 进阶项目：可恢复、可重跑的实验包

[项目总览](../README.md) · [R02 课程](../../course/advanced/workflows/02_reproducibility/README.md) · [实验源码](../../scripts/advanced/experiment.py)

一次结果需要同时保留输入、参数、源码、命令、环境与输出。本项目用标准库随机数生成器，方便把复现问题拆成小步骤。

```bash
bash scripts/advanced.sh lab reproduce
```

本次目录包含 bundle/、experiment.tar.gz 和 restored/。参数为 seed=71、count=10。manifest.json 保存 Python 版本、命令和源码/参数/结果 SHA-256；恢复后核对摘要，并执行 copied experiment.py 生成 replayed.json。

## 自己扩展

另建程序，增加一个统计量。先保存新的输入、源码和输出，再换目录重跑。随后换种子验证结果变化，只换输出格式验证“数值相同”和“字节相同”不是同一判断。

## 完成标准

恢复文件的摘要一致，重跑结果符合预期；明确已验证同环境，而未保证跨 Python 版本、硬件或 GPU 算法一致。项目包不包含整个运行环境，跨机器复现要另记录兼容依赖。
