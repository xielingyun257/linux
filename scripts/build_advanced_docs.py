"""进阶课程的独立正文、理论与 60 节总导航；不改基础生成器。"""
import inspect
import json
import os
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
GROUPS={'shell':('H','Bash 与文本处理'), 'systems':('N','系统与网络进阶'),
        'engineering':('E','程序工程与开发工具'), 'workflows':('R','复现与故障排查')}
LESSONS=[]


def add(group,slug,title,prerequisites,lab,goal,steps,expected,exercise,pitfalls,quiz,answer,theory):
    LESSONS.append(dict(group=group,slug=slug,title=title,prerequisites=prerequisites.split(','),lab=lab,
                        goal=goal,steps=steps,expected=expected,exercise=exercise,pitfalls=pitfalls,
                        quiz=quiz,answer=answer,theory=inspect.cleandoc(theory)))


add('shell','01_quoting','引号、展开与参数边界','C01,C02,C07,P07','quoting',
    '解释 Shell 在启动程序前怎样处理变量、空格和通配符，避免把一个路径传成多个参数。',
    '1. 单引号保留字面字符；双引号允许变量展开但保留空格。\n2. 裸 *.txt 由 Shell 匹配路径，"*.txt" 是一个字面参数。\n3. 先判断参数数目，再解释目标程序得到什么。',
    '三行输出依次是 two words、one.txt、*.txt。实验只创建自己的 one.txt；命令日志保留实际传入参数。',
    '另建脚本，用 set -- "$value" 和 set -- $value 对照 $#；令 value="two words"，预测参数数量分别为 1 与 2。再增加匹配文件，预测通配符结果。',
    '引号是 Shell 语法，通常不会成为程序收到的字符；字符串中的路径并不会自动检查是否存在。',
    '1. 为什么 "$value" 与 $value 不一样？\n2. 程序收到引号本身吗？',
    '1. 未加引号可能发生分词和通配符展开。\n2. 用于分组的语法引号会被 Shell 去掉。',
    r'''## 展开顺序与可预测性

    参数展开、分词和路径名展开发生在程序启动之前。value='a b' 时，printf '%s\n' "$value" 输出一行，而未加引号可能输出两行。排错不能只看命令在屏幕上的样子，应追踪最终参数。

    ## 参数数组

    "$@" 保留每个位置参数的独立边界，适合把收到的参数传给另一个程序；"$*" 通常把它们拼成一个参数。自己的脚本应采用明确的参数契约，避免把命令字符串拼接后交给 eval。''')

add('shell','02_sed_awk','sed、awk 与结构化文本','C04,C05,C06,P03','text',
    '按行选择、替换和聚合文本，判断什么时候应改用 CSV 解析器。',
    '1. sed 的 s/模式/替换/ 改变输出文本，本实验不使用 -i。\n2. awk -F, 用逗号分字段；NR>1 跳过表头。\n3. 累加第二字段，最后用总和除以合法记录数。',
    '三条值 10、20、30 的均值为 20；sed 输出 beta,20，原文件仍是 b,20。不要把过滤后输出与原输入混淆。',
    '增加一条 d,40，预测均值 25。再加入空值，讨论它是否应计入分母；自己写明处理规则，不默认把所有坏值当零。',
    '简单 -F, 不能完整处理带引号且字段内部有逗号的 CSV；多列真实数据优先用 csv 模块。',
    '1. NR>1 为什么放在这里？\n2. sed 默认会改原文件吗？',
    '1. 跳过表头，避免把列名参与算术。\n2. 不会，默认写标准输出。',
    r'''## awk 的执行模型

    BEGIN 可在读输入前执行，普通规则对匹配的每条记录执行，END 在结束时汇总。$1、$2 是字段，NR 是累计记录号。均值的关键不是公式复杂，而是哪些记录进入 n。

    ## 正则和数据格式

    sed 适合按规则改文本，awk 适合字段与行上的轻量统计。带引号、转义与缺失值的数据需要格式解析；工具选择应依据数据规则，而不是一味追求一行命令。''')

add('shell','03_nul_paths','find、xargs 与复杂文件名','C02,C05,P08','paths',
    '正确处理空格、中文和以连字符开头的文件名，理解 NUL 分隔。',
    '1. find 选择输入路径，-print0 在路径之间写零字节。\n2. xargs -0 按相同分隔约定组合参数。\n3. Python 将实际参数列表保存为 JSON，避免用肉眼猜路径数量。',
    '至少 3 个完整路径，包括“课程 笔记.txt”和“-option.txt”。若当前文件系统允许换行文件名，还验证第四个；否则记录具体限制。',
    '给自己的练习目录增加包含多个空格的文件，预测路径数量。比较普通换行分隔与 NUL 分隔；程序参数中的 -- 可用于结束许多工具的选项解析。',
    '不能解析 ls 输出来可靠遍历文件。Linux 的 Shell 支持某类字符，不代表当前 NTFS 挂载也允许它出现在文件名中。',
    '1. 为什么空格不再拆开路径？\n2. NUL 可以存在于普通文件名中吗？',
    '1. 生产和消费两端使用零字节分隔。\n2. 不可以，因此适合作无歧义分隔。',
    r'''## 两端协议必须一致

    -print0 与 -0 是配对的接口约定。只改一端不能完成正确解析。Shell 通配符、换行分隔文本和参数数组是三种不同的对象，转换时需要保持边界。

    ## xargs 的调用次数

    输入很多时，xargs 会按系统参数长度限制分成多次调用。某些任务不能假定只启动一个进程；有序统计和并行执行应另设汇总规则。课程用少量已知文件验证基本契约。''')

