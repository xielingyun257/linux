"""维护课程的正文与导航。新增可执行代码仍全部放在 scripts/。"""
import json
from pathlib import Path
import inspect

ROOT = Path(__file__).resolve().parent.parent
LESSONS = []
GROUPS = {
    'ubuntu': ('lessons/ubuntu_basics', 'U', 'Ubuntu 日常操作', '零基础，从桌面建立计算机与文件的概念。'),
    'terminal': ('lessons/terminal', 'C', '终端与命令行', '先理解路径与参数，再组合命令处理文件。'),
    'system': ('lessons/system', 'S', '系统管理基础', '解释权限、软件、进程、服务、网络和磁盘的职责。'),
    'programming': ('programming', 'P', '编程基础', '用 Python 建立程序思维，再学 Bash 自动化与 C++ 构建。'),
    'tools': ('tools', 'T', 'Linux 配套工具', '把编辑、调试、版本管理和终端会话连成工作流程。'),
}


def lesson(group, slug, title, goal, concept, commands, expected, exercise, pitfalls, questions, answers, theory):
    LESSONS.append(dict(group=group, slug=slug, title=title, goal=goal, concept=concept,
                        commands=inspect.cleandoc(commands).strip(), expected=expected,
                        exercise=exercise, pitfalls=pitfalls, questions=questions,
                        answers=answers, theory=inspect.cleandoc(theory).strip()))


lesson('ubuntu', '01_linux_ubuntu', 'Linux、Ubuntu 与电脑里的几层软件',
       '区分硬件、内核、发行版、桌面、终端与应用；查出本机系统版本。',
       'CPU 执行指令，内存保存正在使用的数据，磁盘保存文件。Linux 内核管理硬件与进程；Ubuntu 把内核、软件包和桌面组合成可使用的系统。GNOME 是桌面环境，Bash 是命令解释器，它们负责不同的交互方式。',
       r'''cat /etc/os-release
       uname -r
       bash scripts/study.sh environment''',
       '本机 VERSION_ID 为 22.04，课程解释器是 /usr/bin/python3。uname 输出内核版本，不能拿它当 Ubuntu 版本号。环境报告的路径会随每次运行变化。',
       '在 scripts/practice/ 下新建自己的学习笔记，画出“硬件→内核→桌面/终端→应用”的关系，并记录两个版本号的含义。',
       'Ubuntu、Linux 和终端不是同一个软件；网上不同发行版的安装命令不能直接混用。',
       '1. Bash 属于内核吗？\n2. 系统版本与内核版本为什么不同？',
       '1. 不属于，它是用户空间程序。\n2. Ubuntu 发行版和 Linux 内核分别维护、分别编号。',
       r'''## 分层如何帮助排错

       桌面打不开应用，可能是启动器的问题，也可能是应用报错。终端中运行同一个应用可以看到错误信息；这并不表示应用“属于终端”。文件读写最终仍通过操作系统完成。

       ## LTS 与课程环境

       LTS 表示长期支持发行版。这里记录本机实际版本，课程不要求升级系统。ROS 2 Humble 与系统 Python 的二进制依赖有关，因此学习 Linux 时也要保留环境边界。''')

lesson('ubuntu', '02_desktop_windows', '桌面、窗口与快捷键',
       '打开应用、切换窗口和工作区，理解关闭窗口与退出程序的关系。',
       '活动概览负责查找应用和窗口；工作区用于分组窗口。键盘快捷键由桌面和当前应用分别处理，同一个按键组合在不同应用中可能有不同意义。',
       r'''# 在桌面手动完成：
       # Super：打开活动概览；输入“终端”后按 Enter
       # Ctrl+Alt+T：打开终端
       # Alt+Tab：切换应用
       # Alt+F4：关闭当前窗口
       printf '终端已启动\n'
       echo "$XDG_CURRENT_DESKTOP"''',
       '桌面操作应看到窗口实际切换；终端打印“终端已启动”。变量可能包含 ubuntu:GNOME，远程或无图形会话可能为空。',
       '同时打开文件管理器和两个终端；把一个窗口移动到另一个工作区，切换回来，描述“窗口”和“工作区”的区别。',
       '关闭终端可能影响从该终端启动的任务；在应用设置中重新绑定快捷键后，默认组合可能失效。',
       '1. 工作区会创建另一套文件吗？\n2. 无桌面的 SSH 会话能用命令行吗？',
       '1. 不会，工作区只是窗口组织方式。\n2. 能，命令行不依赖桌面。',
       r'''## 窗口、应用、进程

       一个应用可以有多个窗口，也可能有多个进程。浏览器每个标签页不等于一个独立应用；关闭一个窗口也不一定结束全部后台进程。系统管理课会用 ps 查看真正的进程。

       ## 快捷键的上下文

       Super 通常是键盘 Windows 标志键。桌面收到某些全局组合键，应用收到其余组合键。先看“设置→键盘→查看及自定义快捷键”，再确认本机的绑定。''')

lesson('ubuntu', '03_file_manager', '文件管理器、目录与隐藏文件',
       '在图形界面中找到仓库，区分文件、目录、路径和扩展名。',
       '目录是组织文件的容器。绝对路径从 / 开始；文件扩展名提示用途，不决定文件是否真的具有该格式。以点开头的名称通常默认隐藏，例如 .gitignore。',
       r'''pwd
       ls -la
       bash scripts/study.sh demo files
       # 文件管理器按 Ctrl+L，输入仓库绝对路径
       # Ctrl+H 切换隐藏文件；Ctrl+Shift+N 新建文件夹''',
       '实验创建“练习 文件/笔记.txt”和 renamed.txt，内容一致。文件管理器能看到 .gitignore；scripts/runs/ 中是刚生成的练习资料。',
       '在文件管理器中打开刚生成的实验目录，复制笔记，给副本改名；比较原文件和副本内容，记录它们的完整路径。',
       '同名文件在不同目录里可以同时存在。把 .txt 改成 .png 不会把文本转成图片。',
       '1. / 与当前目录有什么区别？\n2. 隐藏文件能被终端访问吗？',
       '1. / 是文件系统根目录，当前目录是本终端所在位置。\n2. 能，隐藏是显示习惯，不是权限限制。',
       r'''## Linux 的统一目录树

       Linux 把磁盘和分区挂载到目录树中。本仓库所在 /media/wdros/DataE 是挂载路径，不是 Windows 的盘符。进入挂载目录后，路径写法仍遵循同一规则。

       ## 三种常用目录

       /home 保存用户家目录，/etc 保存许多系统配置，/usr 保存许多已安装程序与库。这里只读系统资料；自己的练习放 scripts/practice/，自动实验放 scripts/runs/。''')

lesson('ubuntu', '04_input_clipboard', '中文输入、复制粘贴与终端快捷键',
       '切换输入源，正确复制粘贴命令，解释 Ctrl+C 在终端中的作用。',
       '图形应用通常用 Ctrl+C/V 复制粘贴；终端通常用 Ctrl+Shift+C/V。终端中的 Ctrl+C 通常向前台任务发送中断信号。输入法影响你键入的字符，不会替命令纠正中文标点。',
       r'''printf '你好，Ubuntu\n'
       printf '%s\n' '包含 空格的文本'
       sleep 30
       # 在 sleep 运行时按 Ctrl+C，再输入下一条命令
       printf '我已经回到提示符\n'
       # 桌面：设置→键盘→输入源；按本机绑定切换输入法''',
       'sleep 原本等待 30 秒；按 Ctrl+C 后提前返回提示符。单引号保留文字和空格，命令中的引号必须是英文半角字符。',
       '先在编辑器写一条带中文文本的 printf，再粘贴到终端执行；分别演示复制文本与中断等待任务。',
       '不要连提示符里的 $ 或教程里的注释说明一起当成命令。弯引号“”与中文分号不能替代 Shell 语法字符。',
       '1. Ctrl+C 在终端为何不总是复制？\n2. 单引号中的空格会拆成参数吗？',
       '1. 它通常对应前台任务的中断操作。\n2. 不会，这一整段是一个参数。',
       r'''## 字符与字节

       UTF-8 用可变长度字节表示字符。中文文本出现乱码时，要检查文件编码、终端编码和字体；字符数与文件字节数并不相同。

       ## 输入法与 Shell 解析

       Shell 在执行程序前解析空格、引号和变量。先让输入法生成正确的英文语法字符，再让程序处理引号里的中文数据。Tab 补全可减少长路径输入错误。''')

