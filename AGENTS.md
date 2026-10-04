# Linux 学习仓库协作约定

- 全程中文沟通，Git 提交信息用中文。
- 新任务先读 README、课程入口、相关全局记忆；提出计划，经用户确认后执行。已经确认的范围持续有效，不重复询问。
- 本轮用户已确认建设 36 节 Ubuntu/Linux 课程、示例、项目和验证，并授权向 https://github.com/xielingyun257/linux.git 提交与推送。
- 主环境为 Ubuntu 22.04；课程入口固定系统 /usr/bin/python3 3.10。本机默认 Python 来自 Miniforge，不能隐式混用。
- 不修改任务开始前已有的源文件。新增代码全部在根目录 scripts/ 下；课程与说明文档可以更新。自己的练习另建文件，不覆盖课程示例。
- 原始材料、备份、虚拟环境、构建、临时文件和输出全部在仓库内。全局记忆按专门约定保存在 ~/.Codex/memory/，本仓库 scripts/memory 链接过去。
- 主课程仅依赖系统工具与 Python 标准库；若增加依赖，先写清用途与路径，优先仓库内 venv（--system-site-packages）。不要为本课程替换系统 Python 链接或写用户全局 Shell 配置。
- 实质改动前先跑热身，输出环境与依赖路径。验证检查实际结果，而不只判断命令能退出。
- 每次自动实验生成独立 scripts/runs/ 目录。进程、HTTP 服务和 tmux 只创建并清理自己的资源，不按名字全局杀进程。
- 本项目不启动 ROS 仿真。若后续涉及 ROS，按用户规则先识别并清理属于本任务的残留，遵循 ROS 仓库入口与版本隔离约定。
- 自动验收不改变系统服务、软件源、磁盘分区和用户组，不启动 Docker daemon；这些是课程中明确标注的手动练习。
- NTFS 权限与链接按实际挂载观测，不以 ext4 常规行为冒充本机实测。
- 文档构建器 scripts/build_course_docs.py 维护 36 节正文和导航。改动正文后同步操作页、理论页与清单；运行 scripts/validate_course.py 检查完整性和本地链接。
- 完成代码改动后执行相关验证、git add、中文 git commit、git push；只提交本任务文件，不混入无关修改。不得猜测用户身份、覆盖远端历史或强推。
- 阶段经验存全局记忆，标注 category: rule 或 category: guidance；文档明确区分已自动验证和待手动操作。