add('shell','04_graceful_exit','退出状态、信号与资源清理','S03,P07,P06','signals',
    '为任务设计可检查的停止过程，区分请求退出与强制结束。',
    '1. 子进程完成准备后写 ready.json，父进程确认 PID。\n2. 父进程发送 SIGTERM，子进程用事件结束循环。\n3. finally 保存 stopped.json，父进程 wait 回收。',
    '子进程状态为 0，clean_exit=true，且已经回收。这个结果来自程序主动处理 SIGTERM，并非所有程序收到信号都返回 0。',
    '在自己的新脚本里用 trap 为 EXIT/INT/TERM 登记清理动作；启动后停止，只清理自己创建的临时资源，并保留一条退出日志。',
    'SIGKILL 无法被捕获。trap 和 finally 不能保证断电后运行；应同时设计可恢复的数据写入方式。',
    '1. ready 标记为什么有用？\n2. wait 负责什么？',
    '1. 避免父进程过早停止尚未初始化的任务。\n2. 等待结束并回收子进程状态。',
    r'''## 生命周期是一种契约

    启动、就绪、运行、停止、回收应各有明确证据。PID 存在只是中间状态，不能代替就绪检查；任务不打印也不能证明它结束。处理信号时避免做复杂、易阻塞的工作，先通知主循环。

    ## Bash 与 Python

    Bash 用 trap 注册动作，Python 用 signal 接收信号、finally 释放资源。后台子任务仍由父进程跟踪；退出清理应限定到自己登记的资源，避免按名字结束其他学习项目。''')

add('shell','05_cli_contract','参数化命令行工具与机器可读报告','P04,P05,P06,C06','cli',
    '将一次性脚本改成有明确参数、输入检查、报告格式和退出状态的工具。',
    '1. argparse 明确 --input、--output、--strict 与阈值。\n2. CSV 用 Event 模型逐行校验，坏记录另列。\n3. 报告落盘后，用状态 3 表达严格格式检查失败，4 表达错误率超限；路径或覆盖问题是 2。',
    '合法 8 条，错误率 3/8=0.375，平均耗时 45 ms，坏记录 1 条。四种运行验证正常、格式问题、阈值超限与拒绝覆盖；已有报告字节不变。',
    '查看 log_cli.py 的 --help。复制为自己的工具，增加一个筛选组件参数；明确错误率分母是在筛选前还是筛选后，并设计输入。',
    '非零状态也可能是预期的巡检结论，报告仍会生成。不要把“没有记录”当错误率 0；本工具返回 null，并以状态 5 表达无合法数据。',
    '1. --strict 的失败状态是什么？\n2. 已有输出为什么拒绝覆盖？',
    '1. 3。\n2. 保留可审查的既有结果，调用者需指定新文件。',
    r'''## 数据与控制分开

    JSON 用于保存数据，退出状态用于上层调度。0 表示按当前检查规则通过；2 表示输入输出问题；3 表示严格模式发现坏记录；4 表示阈值超限。调度器应解释状态而不是把所有非零值归成同一种故障。

    ## 分母与缺失值

    错误率只在合法记录上计算，本例是 3/8，不是 3/9。格式错误必须同时报告；若没有合法记录，错误率未知，以 null 表达。阈值允许 0～1，超过范围应在执行前拒绝。''')

add('shell','06_lock_atomic','文件锁、原子替换与重复运行','P08,S03,C03','atomic',
    '理解多个进程写同一文件的竞争，以及完整报告如何对读者可见。',
    '1. 两个进程各执行 20 次“读→加一→写”。\n2. 对稳定的 counter.lock 使用排他锁，覆盖整段操作。\n3. 在同目录写临时文件，再 os.replace 替换计数文件。',
    '最终计数 40，两个进程均退出，没有残留 counter-*.tmp。锁只约束遵守同一锁协议的写者。',
    '另建自己的程序，增加第三个进程，预测 60；解释为什么锁住临时文件而不是稳定锁文件可能失效。',
    '原子替换让读者看到完整文件，但单独使用它仍会丢失并发更新。原子可见性也不等于断电后的持久性。',
    '1. 为什么锁覆盖读和写？\n2. 临时文件为什么放同一文件系统？',
    '1. 避免两个写者读到同一旧值。\n2. 跨文件系统无法使用相同的原子重命名语义。',
    r'''## 两个不同的问题

    读到半份 JSON 是可见性问题，两个增量互相覆盖是并发更新问题。临时文件加原子替换处理前者；稳定文件上的互斥锁处理后者。完整“读改写”事务都要持锁。

    ## 持久性与幂等性

    真正需要断电保证时还要考虑文件和目录 fsync、文件系统与存储设备语义。幂等操作重复执行应有同一业务效果；累加计数本身不是幂等，重试前必须判断该操作是否已经完成。''')

add('systems','01_proc_limits','/proc、资源上限与观察范围','S03,S06','proc',
    '用只读证据区分 CPU、内存、文件描述符和资源上限。',
    '1. /proc/self 指读取者自己，不是整个系统。\n2. status 中 Threads、VmRSS 反映不同资源。\n3. resource.getrlimit 返回软/硬上限；本课只读，不修改限制。',
    '报告保存本次 PID、线程数、驻留内存和文件描述符上限。具体数值随运行变化，不要求与课本或别人电脑一致。',
    '结合 ps、free、df 和本报告，各选一项解释统计对象与单位。另开终端读 /proc/self/status，说明它为什么可能不是 Python 进程。',
    'VSZ 不等于实际驻留内存。/proc 中信息会随进程变化或消失；已退出的 PID 可能被复用。',
    '1. /proc/self 中的 self 指谁？\n2. 软上限和当前占用是一回事吗？',
    '1. 当前读取该路径的进程。\n2. 不是，上限是可使用边界，占用是当前量。',
    r'''## 快照与动态状态

    /proc 是内核提供的虚拟信息接口。多次读取不同文件并不是对全系统的原子快照；同一进程的状态可能在读取期间改变。记录时间、对象和单位，避免拼成不存在的瞬间状态。

    ## 资源分类

    驻留内存、虚拟地址空间、打开文件和 CPU 时间分别描述不同对象。Linux 下 ru_maxrss 通常以 KiB 表示峰值，VmRSS 描述当时驻留量。资源上限造成的失败与物理内存耗尽也应分开定位。''')