lesson('ubuntu', '05_settings_devices', '系统设置、设备与软件入口',
       '找到网络、显示、声音、蓝牙与关于页面；区分设置、驱动和应用。',
       '系统设置提供常见配置界面；驱动让内核与硬件通信；应用使用已经提供的设备能力。设置页面能够看到设备，不保证每个应用已经配置好该设备。',
       r'''# 桌面：打开“设置”，查看“关于”“显示器”“声音”“网络”
       lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS
       free -h
       df -h .''',
       'lsblk 列出块设备，free 显示内存，df 显示仓库所在文件系统的空间。三者的“容量”描述不同对象。',
       '记录当前分辨率、输出声音设备、网络连接方式，以及内存和磁盘的区别；观察设置页后恢复自己原来的选择。',
       '任务管理中的内存占用不是磁盘占用。更新驱动、修改分区和普通应用设置影响范围不同。',
       '1. free 与 df 各看什么？\n2. 软件中心和 apt 是同一种交互界面吗？',
       '1. free 看内存，df 看文件系统空间。\n2. 不是，前者是图形入口，apt 是命令行包管理工具。',
       r'''## 设备、分区、文件系统、挂载

       一块物理磁盘可以分成多个分区；分区上的文件系统负责组织文件；挂载把它接到目录树中。lsblk、df、文件管理器分别呈现不同视角。

       ## 配置何时生效

       应用设置可能只影响当前程序；用户设置可能影响之后的会话；系统或驱动设置可能需要重新登录或重启。先理解变化范围，再判断是否生效。''')

lesson('ubuntu', '06_screenshots_learning', '截图、求助与记录一次操作',
       '保存截图和可复现的操作记录，学会查本机帮助。',
       '截图保留界面状态，文本日志保留完整错误与命令。一次有用的记录包含目标、环境、命令、预期、实际结果和改动；只写“运行失败”无法定位原因。',
       r'''# 桌面按 Print Screen；按界面提示选区域或窗口
       # 将用于课程的截图放 scripts/practice/ 下
       mkdir -p scripts/practice
       ls --help
       man ls
       # 在 man 中 / 搜索，n 找下一个，q 退出
       bash scripts/study.sh environment''',
       '能保存一张截图，找到 ls 的 -a 说明，并查看环境 JSON。终端自动实验的 commands.jsonl 保存命令、标准输出和错误输出。',
       '用“操作前预测→操作→观察→解释”的格式记录一次隐藏文件显示；说明自己的结果与预期是否一致。',
       '手册中的 [参数] 表示可选项，尖括号通常表示要替换的内容；它们不是都需要原样输入。',
       '1. man 中怎样退出？\n2. 为什么求助时要保留错误全文？',
       '1. 按 q。\n2. 错误类型、路径和上下文常决定解决方法。',
       r'''## 两条查帮助路线

       本机 --help 与 man 对应已安装版本；网上官方文档能解释概念，但版本可能更新。课程以本机帮助验证具体参数，再用官方资料补充原理。

       ## 证据的边界

       文件存在说明它已被创建，不能证明程序正确。需要对照输入、输出与完成标准。自动检查可以验证文件与数值，桌面步骤仍需自己实际操作并记录。''')

lesson('terminal', '01_shell_commands', '终端、Shell 与一条命令的结构',
       '读懂命令名、选项、参数、提示符和退出状态。',
       '终端传递键盘输入并显示结果，Bash 解析命令，具体程序完成任务。ls -la scripts 中 ls 是程序，-la 是短选项组合，scripts 是路径参数。Shell 内建命令 cd 会改变当前 Shell 的状态。',
       r'''pwd
       type cd
       type ls
       ls -la scripts
       false
       printf '上一条退出状态：%s\n' "$?"''',
       'cd 被识别为内建命令，ls 通常是程序或别名；false 的状态是 1。printf 成功后再看 $?，看到的是 printf 的状态。',
       '将 ls -la scripts 拆成三部分，尝试 ls -l -a scripts 并解释结果为何相同。',
       'Shell 区分大小写；命令提示符中的用户名、路径和 $ 不属于要输入的命令。',
       '1. 退出状态 0 通常表示什么？\n2. 为什么另一个终端的 cd 不影响本终端？',
       '1. 命令成功。\n2. 每个 Shell 有自己的当前目录等状态。',
       r'''## 执行顺序

       Bash 先做语法解析与展开，再寻找内建命令或 PATH 中的可执行程序，最后等待前台任务。PATH 是按顺序搜索的目录列表，因此同名程序可能解析到不同位置。

       ## 标准输出与退出状态

       “没有打印内容”不等于失败；状态码与输出是两个通道。失败常向标准错误写说明并返回非零状态。$? 只保存最近结束的命令状态，要及时记录。''')

lesson('terminal', '02_paths_navigation', '绝对路径、相对路径与目录导航',
       '用 pwd 与 cd 确认位置，正确处理空格和中文路径。',
       '/ 开头是绝对路径，其他路径通常相对当前目录。点号 . 表示当前目录，.. 表示父目录；~ 在合适的 Shell 上下文中展开为家目录。给路径加引号可保留空格。',
       r'''pwd
       mkdir -p 'scripts/practice/路径 练习'
       cd 'scripts/practice/路径 练习'
       pwd
       cd ../../..
       pwd
       ls ./scripts''',
       '第一次进入新目录，三级 .. 回到仓库根目录。所有命令按这一顺序在同一终端执行。',
       '用一条相对路径和一条绝对路径进入同一个练习目录；写出每次 pwd 的预期值再执行。',
       'cd .. 与 cd.. 不同；引号里的 ~ 不会像裸 ~ 一样展开。路径拼写与实际大小写应一致。',
       '1. ./scripts 相对哪里？\n2. 路径包含空格为何要加引号？',
       '1. 当前工作目录。\n2. 避免 Shell 把一个路径拆成多个参数。',
       r'''## 当前目录是隐含输入

       同一条 ls scripts 在仓库根目录可用，在其他目录可能报错。程序中的相对输入路径也有同样问题。课程入口根据脚本自身路径定位仓库，不依赖调用者所在目录。

       ## 逻辑与物理路径

       软链接可能让 pwd 的逻辑路径与实际物理路径不同；pwd -P 查看物理路径。目录导航先确认位置，再理解后续文件操作的范围。''')

lesson('terminal', '03_file_operations', '创建、复制、移动与删除练习文件',
       '理解 mkdir、touch、cp、mv、rm 和重定向各自做什么。',
       'touch 更新时间戳，文件不存在时会创建空文件；cp 复制，mv 移动或重命名。> 写入文件会截断已有内容，>> 追加。rm 删除指定目录项，终端删除通常不进入桌面回收站。',
       r'''mkdir -p scripts/practice/files
       printf '第一条笔记\n' > scripts/practice/files/original.txt
       cp -i scripts/practice/files/original.txt scripts/practice/files/copy.txt
       mv -i scripts/practice/files/copy.txt scripts/practice/files/renamed.txt
       cat scripts/practice/files/renamed.txt
       # 确认这是刚建立的副本，再删除它；提示时输入 y
       rm -i scripts/practice/files/renamed.txt
       bash scripts/study.sh demo files''',
       '副本改名后内容仍是“第一条笔记”；删除副本后 original.txt 仍在。自动实验会额外验证复制后的内容。',
       '给 original.txt 追加第二行；解释追加与覆盖的区别，列出目录确认最终只保留原文件。',
       'mkdir -p 可重复建立目录，但 > 会覆盖文件内容；cp 到已存在的同名目标也可能覆盖。',
       '1. touch 会写入文字吗？\n2. rm 副本会删除原文件吗？',
       '1. 不会。\n2. 普通复制生成不同文件，删除副本不删除原文件。',
       r'''## 目录项与文件内容

       重命名通常只改变目录中的名字，并不重写文件全部内容。复制需要创建新文件并写入内容。硬链接、软链接与普通复制的关系不同，在系统课再比较。

       ## 操作顺序

       先建立目标目录，再创建文件，再查看内容和路径，最后操作指定练习副本。-i 在可能覆盖或删除时提示；它适合初学手动操作，自动程序应设计独立输出目录。''')

