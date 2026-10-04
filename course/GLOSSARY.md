# 中英文术语表

[课程总览](README.md)

| 术语 | 含义与例子 |
| --- | --- |
| Linux kernel / 内核 | 管理进程、内存和设备的核心软件，不等于整个 Ubuntu |
| Distribution / 发行版 | 内核、软件包和工具的组合，如 Ubuntu |
| Desktop environment / 桌面环境 | 图形交互与窗口组织，如 GNOME |
| Terminal / 终端 | 显示输入输出的界面；可运行 Shell，也可运行其他程序 |
| Shell / 命令解释器 | 解析命令并启动程序，如 Bash |
| Command / 命令 | Shell 内建或程序加上选项、参数形成的操作 |
| Option / 选项 | 改变命令行为，如 ls 的 -a |
| Argument / 参数 | 传给命令的数据，如要查看的路径 |
| Working directory / 工作目录 | 相对路径的起点，用 pwd 查看 |
| Absolute path / 绝对路径 | 从 / 开始的路径 |
| Relative path / 相对路径 | 相对当前目录或特定基准解析的路径 |
| Home directory / 家目录 | 当前用户的个人目录，Shell 中常用 ~ 表示 |
| Root directory / 根目录 | 目录树顶层 /，不同于 root 用户 |
| root user / 超级用户 | 具有广泛系统权限的用户 |
| Mount / 挂载 | 把文件系统接入目录树 |
| Filesystem / 文件系统 | 组织文件和元数据的方式，如 ext4、ntfs3 |
| Symlink / 软链接 | 指向另一个路径，目标移走后可能失效 |
| Permission / 权限 | 读、写、执行及所有者/组/其他用户的规则 |
| sudo | 按策略以另一个用户身份执行命令，常用于管理员操作 |
| Process / 进程 | 程序的一次运行，有 PID |
| Job / 作业 | 当前 Shell 管理的前台或后台任务 |
| Signal / 信号 | 通知进程的机制，如 SIGINT、SIGTERM |
| Service / 服务 | 常由服务管理器管理的后台功能 |
| Unit | systemd 管理资源的配置单元 |
| Standard input/output/error | 标准输入、输出、错误，通常对应 0/1/2 |
| Pipe / 管道 | 将一个命令的标准输出连接到另一个的输入 |
| Redirection / 重定向 | 改变输入输出位置，如 >、2> |
| Exit status / 退出状态 | 0 通常成功，非零需结合命令契约解释 |
| Environment variable / 环境变量 | 子进程启动时可继承的名字和值 |
| PATH | 可执行程序搜索目录的顺序列表 |
| Interpreter / 解释器 | 执行源代码的程序，如 Python |
| Module / 模块 | 可导入的代码单元，如一个 .py 文件 |
| Package / 包 | Python 中组织模块；系统包则是另一层分发单位 |
| venv / 虚拟环境 | 分隔 Python 包安装位置与解释器入口 |
| Function / 函数 | 有明确输入与返回值的计算步骤 |
| Object / 对象 | 具有数据与行为的实体，如 Path 实例 |
| Exception / 异常 | 程序用来表达异常情况的机制 |
| Compiler / 编译器 | 将源码转换成目标代码，如 g++ |
| Linker / 链接器 | 将目标代码与库组成程序或库 |
| Build / 构建 | 配置、生成规则、编译和链接等过程 |
| Debugger / 调试器 | 用断点、单步和变量观察检查执行 |
| Repository / 仓库 | 文件及其版本历史的工作单元 |
| Staging area / 暂存区 | 准备提交的快照，不是远端 |
| Commit / 提交 | 一个本地版本记录 |
| Branch / 分支 | 指向提交的可移动名字 |
| Remote / 远端 | 与本地交换历史的另一个仓库 |
| IP address / IP 地址 | 网络层定位接口的地址 |
| Port / 端口 | 区分同一地址上的不同服务 |
| DNS | 将域名等名称解析为地址的系统 |
| SSH | 加密远程登录与命令执行协议 |
| Archive / 归档 | 把多个路径打包，不必同时压缩 |
| Checksum / 校验值 | 用于比较内容的摘要，不能单独证明可信来源 |
| Image / 镜像 | Docker 中的文件系统与启动配置模板 |
| Container / 容器 | 镜像的一次运行，通常共享宿主内核 |

遇到相同词在不同工具中含义不同，先确定层级：系统包、Python 包、Git 仓库和 ROS 工作区不是同一对象。