add('systems','02_performance_strace','性能测量、复杂度与 strace','P03,S03,C04','timing',
    '在正确结果的基础上测量，区分算法耗时与系统调用观察。',
    '1. 对同一输入比较重复扫描和预先计数，两者结果应一致。\n2. perf_counter 记录三次时长，保存原值而不只说“更快”。\n3. strace -c 汇总自己的短进程系统调用，输出留在实验目录。',
    '两种算法结果相同，报告列三次耗时；strace 若可用生成汇总，否则保留原因。速度比随机器与负载变化，课程不规定固定倍率。',
    '另建程序，把输入量扩大两倍再测；解释线性和平方增长的预期。先验证数值相同，再比较时间，避免用错误算法换速度。',
    '一次测量会受调度、缓存与初始化影响。strace 会扰动程序，它不等于没有开销的性能基准。',
    '1. 比较速度之前先检查什么？\n2. strace 主要看哪一层？',
    '1. 输入与计算结果一致。\n2. 程序与内核之间的系统调用。',
    r'''## 公平比较

    重复 count 对每个元素重新扫描，工作量约 O(n²)；Counter 先一次计数，再按表查询，通常约 O(n)。本例比较的是相同的“频数之和”，不是两种不同答案。

    ## 定位瓶颈

    墙钟时间、CPU 时间和等待时间不是同一指标。算法占 CPU 可以先看复杂度；大量文件读写或网络等待可用系统调用信息缩小范围。保存数据量、环境与多次测量，避免把单次结果推广成普遍结论。''')

add('systems','03_http_diagnosis','HTTP 状态、curl 与分层网络排错','S05,C06','http',
    '区分连接故障、HTTP 返回失败和应用数据错误。',
    '1. 本机临时服务提供 /health、/missing、/protected。\n2. curl -f 把 HTTP 400 及以上响应作为失败。\n3. 同时看状态、正文和退出值，结束时关闭服务器。',
    '/health 返回 200 且正文正确；404 和 401 在 curl -f 下返回 22。全部监听 127.0.0.1，测试后线程关闭，不证明外网可达。',
    '在自己的新服务器中加 /slow 路由，用 curl --max-time 设置等待上限。把超时、401、404 分别写成不同诊断，不把它们都称为网络断了。',
    '未用 -f 时，curl 能成功收到 404 响应并返回 0；HTTP 状态与命令状态不能简单等同。',
    '1. 401 通常属于哪层问题？\n2. HTTP 200 足以验证内容吗？',
    '1. 协议上的认证要求，连接已经建立。\n2. 不够，还需内容与业务规则检查。',
    r'''## 从连接到业务

    先验证地址与路由，再看端口是否监听，再确认 TLS/HTTP 协议与认证，最后验证数据。连接拒绝常是无监听或被拒绝；收到 HTTP 错误说明已经到达某个 HTTP 服务，但不证明到达了期望服务。

    ## 重试条件

    401 通常需要认证信息，404 需要核对路径，瞬时超时可能适合有限重试。对会产生副作用的请求，重试前必须了解幂等性。本课只请求自己的只读教学接口。''')

add('systems','04_ssh_config','SSH 配置、密钥与端口转发','S05,C07','ssh-config',
    '用独立配置文件表达连接参数，理解本地端口转发的实际位置。',
    '1. Host 是别名，HostName 是目标地址，Port 是目标 SSH 端口。\n2. ssh -G -F 配置 别名 展示解析后的参数，不发起连接。\n3. LocalForward 的本地监听端与远端连接目标分别写明。',
    '解析结果使用 127.0.0.1、端口 2222 和示例用户 student。配置放本次实验目录；未创建密钥、修改全局配置或登录服务器。',
    '给自己的配置副本增加另一个别名，用 -G 比较结果。拥有服务器后再练习 ssh -p 与 scp -P；记录主机指纹与实际连接路径。',
    '隧道里的远端 127.0.0.1 指远程机器。私钥不能作为课程素材提交，公钥与私钥用途不同。',
    '1. -G 会验证远端密码吗？\n2. 本地 9000 端口与 SSH 2222 端口是同一个吗？',
    '1. 不会，只计算配置。\n2. 不是，分别是隧道监听与 SSH 连接端口。',
    r'''## 本地转发的路径

    -L 127.0.0.1:9000:127.0.0.1:8000 表示本机 9000 接收请求，经 SSH 连接让远端访问远端自己的 8000。转发成功还依赖 SSH 连接、权限与目标服务，本课只验证静态参数。

    ## 认证与可用性

    用户认证确认你是谁，主机密钥确认连接的是谁；ServerAliveInterval 检测连接存活，不保证远端应用正常。把配置、认证、通信和业务健康分别验证。''')

add('systems','05_user_timers','systemd unit、用户服务与定时器','S04,P07,H05','systemd',
    '读懂 oneshot 服务与 calendar 定时器，并在启用前检查语法。',
    '1. service 描述命令，timer 描述何时触发相应 unit。\n2. systemd-analyze verify 检查文件，calendar 解析 hourly。\n3. ExecStart 不是默认交给 Shell 的字符串，管道需显式解释器。',
    '两个 unit 静态验证通过，hourly 显示未来两次时间。实验仅在仓库内生成文件，没有安装、启用或启动系统或用户服务。',
    '修改自己的 timer 副本为每天 20:00，用 systemd-analyze calendar 预测下次时间；解释时区与 Persistent 的意义。真实部署作为后续手动练习。',
    'enable 与 start 不同；用户服务还取决于用户会话生命周期。Persistent 主要服务于日历触发的补执行，不代表每一次遗漏都补跑。',
    '1. timer 与 service 分工是什么？\n2. verify 通过代表任务真的跑过吗？',
    '1. 定义触发时间与定义执行动作。\n2. 不代表，还需启用、执行和日志证据。',
    r'''## 调度不代替结果检查

    定时器触发后，服务仍可能因路径、环境或输入失败。为任务明确 WorkingDirectory、解释器、输出与退出状态，运行后查 journal。完整路径减少对交互 Shell 配置的隐式依赖。

    ## 时间与会话

    OnCalendar 使用日历表达式，OnActiveSec 等采用相对时间。用户 manager 与系统 manager 作用范围不同；注销后是否运行需另核对，不能仅根据 unit 文件推断。''')