lesson('terminal', '04_read_text', '查看文本、日志与文件类型',
       '按文件大小和用途选择 cat、less、head、tail 与 file。',
       'cat 输出整个文件；less 分页浏览；head/tail 查看开头或末尾。file 根据内容特征猜测类型，wc 可计数。程序输出不一定是 UTF-8 文本，不应把所有二进制文件直接交给 cat。',
       r'''bash scripts/study.sh demo text
       # 下面用源码文本练习，不改动它
       head -n 12 scripts/lab.py
       tail -n 8 scripts/lab.py
       wc -l scripts/lab.py
       file scripts/lab.py
       less scripts/lab.py''',
       'head 和 tail 显示不同部分，wc -l 输出行数。less 中按 / 搜索 new_run，按 n 继续，按 q 退出。',
       '在刚生成的 events.log 中分别查首两行、末两行和总行数；说明 tail -f 与一次性的 tail 有何差别。',
       'tail -f 会持续等待新内容，需 Ctrl+C 结束；wc -l 计的是换行符，最后一行没有换行时可能与肉眼数行不同。',
       '1. 大日志先用 cat 还是 less？\n2. 扩展名能保证真实文件类型吗？',
       '1. less 更适合分页查看。\n2. 不能，应结合内容和生成方式。',
       r'''## 文本不是显示效果

       文件里的字符、编码和换行共同决定显示。Windows 常见 CRLF 与 Linux 常见 LF 是两种换行编码；脚本出现 ^M 时应检查换行格式。

       ## 观察正在增长的日志

       tail -f 跟踪打开的文件；tail -F 按文件名重试，对日志轮转更实用。它只展示新内容，不判断报错是否严重；还需结合时间、任务和退出状态。''')

lesson('terminal', '05_search_find', '查文件与查内容：find、grep、rg',
       '区分按名称找文件与在文件中搜索文字。',
       'find 遍历目录并按条件选择路径；grep 搜索文本行；rg 是可选的快速文本搜索工具。Shell 通配符和正则表达式是两套语法：*.md 选文件名，^ERROR 匹配行首文字。',
       r'''find course -type f -name '*.md'
       grep -n 'def main' scripts/lab.py
       grep -R -n '平均值' scripts/programming/python --include='*.py'
       command -v rg
       # 已安装 rg 时可试：
       # rg -n '平均值' scripts/programming/python''',
       'find 返回 Markdown 路径，grep -n 返回行号和匹配行。没有安装 rg 时仍可用 grep 与 find 完成本课。',
       '找到全部 C++ 源文件；查出哪些 Python 文件包含 raise ValueError，解释两个任务为何使用不同工具。',
       'find 的 *.md 应加引号，否则可能先被当前 Shell 展开。grep 搜不到时状态为 1，这不必然是运行错误。',
       '1. -type f 排除了什么？\n2. ^ERROR 与 ERROR 匹配范围相同吗？',
       '1. 目录等非普通文件。\n2. 不同，前者要求出现在行首。',
       r'''## 搜索范围是重要参数

       从仓库根目录查文本时，构建目录、日志与 .git 会引入很多无关结果。指定课程或代码子目录，再决定是否需要隐藏文件与被忽略文件。

       ## 正则的最小集合

       ^ 表示行首，$ 表示行尾，. 表示一个字符。grep 默认使用基本正则，grep -E 使用扩展正则。固定字符串可用 grep -F，避免把 . 等字符解释成模式。''')

lesson('terminal', '06_pipes_redirection', '管道、标准输出与错误输出',
       '将多个命令组合成流程，并分别保存结果和错误。',
       '文件描述符 0、1、2 通常对应标准输入、标准输出、标准错误。| 默认只把前一条的标准输出传给下一条的标准输入。2> 保存错误，> 保存结果，tee 同时显示与写文件。',
       r'''mkdir -p scripts/practice/pipes
       printf 'INFO start\nERROR camera\nERROR camera\nERROR network\n' > scripts/practice/pipes/events.log
       grep '^ERROR' scripts/practice/pipes/events.log | cut -d ' ' -f 2 | sort | uniq -c
       ls scripts/practice/pipes/not-created > scripts/practice/pipes/out.txt 2> scripts/practice/pipes/err.txt
       cat scripts/practice/pipes/err.txt
       bash scripts/study.sh demo text''',
       '统计结果是 camera 2 次、network 1 次。指定不存在路径的 ls 故意失败，错误进入 err.txt，out.txt 没有正常列表。',
       '把错误统计保存到 summary.txt，同时在屏幕显示；解释 uniq -c 前为什么需要 sort。',
       '2>&1 与 > 的先后次序影响流向；管道默认状态通常来自最后一个命令，自动脚本可用 set -o pipefail。',
       '1. | 会默认传递标准错误吗？\n2. uniq 能合并不相邻的重复行吗？',
       '1. 不会。\n2. 不能，先排序才能把相同项放在一起。',
       r'''## 管道传递字节流

       grep 选择行，cut 取字段，sort 排序，uniq 统计相邻重复项。每一步都有明确输入与输出，先单独观察，再组合，才能定位是哪一步改变了结果。

       ## 重定向顺序

       command >out.txt 2>&1 让两个流都进入 out.txt；command 2>&1 >out.txt 先让错误指向原输出位置，再改变标准输出，因此错误可能仍显示在终端。''')

lesson('terminal', '07_environment_paths', '环境变量、PATH 与启动配置',
       '查清命令实际来自哪里，理解变量的作用范围。',
       'Shell 变量存在于当前 Shell；export 后子进程可以继承。PATH 决定程序搜索顺序。source 在当前 Shell 执行文件，bash script.sh 使用另一个 Shell，因此二者对环境的影响不同。',
       r'''printf '%s\n' "$PATH"
       type -a python3
       command -v python3
       /usr/bin/python3 --version
       LINUX_LESSON_MESSAGE='一次命令的环境' /usr/bin/python3 -c 'import os; print(os.environ["LINUX_LESSON_MESSAGE"])'
       bash scripts/study.sh environment''',
       '本机裸 python3 优先找到 Miniforge，课程入口固定 /usr/bin/python3。单条命令的环境赋值不会永久写入 ~/.bashrc。',
       '创建一个自己的变量，先不 export 再 export，用子进程读取并比较；完成后 unset 该练习变量。',
       '不要为一个项目替换系统 /usr/bin/python3 链接。当前终端临时设置与写入启动配置是两种操作。',
       '1. source 与 bash 的环境作用范围相同吗？\n2. 绝对路径启动程序还需 PATH 查找吗？',
       '1. 不同。\n2. 指定该程序时不需要搜索 PATH。',
       r'''## 父进程与子进程

       子进程继承启动时的环境副本，不能直接修改父 Shell 的变量。激活虚拟环境用 source，是为了改变当前 Shell 的 PATH 等状态；课程启动器则把隔离限制在自己的子进程。

       ## 两种清理机制

       Python 的 -E 忽略 PYTHON* 环境变量，-s 不加载用户 site-packages；-I 还排除脚本目录等搜索位置。模块课需要同目录导入，因此入口对子示例使用 -E -s。''')

lesson('terminal', '08_archives_links', '压缩归档、校验与软链接',
       '列出压缩包内容，解释归档与压缩的区别，认识软链接。',
       'tar 把多个路径组织成归档；gzip 压缩字节。tar -czf 创建 gzip 归档，-tzf 查看清单。软链接保存目标路径，目标移走后链接可能失效；它不是文件内容的副本。',
       r'''bash scripts/study.sh demo archives
       mkdir -p scripts/practice/links
       printf '链接目标\n' > scripts/practice/links/target.txt
       ln -s target.txt scripts/practice/links/shortcut.txt
       ls -l scripts/practice/links
       cat scripts/practice/links/shortcut.txt
       sha256sum scripts/practice/links/target.txt''',
       '归档实验得到 notes.tar.gz 和 restored.txt，并验证字节一致。软链接显示 shortcut.txt -> target.txt；本机 NTFS 挂载能否建链接以实际结果为准。链接已存在时 ln 会报错。',
       '对归档内容先列清单，再在一个新目录恢复；比较恢复文件与原文件的校验值。给软链接画出指向关系。',
       '软链接目标的相对路径相对链接所在目录。压缩成功不等于备份可恢复，还需要实际读取或恢复校验。',
       '1. 归档必须压缩吗？\n2. SHA-256 相同在这里说明什么？',
       '1. 不必，tar -cf 可只归档。\n2. 支持两份文件内容一致的判断；不是来源真实性证明。',
       r'''## 备份完成标准

       需要知道备份包含哪些路径、保存在哪里、能否读取，以及恢复后内容是否一致。综合项目使用清单与 SHA-256 验证自己的教学归档。

       ## 路径恢复

       tar -C 新目录 -xzf 归档名 会在指定目录恢复。先查看清单，尤其留意包中路径。课程自动归档只包含自己生成的已知文件；软链接也不替代真正的数据备份。''')

