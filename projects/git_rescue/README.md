# 进阶项目：Git 冲突恢复与回归二分

[项目总览](../README.md) · [E07 课程](../../course/advanced/engineering/07_git_recovery/README.md)

本项目在两个独立示例仓库中练习，不修改主仓库分支，也不推送演示历史。

```bash
bash scripts/advanced.sh lab git
```

conflict-example/ 中两个分支修改同一配置行：先制造冲突，用 merge --abort 恢复，再重做合并并保存双方意图。bisect-example/ 有 0～4 五版，其中 3、4 为坏版本；探针检查 value.txt，bisect 找到第 3 版后结束二分状态。

## 自己扩展

新建自己的示例仓库，让一方新增参数、另一方改默认值。先解释共同祖先和最终行为，再合并。设计一个需要跳过的提交，了解 bisect 探针状态 125 的用途。

## 完成标准

保留冲突证据、恢复前后状态、解决后的差异和中文提交；二分结束后状态干净；说明探针为何可重复。不要只删除冲突标记，也不要用强推覆盖未知远端历史。