add('systems','06_incremental_backup','rsync、增量快照与恢复','C08,S06,H06','backup',
    '保留多个资料版本，理解 --link-dest、校验比较与硬链接约束。',
    '1. 先复制版本 1 的文件形成 snapshot1。\n2. 修改源内容并增加文件，用 --checksum 和 --link-dest 生成 snapshot2。\n3. 检查旧内容仍在，再观察未变文件的 inode 是否共享。',
    'snapshot1 保留 version 1，snapshot2 保存 version 2 和新文件。报告记录 unchanged_hardlink 的实际值，不凭文件名断定硬链接已生效。',
    '从第一份快照恢复到新的目录并核对内容。解释为什么不能直接修改快照中共享硬链接的文件；设计保留周期，先只列候选，不自动删除。',
    '大小和时间相同不保证内容相同，本实验专门用 --checksum。共享 inode 的快照不是独立介质备份，也不能被原地编辑。',
    '1. 源目录末尾 / 表示什么？\n2. --link-dest 为什么节省空间？',
    '1. 复制目录内容。\n2. 条件满足时对未变文件使用硬链接，而非重写完整数据。',
    r'''## 比较规则与成本

    rsync 默认快速检查常参考大小和时间，--checksum 会读取内容计算摘要，增加 I/O。本例版本 1 和 2 长度相同，快速修改可能保留近似时间，因此显式校验避免错判。

    ## 快照不等于隔离副本

    --link-dest 需要相关文件系统和属性支持，未变文件可共享 inode。通过新路径替换改变的文件，旧版本才保留；直接改共享文件会影响多份快照。恢复测试和独立备份位置仍是必要的完成标准。''')

add('engineering','01_models_types','类、dataclass、类型提示与数据模型','P04,P05,P06','objects',
    '把校验后的数据组织成对象，区分类型提示与运行时检查。',
    '1. Event 把时间、级别、组件和耗时组织在一起。\n2. from_row 是类方法，负责字符串转换与校验。\n3. frozen 限制通常的字段赋值，asdict 用于生成结构化输出。',
    '耗时字符串 12.5 被转换为浮点数，缺失字段被拒绝。类型提示不会自动检查 CSV，校验来自明确写出的代码。',
    '新建自己的模型，加一个单位明确的字段；设计正常、缺失、负值与非有限数值样例。说明为何仅写 float 类型提示不够。',
    'dataclass 自动生成部分方法，不自动验证业务规则。frozen 是浅层的字段限制，内部可变对象仍需单独考虑。',
    '1. cls 与普通实例 self 的区别？\n2. nan 为什么拒绝？',
    '1. 类方法收到类，实例方法收到对象。\n2. 它不是有限测量值，可能破坏比较和统计。',
    r'''## 对象不只是语法

    一个数据模型声明字段、单位和合法范围，把转换责任集中在边界。CSV 解析后仍是字符串字典，Event.from_row 才产生可以参与计算的记录。构造失败时应说明输入问题。

    ## 接口与责任

    模型负责单条记录，统计函数负责多条记录，CLI 负责路径与退出状态。职责分开后，同一个模型可在终端程序、测试或 ROS 回调中复用，而不绑定某个图形界面。''')

add('engineering','02_unittest','单元测试、边界输入与失败契约','P04,P06,E01,H05','tests',
    '把手工预期写成独立检查，测试结果与错误分支。',
    '1. unittest discover 查找 test_*.py。\n2. 模型测试合法转换、缺失和非法输入。\n3. CLI 测试报告、状态 2/3/4 与拒绝覆盖；空记录不能伪装成零错误率。',
    '10 个测试通过，非法值包含 nan、inf、负数、未知级别等子样例。测试只使用仓库内临时目录，完成后清理自己的测试输入。',
    '给自己模型增加一个字段后，先写一个会失败的预期检查，再实现校验使其通过；保存失败和成功两次记录。',
    '测试应检查用户可见的行为，不只重复实现公式。全部通过只说明已测试场景，不能保证任意输入都正确。',
    '1. 为什么要测试空输入？\n2. assertRaises 在检查什么？',
    '1. 防止无数据被当成正常零值。\n2. 指定情况会产生预期异常。',
    r'''## 选择有意义的边界

    正常输入、最小输入、缺失字段、非法值、现有输出和阈值边界覆盖不同风险。使用 subTest 能把一组非法输入逐项报告；失败时应知道是哪一项条件被违反。

    ## 测试层级

    单元测试检查局部模型或函数，CLI 测试检查参数、文件与退出状态，综合实验验证多步骤协作。速度较快的局部测试帮助定位，但不能完全替代端到端运行。''')