lesson('system', '01_users_permissions', '用户、组、权限与 sudo',
       '读懂权限位，区分普通用户、管理员授权与文件所有者。',
       'r/w/x 对文件分别表示读、写、执行；对目录分别表示列名字、修改目录项、进入或搜索路径。三组位对应所有者、所属组和其他用户。sudo 按系统策略用更高权限执行一条命令，不是修复所有报错的通用办法。',
       r'''id
       ls -ld . scripts
       umask
       bash scripts/study.sh demo permissions
       # 自动实验只对自己新建的 private.txt 尝试 chmod 600''',
       '报告显示请求的 0600 和实际观察到的模式。本仓库在 NTFS 上：若 chmod 后显示与预期不同，结合 findmnt 的文件系统、挂载参数解释；不要直接把课本里的 ext4 行为当成实测。',
       '将 rw-r----- 转成八进制，并判断所属组能否读、写、执行；从实验报告解释本机 chmod 的实际结果。',
       '文件可写不等于能删除：删除还取决于父目录。chmod 777 会扩大权限，应先解释需要哪一位。',
       '1. rw-r----- 对应多少？\n2. 目录 x 位是什么作用？',
       '1. 640：6=4+2，4=读，0=无权限。\n2. 进入目录和按名称访问其中路径所需的搜索权限。',
       r'''## 权限与文件系统

       POSIX 文件系统可保存用户、组与模式位；NTFS 的 Linux 驱动可能从挂载选项映射这些信息。本课程把“chmod 命令成功”和“观察到所需权限位”分别记录。

       ## 默认权限与管理员

       umask 在程序申请的初始权限基础上屏蔽部分位，不会给普通文本自动增加执行位。sudo 提升权限时路径与环境也可能变化，排错先检查对象、所有者和当前用户。''')

lesson('system', '02_packages_software', 'apt、dpkg、Snap 与软件安装',
       '查出软件包来源，理解安装、更新索引、升级和卸载的区别。',
       'dpkg 管理本地 Debian 软件包，apt 处理仓库索引与依赖。apt update 更新可用软件信息，apt upgrade 升级已安装包。Snap 是另一套打包与分发机制；pip 管 Python 包，不能替代系统包管理。',
       r'''apt-cache policy git
       dpkg-query -W git
       dpkg -L git | head -n 12
       command -v snap
       # 以下是手动安装流程，自动实验不会执行：
       # sudo apt update
       # sudo apt install tree
       # tree --version''',
       '显示 git 已安装版本与候选版本；dpkg -L 列出系统包管理器登记的路径。注释中的命令只在自己决定安装 tree 时执行。',
       '用 command -v 与 dpkg -S 查 git 可执行文件所属包，解释“可执行文件位置”和“包名”的区别。',
       'sudo pip install 可能污染系统 Python。添加第三方源之前应核对发行版代号和官方步骤；删除包不一定删除用户配置。',
       '1. apt update 会直接升级所有软件吗？\n2. pip 包和 apt 包是同一层吗？',
       '1. 不会，它更新索引。\n2. 不是，分别服务于 Python 环境和系统包管理。',
       r'''## 依赖图

       安装一个应用可能需要多个库，apt 根据版本约束选择依赖。只有一个 .deb 文件不代表依赖已经满足；apt install ./文件.deb 与直接 dpkg -i 的依赖处理不同。

       ## 可复现安装

       记录系统版本、软件版本、来源和环境位置。系统包、虚拟环境与容器有各自边界，不要把“装过同名软件”视为当前命令必定调用它。''')

lesson('system', '03_process_jobs', '进程、前后台与任务结束',
       '识别 PID、父进程与状态，结束自己创建的任务。',
       '程序是文件，进程是程序的一次运行。PID 是当前进程标识；& 让 Shell 不等待任务；jobs 显示本 Shell 管理的作业。Ctrl+C 通常中断前台任务，kill 默认发送 SIGTERM，程序可以处理这个信号后退出。',
       r'''ps -p $$ -o pid,ppid,stat,comm
       sleep 60 &
       linux_lesson_pid=$!
       jobs -l
       ps -p "$linux_lesson_pid" -o pid,ppid,stat,comm
       kill "$linux_lesson_pid"
       wait "$linux_lesson_pid"
       bash scripts/study.sh demo processes''',
       '看到自己创建的 sleep PID；kill 后 wait 可能返回非零，因为进程被信号结束。自动实验会回收自己的子进程并保存 reaped=true。',
       '在同一终端启动 sleep，再使用 Ctrl+Z、jobs、bg、fg，最后 Ctrl+C；解释“暂停”和“退出”。',
       'jobs 只看本 Shell 的作业。不要按常见程序名全局杀进程；PID 也可能被复用，应确认归属。',
       '1. Ctrl+Z 会删除进程吗？\n2. 为何优先正常退出或 SIGTERM？',
       '1. 通常暂停前台作业。\n2. 给程序清理资源、保存数据的机会，SIGKILL 无法被处理。',
       r'''## 生命周期

       父进程启动子进程，子进程退出后父进程应等待并回收退出状态。只看到任务不再打印不能证明它退出；需要 poll、wait 或进程表中的证据。

       ## 资源观察

       top 交互查看 CPU、内存和进程状态，q 退出。CPU 百分比、内存与磁盘占用是不同指标。自动演示只检查自己创建的进程，避免干扰正在运行的 ROS 或训练任务。''')

lesson('system', '04_services_logs', 'systemd 服务、启动项与日志',
       '区分普通进程和受服务管理器管理的服务，查服务状态与日志。',
       'systemd 用 unit 描述服务、定时器等资源。start 是现在启动，enable 是配置未来开机或目标激活时启动；active 与 enabled 描述不同状态。journalctl 查询 systemd 收集的日志。',
       r'''systemctl --version
       systemctl list-units --type=service --state=running --no-pager
       systemctl status cron.service --no-pager
       journalctl -u cron.service -n 20 --no-pager
       # 用户服务另用 systemctl --user；本节先只读观察''',
       '看到正在运行的服务和 cron 状态；服务未安装时可显示 unit not found，日志权限不足或无记录时也应记录。自动检查未执行服务启停。',
       '选择列表中的一个实际服务，记录 active 状态、是否 enabled 及最近三条日志；不要把示例服务名当成本机必然存在的服务。',
       'status 的非零状态可能表示服务未运行。journalctl 可因权限或日志保留策略看不到历史；不能据此断言从未发生事件。',
       '1. enable 会立刻启动服务吗？\n2. --user 与系统服务作用范围一样吗？',
       '1. 单独 enable 通常不会；enable --now 才兼顾立即启动。\n2. 不同，前者管理用户会话的 unit。',
       r'''## 服务依赖与恢复

       服务管理器能安排依赖、记录退出状态和按策略重启。程序立即退出不一定是故障，需看 unit 类型与日志；反复重启可能掩盖原始错误。

       ## 时间维度

       journalctl --since '1 hour ago' 限定时间，-b 限定当前启动，-f 持续观察新日志。先确定服务名与发生时间，再缩小范围；错误等级也不代替业务上下文。''')

lesson('system', '05_network_ssh', 'IP、端口、HTTP、SSH 与文件传输',
       '理解地址与端口，按层次排查连接问题，认识远程操作的边界。',
       'IP 定位网络接口，端口定位服务，DNS 把域名解析为地址。127.0.0.1 指本机，SSH 在远程机器上启动命令会话；远程 Shell 的当前目录属于远程主机。curl 可检查 HTTP 响应。',
       r'''ip -br address
       ip route
       ss -ltn
       ssh -V
       rsync --version | head -n 1
       bash scripts/study.sh demo network
       # 有自己的远程账号时，才替换实际地址执行 ssh 用户名@主机''',
       '自动实验在本机随机端口返回 HTTP 200，随后关闭服务。它验证本机回环通信，不代表互联网、DNS或远程 SSH 已通。',
       '说明 ssh、scp、rsync 分别用于什么；写出一次连接排错的顺序：地址→路由/DNS→端口→协议→认证。',
       'SSH 默认端口常为 22，但服务器可修改；连接失败、认证失败与目录不存在是不同问题。首次主机指纹应按自己的服务器信息核对。',
       '1. 另一台电脑的 127.0.0.1 是本机吗？\n2. HTTP 200 能证明文件内容正确吗？',
       '1. 是那台电脑自己。\n2. 不能，还需检查内容；演示会同时校验响应正文。',
       r'''## 监听地址

       监听 127.0.0.1 只接受本机连接；监听 0.0.0.0 表示所有 IPv4 接口，能否远程访问还受路由与防火墙影响。地址、端口与访问范围需要分别解释。

       ## 传输语法

       scp 本地文件 用户@主机:远端路径 复制文件；rsync -av --dry-run 源目录/ 目标目录/ 预览同步。rsync 源末尾 / 表示复制目录内容。正式同步先确认两端路径与预览，不使用 --delete 做入门练习。''')