add('engineering','03_offline_packaging','Python 打包、wheel 与安装入口','P01,P05,H05','packaging',
    '理解源码目录、构建后端、分发包和安装后命令的关系。',
    '1. pyproject.toml 声明 setuptools 构建后端；本例用 setup.cfg 兼容本机工具版本。\n2. 复制源码到本次目录，离线构建 wheel。\n3. 在本次 venv 安装 wheel，再调用 linux-greet 验证入口。',
    '生成一个 wheel，并安装 linux-learning-demo 0.1.0；linux-greet --name Ubuntu 输出“你好，Ubuntu！”。无第三方下载，源码目录不写入打包产物。',
    '复制为自己的新包，改名称与问候规则；构建、安装到另一新环境，在源码目录以外调用命令，证明运行来自安装包。',
    '--no-build-isolation 要求所需后端已存在，本机已找到 setuptools/wheel。它不是忽略依赖；现代项目也可用 pyproject 的 project 表声明元数据。',
    '1. wheel 与源码文件夹相同吗？\n2. console_scripts 指向哪里？',
    '1. 不同，它是可安装分发物。\n2. 指向包内某个可调用入口，如 cli:main。',
    r'''## 几个“包”的区别

    Python 导入包、pip 分发名与系统 apt 包可以名称不同。本例分发叫 linux-learning-demo，导入包叫 linux_greeting，命令叫 linux-greet。排错要区分正在寻找哪一层。

    ## 离线可复现边界

    构建使用本机已安装后端，禁止下载；允许系统包的 venv 提供 wheel。要复现到另一台电脑，需要记录后端版本及兼容依赖，而不只保存 wheel 文件名。发布到 PyPI 不属于本课实验。''')

add('engineering','04_concurrency','线程池、Future 与任务汇总','P03,P04,S03','concurrency',
    '将独立工作分派给线程池，区分并发、并行和结果顺序。',
    '1. 为 0～11 的每项执行平方计算。\n2. ThreadPoolExecutor 限制工作线程数量。\n3. map 按输入顺序返回结果，with 在结束时关闭线程池。',
    '结果等于顺序程序的 [0,1,4,...,121]，所有任务完成。这个小例子只验证执行契约，不证明线程让 CPU 计算更快。',
    '在自己的新程序里让任务等待不同时间，再比较 map 与 as_completed 的呈现顺序；给一个任务制造异常，观察在哪一步被重新抛出。',
    '不要在同一个受限线程池任务中互相等待依赖，可能死锁；共享可变数据仍需要同步。',
    '1. map 的顺序是什么？\n2. cancel 能强制中断已运行函数吗？',
    '1. 输入顺序。\n2. 通常不能，应为运行任务设计合作式停止。',
    r'''## 并发与并行

    并发描述任务可以交错推进，并行描述同一时刻执行多个任务。CPython 的 GIL 会限制许多 Python CPU 代码在线程中的并行；等待 I/O 时线程仍常有价值，CPU 密集任务可考虑进程或释放 GIL 的库。

    ## 结果与异常

    Future 保存任务状态和结果，result 会等待并可能抛出任务异常。线程数应结合任务性质与资源限制选择；保存失败任务标识，不能只统计完成数量。''')

add('engineering','05_cpp_library_tests','C++ 库目标、接口与 CTest','P09,P10,E02','cpp',
    '把头文件、实现、程序与测试组织成工程目标。',
    '1. units.hpp 声明接口，units.cpp 实现换算。\n2. main.cpp 与 test_units.cpp 分别链接 units 库。\n3. CMake 定义依赖，CTest 执行数值检查。',
    'Debug 构建成功，angle_conversion 测试通过；30 度输出约 0.523599。测试含 0 和 30 度，不用终端显示格式作为数学真值。',
    '另建自己的工程，增加 radians_to_degrees 及负角度测试；故意改错公式，确认 CTest 失败，再修复。',
    '头文件声明不等于实现已被链接。生成文件留在独立 build 目录，不能把旧二进制当作新源码结果。',
    '1. target_link_libraries 做什么？\n2. 构建成功等于测试通过吗？',
    '1. 声明程序与库的链接依赖。\n2. 不等于，还需实际执行测试。',
    r'''## 接口与编译单元

    头文件为使用者提供声明，.cpp 分别编译。库目标把实现组织成可复用部分，使用者通过依赖取得链接与需要的包含路径。PUBLIC 与 PRIVATE 的传播关系要随项目需求设计。

    ## 数值断言

    浮点比较使用误差容限；这里对库的内部 double 结果用更严格容差，对打印到六位小数的输出用 1e-6。测试通过证明这些输入契约，不代表所有参数均已处理。''')

add('engineering','06_debug_sanitizer','gdb、调用栈与 AddressSanitizer','P10,E05','debugging',
    '区别编译、逻辑和内存错误，使用断点与运行时诊断定位。',
    '1. Debug 构建供 gdb 在 main 断点观察 argc。\n2. 单独编译故意越界的 bounds_error.cpp，启用 AddressSanitizer。\n3. 保存错误报告，找到访问位置与分配范围。',
    '支持 ptrace 的环境会记录 argc=2；否则明确保留限制。越界进程应非零退出，asan.txt 包含 heap-buffer-overflow；它是预期失败，不是课程验收失败。',
    '阅读调用栈找到源码行，在自己的新文件用合法索引或 at() 改写，再比较结果。不要通过屏蔽诊断掩盖访问越界。',
    '优化可能使变量被消除；sanitizer 改变开销与运行布局。一次未报错不能证明不存在其他内存问题。',
    '1. -g 与 -fsanitize=address 分别作用？\n2. 堆越界为什么不能靠“程序能退出”判断？',
    '1. 调试信息与运行时内存诊断。\n2. 未定义行为可能正常结束也可能崩溃。',
    r'''## 调用栈与定位

    gdb 用断点停在指定位置，backtrace 说明当前调用链；print 与 next 帮助观察状态。环境可能限制调试自身子进程，需要记录限制，不能把静态配置当断点已命中。

    ## 预期失败的测试

    AddressSanitizer 为部分内存访问加检测。教学错误程序故意访问长度 3 的 vector 的索引 4；验收检查诊断类型与非零状态。修复后还要用正确结果和更多边界输入验证。''')