lesson('system', '06_storage_mounts', '磁盘空间、挂载与备份排错',
       '区分磁盘、分区、文件系统、目录占用和 inode。',
       'df 从文件系统角度查看容量；du 累加路径占用；lsblk 查看块设备；findmnt 查看实际挂载。文件系统决定文件名、权限、链接等行为，本机仓库位于 ntfs3。',
       r'''lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS
       df -h .
       df -i .
       du -sh course scripts
       findmnt -T . -o TARGET,FSTYPE,OPTIONS
       bash scripts/study.sh project organize''',
       '能把仓库目录对应到挂载和设备。整理项目生成 3 个文件，保留原资料，并校验归档恢复内容；只是同一磁盘上的教学备份。',
       '比较 df 与 du 的对象，解释为何结果不必相等；为自己的重要资料写一份备份位置和恢复验证计划。',
       '容量未满仍可能出现 inode 或配额限制。课程不格式化分区，也不把同盘副本描述成抗磁盘故障的备份。',
       '1. du -sh course 衡量什么？\n2. 同盘备份能应对整盘损坏吗？',
       '1. 该目录树的占用。\n2. 不能，重要资料需要独立介质或可信远端副本。',
       r'''## df 与 du 不一致

       已删除但仍被进程打开的文件可能占用文件系统空间；稀疏文件、硬链接和统计权限也影响比较。先明确比较的挂载与目录范围，不凭一个数值就删除资料。

       ## 本机文件系统约束

       NTFS 挂载参数影响权限呈现，Windows 兼容命名也会限制名称。为课程保留实际 findmnt 报告；链接或 chmod 的行为按本机观察解释。''')

lesson('programming', '01_python_environment', 'Python、解释器、venv 与 Miniforge',
       '明确自己运行哪套 Python，创建仓库内的学习虚拟环境。',
       'Python 文件是源代码，解释器负责执行；包安装到某个解释器的环境。venv 有独立包目录；--system-site-packages 允许读取系统包，降低与 Ubuntu/ROS 依赖的隔阂，但它不等于完全与系统隔离。',
       r'''command -v python3
       /usr/bin/python3 --version
       mkdir -p scripts/runtime
       /usr/bin/python3 -m venv --system-site-packages scripts/runtime/venv
       scripts/runtime/venv/bin/python -c 'import sys; print(sys.executable); print(sys.prefix); print(sys.base_prefix)'
       scripts/runtime/venv/bin/python -m pip --version
       bash scripts/study.sh environment''',
       'venv 的 sys.prefix 在仓库内，sys.base_prefix 指向系统环境。本机默认 python3 来自 Miniforge；study.sh 明确使用系统 Python。无需 pip 安装即可完成本课程。',
       '用系统解释器和 venv 解释器分别打印 sys.executable，写出安装包时应使用哪个 python -m pip。',
       'source 激活并非必要，可直接调用 venv/bin/python。不要混用 Miniforge 的 pip 与系统解释器；ROS 构建继续遵循 ROS 仓库入口。',
       '1. --system-site-packages 是否只读取 venv 包？\n2. python -m pip 有什么好处？',
       '1. 不是，还允许系统包参与搜索。\n2. 明确 pip 属于所指定的解释器。',
       r'''## 包搜索顺序

       sys.path 包含模块搜索目录，PYTHONPATH 和用户 site-packages 可能改变结果。课程主入口用 -I；局部模块示例用 -E -s 保留正常脚本目录导入。

       ## 编译依赖与科研环境

       Python 纯代码和链接到系统库的二进制扩展，兼容要求不同。系统 Python 用于 Ubuntu/ROS 工具，另一个项目可使用独立 Conda 环境；项目间应各自明确入口。''')

lesson('programming', '02_variables_containers', '变量、类型、单位与容器',
       '用变量表达测量值，区分整数、浮点数、字符串、列表与字典。',
       '变量名指向对象；类型决定支持的操作。列表按位置索引，从 0 开始；字典按键访问。物理单位要写进名称或记录，150 mm / 60 mm/s 才能解释为 2.5 s。',
       r'''bash scripts/study.sh python variables
       # 阅读源码中的 variables 分支
       sed -n '1,45p' scripts/programming/python/examples.py
       mkdir -p scripts/practice/python
       # 自己的新程序放 scripts/practice/python/ 下''',
       '打印 int、float、list，并保存 time_s=2.5、samples=[10,20,30]。JSON 是结构化文本，不能只靠终端格式判断数值类型。',
       '新建自己的变量练习，计算 240 mm 以 80 mm/s 运动所需时间；取 samples 的最后一个值，并记录类型。',
       '字符串 "10" 与整数 10 不同；列表越界会报 IndexError；毫米与米混用会产生数量级错误。',
       '1. [10,20,30][0] 是多少？\n2. 240/80 的物理结果是什么？',
       '1. 10。\n2. 3 秒，前提是单位按题目一致。',
       r'''## 运算与类型

       / 是真除法，// 是向下取整除法，% 是余数。例如 5/2=2.5，5//2=2，-5//2=-3。浮点数有限精度，接近结果的比较可使用容差。

       ## 容器与引用

       b=a 不一定复制列表内容，两个变量可能引用同一对象；需要独立副本时可用 a.copy()，嵌套结构还需考虑浅拷贝。课程项目会区分数据原件与输出副本。''')

lesson('programming', '03_control_flow', '条件、循环与算法步骤',
       '将文字规则改写为条件与循环，跟踪中间状态。',
       'if 根据真假选择执行路径，for 按顺序访问元素。缩进表示 Python 的代码块；= 赋值、== 比较。算法先明确输入、筛选条件与输出，再选择代码形式。',
       r'''bash scripts/study.sh python flow
       /usr/bin/python3 -c 'values=[2,5,8,11]; print([x for x in values if x >= 6])'
       # 完整示例用显式 for 和 if，先逐步阅读再理解推导式''',
       '输入 [2,5,8,11]，选择 >=6 的值，得到 [8,11]，和为 19。能解释每次迭代的值与条件真假。',
       '在自己的新文件中把规则换成“选择偶数”；手工列出每一步，得到 [2,8] 与总和 10，再运行确认。',
       '混用 Tab 与空格容易缩进错误。while 要有终止条件；改变循环条件后需重新预测结果。',
       '1. >=6 会选中 6 吗？\n2. 筛选与求和是同一个步骤吗？',
       '1. 会。\n2. 不是，先确定哪些值入选，再累加。',
       r'''## 状态表

       本例四次迭代条件依次为假、假、真、真，selected 依次为 []、[]、[8]、[8,11]。写状态表可以把结果错误定位到筛选条件或更新步骤。

       ## 复杂度的第一步

       对 n 个元素遍历一次，工作量通常随 n 线性增长。先把单次流程写正确，再考虑重复扫描、嵌套循环和大数据规模。''')

lesson('programming', '04_functions', '函数、参数、返回值与作用域',
       '把重复逻辑写成函数，区分打印与返回。',
       '函数为一个有名字的计算步骤定义输入与输出。参数在调用时取得值，return 把结果交给调用者；print 只是显示。局部变量通常只在函数作用域内可见。',
       r'''bash scripts/study.sh python functions
       grep -n -A 5 '^def mean' scripts/programming/python/examples.py
       # 在自己的练习文件里定义并调用 mean，不改原示例''',
       'mean([10,20,30]) 返回 20.0，结果被写入 JSON。空列表在求和前被检查，避免以零为除数。',
       '新建一个 mm_to_m(value) 函数，输入 250 返回 0.25；调用两次并说明参数、返回值和局部变量。',
       '只 print 而未 return 的函数通常返回 None。默认参数如果使用可变列表，会在多次调用间共享对象。',
       '1. print(结果) 可以替代 return 吗？\n2. mean([]) 应怎么办？',
       '1. 不能，显示和返回用途不同。\n2. 明确拒绝空输入或设计并说明专门语义。',
       r'''## 函数契约

       mean 的输入是非空数值序列，输出是算术平均值，空序列引发 ValueError。契约把“何时能调用”和“何时应报错”写清，比只说“计算平均数”更有用。

       ## 纯计算与副作用

       计算函数尽量返回数据，文件保存与打印放在调用层。这让同一算法既能用于终端，也能用于图形界面或 ROS 回调，并便于检查结果。''')