add('engineering','07_git_recovery','Git 冲突、abort 与 bisect','T03,T04,E02','git',
    '在可丢弃示例仓库中练习真正的冲突和回归定位。',
    '1. 两个分支修改同一行，merge 产生未合并状态。\n2. 先 merge --abort 确认恢复，再重新合并并保留双方意图。\n3. 另一示例仓库用 bisect run 查出首个坏提交，最后 reset 结束二分状态。',
    '冲突出现并恢复，解决后状态干净；五个演示版本中第 3 版（从 0 开始）是首个坏版本。全部在独立仓库，不改课程主分支。',
    '在自己的示例分支设计另一冲突，先记录共同祖先与两边意图再解决；给 bisect 的探针制造不稳定结果，解释它为何会误导二分。',
    'bisect 需要可重复的好/坏判断，状态 125 可跳过无法测试的提交。不要靠强推或硬重置处理未理解的历史。',
    '1. abort 会完成合并吗？\n2. 二分为什么比逐个提交试快？',
    '1. 不会，它终止当前合并并尝试恢复之前状态。\n2. 每次缩小区间，所需检查次数通常对数增长。',
    r'''## 冲突是语义选择

    标记只指出文本无法自动整合，正确结果取决于两边要实现什么。先解释意图，再编辑最终文件，检查测试和差异，最后提交；删掉标记本身不保证功能正确。

    ## 回归定位条件

    二分需要一个已知好提交和已知坏提交，以及在候选版本上可靠执行的判断。环境变化、随机输入或跨版本依赖缺失都可能污染判断；本例用明确探针验证算法流程。''')

add('engineering','08_container_build','Dockerfile、Compose 与环境边界（选修）','T06,P01,H05','containers',
    '读懂镜像构建上下文、COPY、启动命令与 Compose 服务配置。',
    '1. Dockerfile 从 Python 镜像复制自己的 app.py。\n2. Compose 定义只读、无网络的教学服务。\n3. 有 Compose 插件时用 config 解析模型，不启动容器。',
    '检查 Dockerfile 入口；插件可用时解析 JSON 模型并验证 read_only。报告明确记录未启动 daemon、未下载或构建镜像、未运行容器。',
    '在自己确认 Docker 可用后，从模板副本手动 build/run，记录实际镜像 digest 与结果。比较镜像里的文件和绑定挂载后的文件优先关系。',
    '构建上下文决定 COPY 能读哪些文件；.dockerignore 过滤上下文。镜像标签可更新，不能把标签当作固定内容摘要。',
    '1. docker compose config 会启动服务吗？\n2. 容器内只读是否限制全部宿主机？',
    '1. 不会，它解析配置。\n2. 不会，它描述该容器的根文件系统。',
    r'''## 构建与运行分开

    build 根据上下文和 Dockerfile 生成镜像，run 依据镜像配置启动进程，Compose 组织多个服务。本课的静态验证只证明配置可解析，不能证明 daemon、网络、GPU 或 GUI 可用。

    ## 科研环境边界

    venv 分隔 Python 包，容器分隔用户空间环境，二者都不能自动解决 ROS 域、设备权限和显卡驱动兼容性。先写清输入、设备与运行要求，再决定需要哪种隔离。''')

add('workflows','01_read_project','阅读陌生项目：入口、依赖与数据流','P05,P10,T03','reading',
    '从文件证据建立项目地图，避免见到脚本就直接运行。',
    '1. 先读 README，再找构建和依赖声明。\n2. 读取 setup.cfg 的 console_scripts 定位 cli:main。\n3. 追踪输入、调用、输出与环境，最后选择最小可验证入口。',
    '实验列出打包示例文件，明确 pyproject、setup.cfg 与 src/linux_greeting/cli.py 的关系。只读取源码和声明，不触发安装或外部项目任务。',
    '选自己的 ROS 或 cv 项目，写一页项目地图：正式入口、依赖、输入、输出、环境和验证方式。遇到设备或训练入口先解释作用，不凭名称猜运行条件。',
    'README 可能过时，应对照实际配置与源码。环境脚本、构建脚本和训练脚本责任不同，不能都当成启动入口。',
    '1. 包元数据为何值得先看？\n2. 最小运行应该证明什么？',
    '1. 它声明构建后端、依赖与安装入口。\n2. 一个明确输入到预期输出的最短流程可用。',
    r'''## 先静态，再动态

    静态阅读确认文件职责与依赖，动态运行验证真实行为。两者互相校验：目录存在不代表包可导入，声明入口不代表环境齐全。先写出假设，再选择不会引入复杂环境的最小验证。

    ## 与科研项目连接

    cv 的数组和数据、ROS 的节点和工作区、Linux 的进程和环境属于不同层。阅读时把每层入口标清，再解释它们怎样连接；不要用全局 PATH 改动掩盖依赖来源。''')

add('workflows','02_reproducibility','种子、参数、源码摘要与复现实验','P06,C08,E03','reproduce',
    '把一次结果组织成可检查的实验包，区分可重跑与可复现。',
    '1. 输入保存 seed=71、count=10，复制自包含源码。\n2. 保存环境版本、实际命令和源码/输入/输出摘要。\n3. 归档、恢复到新目录，再运行并比较结果字节。',
    '源码与资料摘要相同；同一环境重跑输出逐字节一致。归档包含实验脚本、参数、结果和清单，不包含整个 Python 环境或 GPU 栈。',
    '另建实验，把种子换成另一个值，验证结果变化；再只改变输出格式，解释内容等价与字节相同的区别。',
    '固定种子不能单独保证跨版本、跨硬件的随机或数值行为。只保存图表而不保存参数和输入，很难复核。',
    '1. 为什么保存源码摘要？\n2. 结果一致的结论范围是什么？',
    '1. 确认实际执行的代码版本。\n2. 本课验证的是同环境、同源码、同输入的结果。',
    r'''## 复现的必要信息

    输入、参数、源码、依赖版本、命令和输出构成最小证据链。源码版本可以用 Git 提交与摘要互补；未提交改动仍需单独保留，不能只引用一个旧提交号。

    ## 确定性边界

    同一算法也可能因浮点归约顺序、并发、硬件或依赖差异产生变化。报告应声明逐字节一致还是容差一致，以及已经验证哪些环境。本例选择标准库、固定种子和整数采样，便于理解边界。''')

add('workflows','03_incident_method','故障排查：证据、假设与最小改动','S03,S05,H05,N03','incident',
    '从失败现象提出可验证假设，每次只改变相关条件。',
    '1. 输入不存在时，记录状态 2 与完整错误。\n2. 同一合法数据在阈值 0.2 下返回 4。\n3. 将阈值改为 0.5 后返回 0，保留三次命令与报告。',
    '区分输入问题、巡检超限和规则通过。改变阈值只改变判定规则，没有修复日志里的错误；不能把“变成 0”冒充根因解决。',
    '给自己的工具制造表头错误，再写“现象→证据→假设→验证→结果→下一步”。每次只改变一个条件，并说明何时应回到原配置。',
    '异常等级与根因不是同一概念。重装、全局改环境或提高权限会引入新变量，先用更小的检查缩小范围。',
    '1. 非零退出必然表示代码缺陷吗？\n2. 放宽阈值修复了什么？',
    '1. 不必，也可能是输入或业务判定。\n2. 只改变接受规则，未消除实际错误。',
    r'''## 区分观察与解释

    “没有报告文件”是观察，“程序缺依赖”是假设。应通过解释器、路径、状态与日志逐项验证，不把猜测写成事实。保留改变前后的证据，才能判断是哪次改动产生效果。

    ## 排错树

    路径与输入→解释器和依赖→权限与资源→协议和参数→算法与结果，常能形成有效的检查顺序；具体顺序仍由症状决定。课程示例特意用三个状态表达不同分支，让诊断有可追踪依据。''')

add('workflows','04_capstone','综合实战：日志巡检、阈值与归档','H05,H06,E02,R02','capstone',
    '串联参数化工具、结构化报告、巡检结论与结果留存。',
    '1. 自动生成 8 条合法与 1 条坏格式记录。\n2. 用两个阈值运行巡检，保存各自报告与退出状态。\n3. 将输入和报告归档，读取归档内容验证一致。',
    '错误率 0.375；阈值 0.5 时通过，0.2 时超限。inspection.tar.gz 中报告字节与原报告一致；坏记录仍在报告中。',
    '在自己的新项目中加组件筛选、耗时阈值或文本摘要三者之一；为新行为写测试，再创建一次可恢复的结果包和说明。',
    '不应为了让巡检绿灯而丢弃坏记录。调度、报告和归档分属不同环节，失败时应指出具体阶段与保留的文件。',
    '1. 严格格式检查与错误率检查可以互相替代吗？\n2. 综合项目什么时候算完成？',
    '1. 不能，检查不同问题。\n2. 输入明确、结果正确、失败分支可解释、归档可读且变式通过。',
    r'''## 工具的整条数据流

    原始数据→解析与校验→合法记录统计→阈值判断→结构化报告→归档校验。每个箭头都应有契约，错误不能在中间被悄悄抹去。报告的分母、单位和未知值也是接口的一部分。

    ## 继续扩展

    可以把巡检挂到手动配置的用户定时器，或在已有 CI 环境中运行测试；先证明单次流程正确，再引入调度和发布。真实服务、外部认证或设备条件应单独验证，不从本地演示推断。''')


def relative(target,directory):
    return os.path.relpath(target,directory)