lesson('programming', '05_modules_objects', '模块、import 与对象的入口',
       '把算法与入口分开，区分函数、模块、包和对象。',
       '一个 .py 文件通常可作为模块导入；包组织多个模块。main.py 调用 converter.py 中的函数。对象把状态和操作关联起来，列表、路径也是对象；不必先创建复杂类才能理解对象。',
       r'''bash scripts/study.sh python modules
       cat scripts/programming/python/modules/converter.py
       cat scripts/programming/python/modules/main.py
       /usr/bin/python3 -c 'from pathlib import Path; p=Path("scripts"); print(p.name, p.exists())' ''',
       '30 度约等于 0.523599 弧度；Path 对象的 name 为 scripts，exists() 返回 True。导入 converter 不会自己启动实验。',
       '在自己的新目录建立 unit_converter.py 和 main.py；前者定义 mm_to_m，后者导入调用。解释为何文件名不要叫 json.py。',
       '模块名可能遮蔽标准库；执行入口与被导入时的 __name__ 不同。包、apt 包与 Python 虚拟环境不是同一层。',
       '1. if __name__ == "__main__" 的作用？\n2. Path("scripts").exists() 是函数还是对象方法调用？',
       '1. 直接执行文件时运行入口，被导入时不自动执行该块。\n2. 对象方法调用。',
       r'''## 导入与搜索位置

       普通脚本运行会让脚本目录参与搜索，因此 main.py 可导入同目录 converter.py。-I 会排除这个位置；课程对子模块示例采用 -E -s，而非靠全局修改 PYTHONPATH。

       ## 对象与类

       类定义一类对象的结构，实例是具体对象。p.name 是属性，p.exists() 是方法。需要把多个测量值与操作组织在一起时再写自己的类，先用已有对象建立直觉。''')

lesson('programming', '06_files_errors', '文件、CSV、JSON、异常与输入检查',
       '读取结构化数据，区分格式错误、输入错误与程序错误。',
       'with 管理文件打开与关闭，encoding 明确字符编码。CSV 行中的字段通常先是字符串，需要转数值；JSON 保存列表、字典等结构。try/except 只处理预期异常，其他错误保留上下文便于排查。',
       r'''bash scripts/study.sh python files
       bash scripts/study.sh python errors
       # 每条命令打印各自实验目录；打开对应 result.json 比较
       # CSV 示例含表头 time_s,value 和三条数值记录''',
       '文件课得到 rows=3、mean=20.0。异常课先报告空输入错误，再正常计算 [3,9] 的平均值 6.0，程序没有把错误结果伪装成零。',
       '给自己的 CSV 增加第四条值 40，预测平均值 25；再尝试非数值字符串，记录报错类型与行号。',
       '不要用 except: pass 隐藏问题。相对路径依赖当前目录，跨机器路径应由 Path 组合；Windows 与 Linux 路径分隔方式不同。',
       '1. CSV 中 "20" 如何用于算术？\n2. 空输入返回 0 为什么可能误导？',
       '1. 显式转换为 int 或 float。\n2. 会把“没有数据”混成“测得零”。',
       r'''## 输入、输出与模式

       文本打开模式 r 读取，w 覆盖写入，a 追加；二进制加 b。写文件前需要建立父目录。课程使用独立输出目录保留输入和既有结果。

       ## 可验证的数据处理

       先检查表头、记录数、数据类型与缺失值，再计算。错误日志应记录发生位置和原因；输出存在只说明写入成功，数值正确还需与手算对照。''')

lesson('programming', '07_bash_basics', 'Bash 脚本、变量、参数与条件',
       '把手动命令写成脚本，理解脚本参数与返回状态。',
       'Bash 擅长连接系统命令。变量赋值的等号两侧不加空格，使用时通常写 "$变量"；$1 是第一个参数，$# 是参数数目。[[ ]] 作条件判断，$(( )) 作整数运算。',
       r'''bash scripts/study.sh bash basics
       cat scripts/programming/bash/basics.sh
       bash -n scripts/programming/bash/basics.sh
       # bash -n 只检查语法，不运行脚本''',
       '输出你好与筛选数字之和 19，并保存 result.txt。语法检查通过不等于逻辑正确，所以脚本还校验计算结果。',
       '在自己的新脚本里接收名字参数并用 printf 打招呼；未提供参数时显示清楚的用法。',
       'Bash 赋值 name = value 会被解释为命令。裸变量展开可能分词和展开通配符；set -e 有上下文例外，不是完整的错误处理。',
       '1. "$1" 指什么？\n2. Bash 整数 5/2 是多少？',
       '1. 脚本第一个位置参数。\n2. 在整数算术中为 2，浮点计算交给合适的工具。',
       r'''## 错误处理选项

       set -u 对未定义变量报错，set -o pipefail 让失败的管道成员影响整条管道状态，set -e 在部分未处理非零状态时退出。但 if、逻辑列表等上下文有例外，需要检查命令契约。

       ## Shebang 与执行

       #!/usr/bin/bash 指明直接执行时的解释器。bash 文件.sh 不要求脚本有执行位，./文件.sh 需要执行权限且挂载允许执行。课程统一用 bash 入口。''')

lesson('programming', '08_bash_automation', '遍历文件、批处理与稳健路径',
       '自动处理多个文件，并正确保留空格和特殊字符。',
       '遍历文件不能依赖解析 ls 输出。find -print0 用零字节分隔路径，read -r -d "" 逐个读取；IFS= 避免裁剪空白。程序应先明确输入范围，再处理各文件并统计结果。',
       r'''bash scripts/study.sh bash automation
       cat scripts/programming/bash/automation.sh
       bash -n scripts/programming/bash/automation.sh
       # 示例自动生成“课程 笔记.txt”和 another.txt''',
       '两份文本分别有 2 行与 1 行，总行数是 3。带空格的文件名被当成一个完整路径。',
       '在自己的新脚本里改成统计三个文件的行数，含一个空文件；手工预测后比较，并解释不使用 for f in $(ls) 的理由。',
       'wc -l 前后的空白可影响字符串格式，但可用整数算术处理。批处理如果重写输入，失败后可能无法重跑，应保留原件。',
       '1. -print0 解决什么问题？\n2. 空文件会贡献多少行？',
       '1. 路径含空格或换行时仍能明确分隔。\n2. 零行。',
       r'''## 流与子 Shell

       cmd | while read ... 的循环常在子 Shell 中执行，循环内变量更新可能不回到父 Shell。示例用进程替换 < <(...) 把输入接给当前 Shell 中的循环。

       ## 自动化的完成标准

       需要验证处理对象数、内容统计、输出位置和错误状态；“没有报错”不足以说明全部输入都被处理。Bash 负责调度，复杂数据分析适合交给 Python。''')

lesson('programming', '09_cpp_compilation', 'C++ 源码、编译、链接与可执行文件',
       '编译一个小程序并运行，区分源码、编译器与程序输出。',
       'C++ 源文件先编译成目标代码，再与所需库链接成为可执行文件。g++ 是构建工具，不是程序运行时解释器。命令行参数在 main 的 argc/argv 中提供；返回值影响进程退出状态。',
       r'''bash scripts/study.sh cpp intro
       cat scripts/programming/cpp/angle.cpp
       # 示例：g++ -std=c++17 -g -Wall -Wextra -pedantic 源文件 -o 程序
       # 在本次打印的实验目录中查看 angle 和 cpp.json''',
       '编译成功后，angle 30 输出 0.523599；非数值输入返回状态 2。源文件不变，每次构建与程序都保存在新实验目录。',
       '复制为自己的新源码，增加弧度转角度函数，输入 π/6 应接近 30；同时测试非法参数。',
       '源码改动后需重新编译才能改变可执行程序。警告不一定阻止生成程序，但应理解并处理；整数与浮点除法行为需分清。',
       '1. -o 指定什么？\n2. -g 会提供什么？',
       '1. 输出可执行文件路径。\n2. 调试信息，便于断点与查看源码变量。',
       r'''## 角度换算

       radians = degrees × π / 180。30 度对应 π/6≈0.5235987756，终端按六位小数显示。验证应使用容差，不能要求截断后的打印值逐位等于数学常数。

       ## 输入契约

       程序要求一个完整、有限的数值；30abc、nan 等都拒绝。std::stod 可以部分解析字符串，所以示例额外检查已经消费的字符数。''')

lesson('programming', '10_cmake_debug', 'CMake、构建目录与调试信息',
       '解释 CMake 配置与构建两个阶段，找到生成的程序。',
       'CMake 读取 CMakeLists.txt 生成构建规则，再由 make 等后端调用编译器。源码目录与构建目录分开，避免生成文件混入源码。Debug 构建通常便于调试，不等于程序已经正确。',
       r'''bash scripts/study.sh cpp cmake
       cat scripts/programming/cpp/CMakeLists.txt
       gdb --version | head -n 1
       # 手动调试：gdb 本次实验目录/build/angle
       # 在 gdb 输入：break main；run 30；next；print argc；quit''',
       '能看到配置、编译和运行三个阶段；build/angle 输出相同换算结果。gdb 交互步骤需在自己的终端完成，自动验收没有宣称已验证桌面调试。',
       '在自己的新源码中增加打印，重新构建，说明配置文件变化和源文件变化分别可能触发什么步骤。',
       '改用另一编译器或环境时，不应复用含旧缓存的构建目录。CMake 不是 C++ 编译器；cmake --build 不会自动运行生成程序。',
       '1. -S 与 -B 各指定什么？\n2. CMakeCache.txt 属于源码吗？',
       '1. 源码目录与构建目录。\n2. 不属于，它是配置阶段的生成文件。',
       r'''## 目标与依赖

       add_executable 定义目标，target_compile_features 声明语言标准需求，target_compile_options 增加警告选项。工程变大后，库目标与可执行目标的依赖比拼接长编译命令更清楚。

       ## 可复现构建

       记录编译器版本、构建类型、配置参数与源文件。仓库入口给每次实验独立 build 目录，课程不依赖 ROS 的构建产物，避免跨仓库环境污染。''')

lesson('tools', '01_editors', 'nano、Vim 与文本编辑模式',
       '在终端新建并保存练习文件，掌握退出方式。',
       '编辑器修改文本，Shell 执行命令。nano 的界面底部提示 ^ 代表 Ctrl；Vim 的普通模式执行动作，插入模式输入文字。先练习保存与退出，再增加快捷键。',
       r'''mkdir -p scripts/practice/editor
       nano scripts/practice/editor/nano-note.txt
       # nano：输入文字，Ctrl+O 保存，Enter 确认，Ctrl+X 退出
       vim scripts/practice/editor/vim-note.txt
       # Vim：i 插入，Esc 回普通模式，:wq 保存退出
       cat scripts/practice/editor/nano-note.txt''',
       '两份新笔记保存成功。Vim 放弃尚未保存的修改可用 :q!，普通退出 :q 可能因有改动而拒绝。',
       '给笔记新增三行，在 Vim 中查找其中一个词，再保存；用 cat 确认文件内容与编辑器显示一致。',
       '在 Vim 普通模式敲字母可能触发操作；想输入文字先确认模式。保存前确认路径，课程示例源码只阅读，自己的练习另建。',
       '1. nano 的 ^O 表示什么？\n2. Vim 的 Esc 做什么？',
       '1. Ctrl+O 保存。\n2. 返回普通模式。',
       r'''## 编辑器与文件状态

       编辑器缓冲区可以有尚未写入磁盘的修改。终端中的 cat 读取磁盘文件，不能显示未保存缓冲区。排查“改了却没生效”先检查保存位置和保存动作。

       ## 选择工具

       nano 适合快速配置文本，Vim 适合熟悉键盘模式后高效编辑；VS Code 提供工程导航与调试。它们可以编辑同一种源码，并不决定代码使用哪套解释器。''')

lesson('tools', '02_vscode_debug', 'VS Code 工作区、解释器与断点',
       '打开课程工作区，选择解释器并单步观察变量。',
       'VS Code 是编辑器，Python 扩展提供语言与运行功能，Python Debugger 扩展提供调试。解释器选择、终端激活环境和运行配置可能分别决定运行入口，要查看 sys.executable 确认。',
       r'''mkdir -p scripts/practice/debug
       # 在 Ubuntu 桌面终端打开：
       code scripts/editor/linux-study.code-workspace
       # 扩展：Microsoft Python、Python Debugger
       # 命令面板：Python: Select Interpreter → /usr/bin/python3
       # 在 wrong_mean 的 return 行设断点；运行“平均值错误演示”
       bash scripts/study.sh project debug''',
       '自动项目展示错误平均值 11 与正确值 11.75。桌面断点应看到 values=[10,11,12,14]，sum=47，// 导致向下取整。',
       '用 Step Into 进入函数，用变量面板检查输入；比较 Step Over 和 Continue。把自己的修复放新文件，说明为什么 / 合适。',
       '编辑器选中的解释器不必与一个已打开的终端一致。图形断点操作由学习者实际完成；自动脚本只验证数值与入口。',
       '1. 断点会修改源代码吗？\n2. 47//4 与 47/4 各是多少？',
       '1. 不会，调试器在执行时暂停。\n2. 11 与 11.75。',
       r'''## 调试四步

       给出最小输入，设置断点，观察每一步状态，比较预期与实际。语法错误往往在运行前出现；逻辑错误可能正常结束但结果错误，断点能定位具体运算。

       ## 工程工作区

       提供的 .code-workspace 位于 scripts/editor/，相对引用仓库并配置系统 Python。调试输出放 scripts/practice/debug/；它不会修改用户全局编辑器设置。''')

lesson('tools', '03_git_basics', 'Git 工作区、暂存区与提交',
       '理解 status、diff、add、commit、log 与远端的关系。',
       '工作区是当前文件，暂存区是准备提交的快照，提交是本地历史。add 不上传，commit 不上传，push 才向远端传递提交。Git 记录版本，GitHub 提供远端托管。',
       r'''git status --short --branch
       git log -3 --oneline
       git diff
       git remote -v
       bash scripts/study.sh demo git
       # 想保存自己的代码时，新建 scripts/exercises/ 下的文件
       # 只 add 你准备提交的文件，再用中文写 commit message''',
       '主仓库 origin 指向用户提供的地址；自动演示在独立示例仓库创建历史，没有改动主仓库分支或推送演示内容。',
       '进入本次 example-repository，新增自己的 notes2.md；依次观察未跟踪、已暂存、已提交三个状态，用中文提交。',
       '.gitignore 主要影响未跟踪文件，不会自动移除已跟踪文件。运行结果、虚拟环境和临时练习被忽略，正式练习可放 scripts/exercises/。',
       '1. commit 是否必须联网？\n2. git diff 与 git diff --staged 有何不同？',
       '1. 不必，本地操作。\n2. 前者看未暂存修改，后者看暂存区相对上次提交的变化。',
       r'''## 快照与身份

       每次提交有父提交、作者与说明。主仓库使用已有 Git 身份；自动示例仓库明确设置虚构的课程作者，只为本地演示，不改变全局配置。

       ## 提交范围

       提交前检查 status 与 diff，再 add 指定文件。密码、令牌、环境目录与大量运行输出不作为课程代码提交。中文说明描述做了什么变化，便于回顾。''')

lesson('tools', '04_git_branches', 'Git 分支、合并与同步',
       '读懂分支历史，区分 fetch、pull、merge 与 push。',
       '分支是指向提交的可移动名字。switch 切换工作状态，merge 整合历史，fetch 下载远端历史，pull 再整合到当前分支。冲突是需要选择最终内容的情况，不代表 Git 丢失全部资料。',
       r'''bash scripts/study.sh demo git
       # 在本次 example-repository 中执行以下只读观察
       # git branch -av
       # git log --oneline --graph --all
       # git show HEAD
       # 本地示例没有配置远端，因此不演示真实 pull/push''',
       '看到 main、practice 和一次合并提交；主仓库 main 没被切换。--no-ff 保留演示中的合并节点，便于观察历史结构。',
       '在示例仓库创建另一分支，新增一个独立文件并提交，再合并回 main；预测提交图变化。',
       '不要用强制推送或硬重置处理看不懂的同步问题。合并前确认工作区状态；真实远端操作要针对正确仓库与分支。',
       '1. fetch 会直接修改当前文件吗？\n2. 分支一定是一个复制出来的目录吗？',
       '1. 通常只更新远端历史引用，不直接整合工作区。\n2. 不是，它是历史引用，工作目录随切换呈现相应内容。',
       r'''## 快进与三方合并

       如果当前提交是目标分支的祖先，合并可直接移动分支指针，称快进。历史已经分叉时，Git 按共同祖先与两边变化整合；同一位置的不同修改可能冲突。

       ## 同步节奏

       先获取并检查远端，再决定合并；核对本地结果后推送。课程的主仓库交付沿原 main 历史追加，不覆盖已有远端历史。''')

lesson('tools', '05_tmux', 'tmux 会话、窗口与面板',
       '理解终端窗口与 tmux 会话分离，掌握分离和重新连接。',
       'tmux 服务器维护会话，会话有窗口，窗口有面板。关闭终端客户端不一定结束会话；Ctrl+b 是默认前缀，需要先按前缀，再按动作键。socket 决定连接哪一个 tmux 服务器。',
       r'''bash scripts/study.sh demo tmux
       # 自己在桌面终端练习：
       # tmux new -s linux-study
       # Ctrl+b 再按 %：左右分屏；Ctrl+b 再按 "：上下分屏
       # Ctrl+b 再按 d：分离
       # tmux attach -t linux-study
       # 在练习 Shell 输入 exit 结束相应面板''',
       '自动演示在独立 socket 上建立 lesson，会话列表可见，最后关闭自己的服务器。手动练习需要自己确认窗口、面板和分离状态。',
       '一个面板阅读日志，另一个执行命令；分离后重新连接，解释哪些任务仍在运行。只清理自己的练习会话。',
       'tmux 不保证机器关机后程序继续运行。不要执行不带限定范围的 kill-server 去清理不明会话。',
       '1. 分离等于退出 Shell 吗？\n2. 独立 socket 的意义？',
       '1. 不等于，只断开客户端。\n2. 分隔服务器与会话范围，避免干扰现有任务。',
       r'''## 终端与任务寿命

       远程连接断开时，普通前台任务可能受影响；tmux 的会话服务器与连接客户端分离。长任务仍需要程序自己的日志、检查点和错误处理。

       ## 资源归属

       会话名便于识别任务，socket 提供更明确的隔离。课程自动示例仅在自己生成的路径启动和关闭服务器，不按进程名全局清理。''')