def main():
    base=json.loads((ROOT/'scripts/assets/course_manifest.json').read_text())
    paths={row['id']:ROOT/row['readme'] for row in base}
    advanced=[]
    for item in LESSONS:
        prefix,_=GROUPS[item['group']]
        number=sum(row['group']==item['group'] for row in advanced)+1
        identifier=f'{prefix}{number:02d}'
        directory=ROOT/'course/advanced'/item['group']/item['slug']
        directory.mkdir(parents=True,exist_ok=True)
        row={'id':identifier,'group':item['group'],'title':item['title'],
             'readme':str((directory/'README.md').relative_to(ROOT)),
             'theory':str((directory/'THEORY.md').relative_to(ROOT)),
             'lab':item['lab'],'prerequisites':item['prerequisites']}
        advanced.append(row); paths[identifier]=directory/'README.md'
    for index,(item,row) in enumerate(zip(LESSONS,advanced)):
        directory=(ROOT/row['readme']).parent
        nav=[f'[进阶总览]({relative(ROOT/"course/advanced/README.md",directory)})','[理论补充](THEORY.md)']
        if index: nav.append(f'[上一课]({relative(ROOT/advanced[index-1]["readme"],directory)})')
        if index+1<len(advanced): nav.append(f'[下一课]({relative(ROOT/advanced[index+1]["readme"],directory)})')
        prerequisites='、'.join(f'[{key}]({relative(paths[key],directory)})' for key in item['prerequisites'])
        sources=relative(ROOT/'docs/ADVANCED_RESOURCES.md',directory)
        readme=f'''# {row['id']}：{item['title']}

{' · '.join(nav)}

## 前置知识

{prerequisites}。若已能解释这些操作，可直接进入，不必按页数重复学完基础课。

## 学习目标

{item['goal']}

## 原理与步骤

{item['steps']}

## 动手实验

先写预期结果，再从仓库根目录运行：

```bash
bash scripts/advanced.sh lab {item['lab']}
```

入口打印本次实验目录；`lab.json` 保存检查内容，`commands.jsonl` 保存实际子命令、状态和输出。读取报告，再在[实验源码]({relative(ROOT/'scripts/advanced_lab.py',directory)})中定位 `{item['lab']}` 分支。独立模型和例子在 `scripts/advanced/` 下。

## 结果与边界

{item['expected']}

## 变式练习

{item['exercise']}

自己的新源码仍放 `scripts/`，草稿用 `scripts/practice/`，准备保存版本的作品用 `scripts/exercises/`。不要覆盖课程原示例。记录变式输入、预期、实际结果与解释。

## 常见误区

{item['pitfalls']}

## 自检

{item['quiz']}

<details>
<summary>完成后查看参考答案</summary>

{item['answer']}

</details>

阅读[理论补充](THEORY.md)，检查能否独立解释失败分支。官方资料见[来源与版本说明]({sources})。
'''
        theory=f'''# {row['id']} 理论：{item['title']}

[回到实验](README.md) · [进阶总览]({relative(ROOT/'course/advanced/README.md',directory)})

{item['theory']}

## 本课的输入与结果契约

{item['goal']}

{item['expected']}

## 用变式检验理解

{item['exercise']}

先把原理写成可观察的预期，再运行；如果结果不同，保留证据并定位具体步骤。只改变一个条件，才能判断结果为何发生变化。

## 结论的边界

{item['pitfalls']}

参考[官方资料与本机版本]({sources})。自动完成的检查与需要手动操作的部分分开记录。
'''
        (directory/'README.md').write_text(readme,encoding='utf-8')
        (directory/'THEORY.md').write_text(theory,encoding='utf-8')
    (ROOT/'scripts/assets/advanced_manifest.json').write_text(json.dumps(advanced,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for group,(_,title) in GROUPS.items():
        destination=ROOT/'course/advanced'/group
        lines=[f'# {title}','','[进阶总览](../README.md)','','| 编号 | 课程 | 前置 |','| --- | --- | --- |']
        lines += [f'| {row["id"]} | [{row["title"]}]({relative(ROOT/row["readme"],destination)}) | {", ".join(row["prerequisites"])} |' for row in advanced if row['group']==group]
        (destination/'README.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    destination=ROOT/'course/advanced'
    lines=['# Linux 进阶课程：24 节实践','','在基础操作之后学习可靠脚本、系统观察、工程工具和可复现实验。可以按顺序，也可按[目标路线](../START_HERE.md)进入；每节明确列出前置知识。','','| 系列 | 节数 | 核心能力 |','| --- | --- | --- |',
           '| [Bash 与文本处理](shell/README.md) | 6 | 参数、解析、退出、CLI 与文件锁 |',
           '| [系统与网络](systems/README.md) | 6 | 资源、性能、HTTP、SSH、调度、备份 |',
           '| [程序工程](engineering/README.md) | 8 | 模型、测试、打包、并发、C++、调试、Git、容器 |',
           '| [复现与排错](workflows/README.md) | 4 | 项目阅读、证据包、诊断与巡检工具 |','','| 编号 | 课程 | 实验名 |','| --- | --- | --- | --- |']
    lines += [f'| {row["id"]} | [{row["title"]}]({relative(ROOT/row["readme"],destination)}) | `{row["lab"]}` |' for row in advanced]
    lines += ['','## 怎么开始','','```bash','bash scripts/advanced.sh doctor','bash scripts/advanced.sh lab quoting','```','','每次 45～90 分钟，一节可分两次。先完成自动实验，再做变式；不把“能跑现成命令”当成学会。完整范围见[进阶验收](../../docs/ADVANCED_VALIDATION.md)。',
              '','阶段任务见[里程碑](../MILESTONES.md)，实际任务查[场景索引](../SCENARIOS.md)。学习进度由你主动记录，运行实验不会自动打勾。',
              '','最后可选做[日志巡检工具](../../projects/cli_inspector/README.md)、[复现实验包](../../projects/reproducible_run/README.md)和[Git 恢复演练](../../projects/git_rescue/README.md)。','']
    (destination/'README.md').write_text('\n'.join(lines),encoding='utf-8')
    lines=['# 完整课程总览：基础 36 + 进阶 24','','共 **60 节**，主环境 Ubuntu 22.04。基础与进阶都有操作、理论、变式和自检；容器实操与真实远程操作按依赖选择。',
           '','先看[从哪里开始](START_HERE.md)选择路线；想解决当前问题查[场景索引](SCENARIOS.md)，想验证独立能力做[阶段任务](MILESTONES.md)。',
           '','## 基础课程（36 节）','','| 编号 | 课程 |','| --- | --- |']
    lines += [f'| {row["id"]} | [{row["title"]}]({Path(row["readme"]).relative_to("course")}) |' for row in base]
    lines += ['','## 进阶课程（24 节）','','[系列导览](advanced/README.md)。需要哪一课可按其前置知识进入，不要求先逐页读完。','','| 编号 | 课程 |','| --- | --- |']
    lines += [f'| {row["id"]} | [{row["title"]}]({Path(row["readme"]).relative_to("course")}) |' for row in advanced]
    lines += ['','## 项目与辅助资料','','- [六个综合项目](../projects/README.md)','- [术语表](GLOSSARY.md)与[命令速查](CHEATSHEET.md)',
              '- [学习记录模板](../scripts/templates/study_record.md)','- [基础运行](../scripts/README.md)与[进阶运行](../scripts/ADVANCED.md)',
              '- [故障指南](../docs/TROUBLESHOOTING.md)与[进阶验收](../docs/ADVANCED_VALIDATION.md)',
              '','每课按“理解→预测→操作→观察→变式→解释”学习。基础每次约 30～60 分钟，进阶约 45～90 分钟，按自己的节奏推进。',
              '','```bash','bash scripts/learn.sh catalog','bash scripts/learn.sh progress','```','']
    (ROOT/'course/README.md').write_text('\n'.join(lines),encoding='utf-8')
    # 基础最后一课补上过渡导航；只更新文档。
    last=ROOT/base[-1]['readme']
    marker='\n<!-- advanced-transition -->\n'
    content=last.read_text(encoding='utf-8').split(marker)[0]
    content += marker+f'\n基础工具课之后，可进入[进阶系列]({relative(ROOT/"course/advanced/README.md",last.parent)})，或按[目标路线]({relative(ROOT/"course/START_HERE.md",last.parent)})选择下一步。\n'
    last.write_text(content,encoding='utf-8')
    print('已生成进阶 24 节与理论页，并更新 60 节课程导航。')


if __name__=='__main__': main()