lesson('tools', '06_docker_optional', 'Docker 镜像、容器与挂载（选修）',
       '理解容器的环境边界，读懂一个最小 docker run 命令。',
       '镜像提供文件系统和启动配置，容器是镜像的一次运行。容器共享宿主机内核，不能等同于完整虚拟机。挂载把宿主机目录提供给容器；:ro 表示只读。本课不依赖 Docker 完成主线。',
       r'''docker --version
       docker context show
       # 以下手动实验需 Docker daemon 可用，并会下载镜像：
       # mkdir -p scripts/practice/docker
       # printf 'hello\n' > scripts/practice/docker/note.txt
       # docker run --rm --mount "type=bind,src=$PWD/scripts/practice/docker,dst=/lesson,readonly" python:3.10-slim python -c 'from pathlib import Path; print(Path("/lesson/note.txt").read_text())'
       # 更严格复现应记录实际镜像 digest，标签本身可能变化''',
       '客户端版本可查询，但这不证明 daemon 可用。手动示例应打印 hello，容器退出后 --rm 清理容器，宿主机 note.txt 保留；本次自动验收不下载镜像。',
       '画出宿主机路径与容器 /lesson 的映射；解释镜像、容器、挂载目录各在哪里，以及只读限制作用于谁。',
       'docker 组通常提供很高的主机权限，不为完成课程自动改用户组。--rm 不删除下载的镜像；镜像标签可能随时间更新。',
       '1. 容器有自己的 Linux 内核吗？\n2. --rm 会删除绑定挂载的宿主文件吗？',
       '1. 通常共享宿主内核。\n2. 不会，它清理退出后的容器对象。',
       r'''## 客户端、daemon 与权限

       docker 命令通过 socket 与 daemon 通信。客户端已安装但 daemon 未运行、上下文不正确或权限不足时，docker ps 仍会失败。安装与权限步骤应看当前官方 Ubuntu 文档。

       ## 与 venv 的比较

       venv 主要分隔 Python 包；容器分隔进程视图和用户空间文件，但仍共享内核。GPU、GUI、ROS 网络和设备访问需要额外配置，不能从这个文本示例推断它们已可用。''')


def main():
    import os
    manifest = []
    for index, item in enumerate(LESSONS):
        folder, prefix, _, _ = GROUPS[item['group']]
        number = sum(1 for old in LESSONS[:index + 1] if old['group'] == item['group'])
        identifier = f'{prefix}{number:02d}'
        directory = ROOT / 'course' / folder / item['slug']
        directory.mkdir(parents=True, exist_ok=True)
        overview = os.path.relpath(ROOT / 'course/README.md', directory)
        resources = os.path.relpath(ROOT / 'docs/RESOURCES.md', directory)
        navigation = [f'[课程总览]({overview})', '[理论补充](THEORY.md)']
        for offset, label in ((-1, '上一课'), (1, '下一课')):
            if 0 <= index + offset < len(LESSONS):
                adjacent = LESSONS[index + offset]
                adjacent_dir = ROOT / 'course' / GROUPS[adjacent['group']][0] / adjacent['slug']
                navigation.append(f'[{label}]({os.path.relpath(adjacent_dir / "README.md", directory)})')
        readme = f'''# {identifier}：{item['title']}

{' · '.join(navigation)}

## 学习目标

{item['goal']}

## 先理解

{item['concept']}

## 预测，再操作

先用一句话预测结果。命令从仓库根目录执行；连续的 `cd` 步骤在同一终端完成。以 `#` 开头的行是说明或待手动选择的步骤。自动入口会打印本次独立实验目录。

```bash
{item['commands']}
```

## 观察与完成标准

{item['expected']}

## 自己动手

{item['exercise']}

记录输入、实际结果与原因。自己的新源码放 `scripts/` 下；不要改课程原示例。`scripts/practice/` 是忽略提交的草稿区，完成后想保存版本的作品可放 `scripts/exercises/`。

## 常见错误

{item['pitfalls']}

## 自检

{item['questions']}

<details>
<summary>完成后查看参考答案</summary>

{item['answers']}

</details>

继续阅读[理论补充](THEORY.md)，再用自己的话解释操作。参考资料见[官方资源与版本说明]({resources})。
'''
        theory = f'''# {identifier} 理论补充：{item['title']}

[回到操作课](README.md) · [课程总览]({overview})

{item['theory']}

## 把原理对应到本课

{item['concept']}

核对本课的输入、命令作用范围与完成标准。尝试只改变一个条件，先预测，再对照实际结果；没有验证过的桌面、远程或管理员步骤不要记成已通过。

参考资料见[官方资源与版本说明]({resources})。
'''
        (directory / 'README.md').write_text(readme, encoding='utf-8')
        (directory / 'THEORY.md').write_text(theory, encoding='utf-8')
        manifest.append({'id': identifier, 'group': item['group'], 'title': item['title'],
                         'readme': str((directory / 'README.md').relative_to(ROOT)),
                         'theory': str((directory / 'THEORY.md').relative_to(ROOT))})
    for group, (folder, _, title, description) in GROUPS.items():
        destination = ROOT / 'course' / folder
        items = [row for row in manifest if row['group'] == group]
        lines = [f'# {title}', '', description, '',
                 f'[课程总览]({os.path.relpath(ROOT / "course/README.md", destination)})', '',
                 '| 顺序 | 课程 |', '| --- | --- |']
        lines.extend(f'| {row["id"]} | [{row["title"]}]({os.path.relpath(ROOT / row["readme"], destination)}) |' for row in items)
        lines.extend(['', '每节先读 README，再读 THEORY，完成练习和自检后继续。', ''])
        (destination / 'README.md').write_text('\n'.join(lines), encoding='utf-8')
    assets = ROOT / 'scripts/assets'
    assets.mkdir(parents=True, exist_ok=True)
    (assets / 'course_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = ['# 课程总览与学习路线', '',
             '面向零基础，主环境为 Ubuntu 22.04。共 36 节，T06 Docker 为选修。课程与运行示例各自独立，不需要加载 ROS 或 cv 的环境。', '',
             '从 U01 开始，依次完成 Ubuntu、终端、系统管理、编程与工具课。开始写程序时可提前学习 T01/T02；需要记录自己的版本时穿插 T03/T04。', '',
             '每节按“理解→预测→运行→观察→改一个条件→解释→自检”学习。自动命令从仓库根目录运行；运行前查看本课目标，不必一口气执行全部代码。', '',
             '| 顺序 | 课程 |', '| --- | --- |']
    for row in manifest:
        lines.append(f'| {row["id"]} | [{row["title"]}]({Path(row["readme"]).relative_to("course")}) |')
    lines += ['', '## 综合练习', '',
              '- [资料整理与备份](../projects/organize/README.md)：C03/C08、S06、P06 之后。',
              '- [日志分析](../projects/logs/README.md)：C05/C06、P03/P06 之后。',
              '- [平均值程序调试](../projects/debug/README.md)：P04/P06、T02 之后。', '',
              '## 节奏与完成标准', '',
              '建议每次 30～60 分钟学一节，分两次完成较长实验；可用 8～12 周推进，不设强制周作业。第一轮掌握日常与终端，再学系统排错和 Python，最后串联工具与项目。', '',
              '一节完成意味着：能解释命令或代码的输入与输出；能独立重做核心步骤；改一个条件后能预测变化；能回答自检并保存自己的记录。一次命令成功不能代替理解。', '',
              '## 学习辅助', '',
              '- [术语表](GLOSSARY.md)',
              '- [命令速查](CHEATSHEET.md)',
              '- [练习记录模板](../scripts/templates/study_record.md)',
              '- [运行指南](../scripts/README.md)',
              '- [故障处理](../docs/TROUBLESHOOTING.md)',
              '- [验证范围](../docs/VALIDATION.md)', '']
    (ROOT / 'course/README.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f'已生成 {len(manifest)} 节操作课与理论页，以及模块导航。')


if __name__ == '__main__':
    main()
