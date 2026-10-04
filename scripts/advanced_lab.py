"""24 节进阶课的独立实验入口；基础源码保持不变。"""
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict
import fcntl
import hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
from pathlib import Path
import resource
import shutil
import subprocess
import sys
import tarfile
import threading
import time
import urllib.error
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parent/'advanced'))
from support import ROOT, PYTHON, environment, execute, fixture, new_run, save
from event_model import Event

NAMES = ('quoting','text','paths','signals','cli','atomic','proc','timing','http',
         'ssh-config','systemd','backup','objects','tests','packaging','concurrency',
         'cpp','debugging','git','containers','reading','reproduce','incident','capstone')
SOURCE = ROOT/'scripts/advanced'


def cli(path, source, output, *extra, expected=(0,)):
    return execute([PYTHON,'-E','-s',SOURCE/'log_cli.py','--input',source,
                    '--output',output,*extra],path,expected=expected)


def build_cpp(path):
    execute(['/usr/bin/cmake','-S',SOURCE/'cpp','-B',path/'build','-DCMAKE_BUILD_TYPE=Debug'],path)
    execute(['/usr/bin/cmake','--build',path/'build','--parallel','2'],path)
    execute(['/usr/bin/ctest','--test-dir',path/'build','--output-on-failure'],path)
    return path/'build/angle_advanced'


def doctor():
    path = new_run('doctor')
    tools = {name:shutil.which(name) for name in
             ('bash','awk','sed','find','xargs','flock','rsync','strace','gdb','git','cmake','ctest','ssh','curl','systemd-analyze','docker')}
    report = {'python':sys.executable,'version':sys.version.split()[0],'tools':tools,
              'mount':execute(['/usr/bin/findmnt','-T',ROOT,'-o','TARGET,FSTYPE'],path).stdout}
    save(path,'environment.json',report)
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return path


def lab(name):
    path = new_run(name)
    report = {'lab':name,'checks':[]}
    if name == 'quoting':
        (path/'one.txt').write_text('one')
        script = 'value="two words"; printf "%s\\n" "$value"; printf "%s\\n" *.txt; printf "%s\\n" "*.txt"'
        result = execute(['/usr/bin/bash','--noprofile','--norc','-c',script],path)
        assert result.stdout.splitlines() == ['two words','one.txt','*.txt']
        report['checks']=['双引号保留空格','裸通配符展开','带引号通配符保留字面量']
    elif name == 'text':
        (path/'values.csv').write_text('name,value\na,10\nb,20\nc,30\n')
        result = execute(['/usr/bin/awk','-F,','NR>1 {sum+=$2; n++} END {print sum/n}','values.csv'],path)
        assert float(result.stdout) == 20
        result = execute(['/usr/bin/sed','s/^b,/beta,/','values.csv'],path)
        assert 'beta,20' in result.stdout and 'b,20' in (path/'values.csv').read_text()
        report['checks']=['awk 均值 20','sed 输出改变而输入不变']
    elif name == 'paths':
        folder = path/'files'; folder.mkdir()
        names = ['课程 笔记.txt','another.txt','-option.txt']
        for item in names: (folder/item).write_text(item)
        try:
            (folder/'line\nbreak.txt').write_text('newline name')
            names.append('line\nbreak.txt')
            report['newline_name']='当前文件系统允许'
        except OSError as error:
            report['newline_name']=f'当前文件系统不允许：{error.strerror}'
        script = 'find files -type f -print0 | xargs -0 /usr/bin/python3 -I -c \'import json,sys; print(json.dumps(sys.argv[1:],ensure_ascii=False))\''
        result = execute(['/usr/bin/bash','-o','pipefail','-c',script],path)
        observed=json.loads(result.stdout)
        assert set(observed)=={'files/'+item for item in names}
        report['checks']=[f'NUL 分隔完整保留 {len(names)} 个路径']
    elif name == 'signals':
        child=subprocess.Popen([PYTHON,'-I',SOURCE/'worker.py','graceful',path],cwd=path,env=environment(path))
        try:
            deadline=time.monotonic()+5
            while not (path/'ready.json').exists():
                if child.poll() is not None or time.monotonic()>deadline: raise RuntimeError('进程未准备就绪')
                time.sleep(0.02)
            assert json.loads((path/'ready.json').read_text())['pid']==child.pid
            child.terminate(); child.wait(timeout=5)
            assert child.returncode==0
            assert json.loads((path/'stopped.json').read_text())['clean_exit']
        finally:
            if child.poll() is None: child.kill(); child.wait(timeout=5)
        report['checks']=['SIGTERM 被处理','finally 保存退出标记','子进程已回收']
    elif name == 'cli':
        source=fixture(path)
        cli(path,source,path/'report.json')
        value=json.loads((path/'report.json').read_text())
        assert value['valid_records']==8 and value['error_rate']==0.375
        assert value['mean_duration_ms']==45 and len(value['invalid_records'])==1
        cli(path,source,path/'strict.json','--strict',expected=(3,))
        cli(path,source,path/'threshold.json','--max-error-rate','0.2',expected=(4,))
        original=(path/'report.json').read_bytes()
        cli(path,source,path/'report.json',expected=(2,))
        assert (path/'report.json').read_bytes()==original
        report['checks']=['8 条合法记录','3/8 错误率','格式问题状态 3','阈值状态 4','拒绝覆盖状态 2']
    elif name == 'atomic':
        (path/'counter.txt').write_text('0')
        children=[subprocess.Popen([PYTHON,'-I',SOURCE/'worker.py','increment',path],cwd=path,env=environment(path)) for _ in range(2)]
        try:
            for child in children:
                child.wait(timeout=10); assert child.returncode==0
        finally:
            for child in children:
                if child.poll() is None: child.kill(); child.wait(timeout=3)
        assert int((path/'counter.txt').read_text())==40
        assert not list(path.glob('counter-*.tmp'))
        report['checks']=['两个进程各累加 20 次，结果 40','同文件系统原子替换','无残留临时文件']
    elif name == 'proc':
        fields={line.split(':',1)[0]:line.split(':',1)[1].strip() for line in Path('/proc/self/status').read_text().splitlines() if ':' in line}
        report.update(pid=os.getpid(),status={key:fields.get(key) for key in ('Name','Threads','VmRSS')},
                      open_file_limit=resource.getrlimit(resource.RLIMIT_NOFILE),maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        assert int(fields['Threads'])>=1
        report['checks']=['只读自己的 /proc 状态','资源上限未修改']
    elif name == 'timing':
        values=[i%31 for i in range(800)]
        timings={}; answers=[]
        def repeated_scan():
            return sum(values.count(x) for x in values)
        def counted():
            counts=Counter(values)
            return sum(counts[x] for x in values)
        for label,function in (('repeated_scan',repeated_scan),('counter',counted)):
            times=[]
            for _ in range(3):
                start=time.perf_counter(); answer=function(); times.append(time.perf_counter()-start)
            timings[label]=times; answers.append(answer)
        assert answers[0]==answers[1]
        trace=execute(['/usr/bin/strace','-c','-o',path/'strace-summary.txt',PYTHON,'-I','-c','print(2+3)'],path,expected=None)
        report.update(timings_s=timings,strace='verified' if trace.returncode==0 else f'不可用：{trace.stderr.strip()}')
        report['checks']=['两种算法结果相同','三次计时原值已记录']
    elif name == 'http':
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                code={'/health':200,'/protected':401}.get(self.path,404)
                data=json.dumps({'status':code}).encode()
                self.send_response(code); self.send_header('Content-Length',str(len(data))); self.end_headers(); self.wfile.write(data)
            def log_message(self,*args): pass
        server=HTTPServer(('127.0.0.1',0),Handler)
        thread=threading.Thread(target=server.serve_forever,daemon=True); thread.start()
        try:
            base=f'http://127.0.0.1:{server.server_port}'
            for suffix,expected in (('/health',0),('/missing',22),('/protected',22)):
                result=execute(['/usr/bin/curl','--noproxy','*','-sS','-f',base+suffix],path,expected=(expected,))
                if suffix=='/health': assert json.loads(result.stdout)['status']==200
            report['checks']=['HTTP 200 正文','404/401 在 curl -f 下为状态 22']
        finally:
            server.shutdown(); server.server_close(); thread.join(timeout=3)
        assert not thread.is_alive()
    elif name == 'ssh-config':
        config=path/'ssh_config'
        config.write_text('Host lesson\n  HostName 127.0.0.1\n  User student\n  Port 2222\n  ServerAliveInterval 30\n  LocalForward 127.0.0.1:9000 127.0.0.1:8000\n')
        result=execute(['/usr/bin/ssh','-G','-F',config,'lesson'],path,echo=False)
        assert 'hostname 127.0.0.1' in result.stdout and 'port 2222' in result.stdout
        report['checks']=['离线解析配置，端口 2222','只配置本机转发地址']; report['connection']='未连接远端'
    elif name == 'systemd':
        service=path/'lesson-report.service'; timer=path/'lesson-report.timer'
        service.write_text('[Unit]\nDescription=Linux lesson report\n[Service]\nType=oneshot\nExecStart=/usr/bin/python3 -I -c "print(5)"\n')
        timer.write_text('[Unit]\nDescription=Linux lesson timer\n[Timer]\nOnCalendar=hourly\nPersistent=true\nUnit=lesson-report.service\n[Install]\nWantedBy=timers.target\n')
        execute(['/usr/bin/systemd-analyze','verify','--man=no',service,timer],path)
        execute(['/usr/bin/systemd-analyze','calendar','--iterations=2','hourly'],path)
        report['checks']=['unit 静态验证','日历表达式解析']; report['activation']='未安装或启用 unit'
    elif name == 'backup':
        source=path/'input'; source.mkdir()
        (source/'changed.txt').write_text('version 1'); (source/'unchanged.txt').write_text('same')
        first=path/'snapshot1'; second=path/'snapshot2'
        execute(['/usr/bin/rsync','-a',str(source)+'/',str(first)+'/'],path)
        (source/'changed.txt').write_text('version 2'); (source/'new.txt').write_text('new')
        execute(['/usr/bin/rsync','-a','--checksum','--link-dest='+str(first),str(source)+'/',str(second)+'/'],path)
        assert (first/'changed.txt').read_text()=='version 1'
        assert (second/'changed.txt').read_text()=='version 2'
        assert (second/'unchanged.txt').read_text()=='same'
        linked=(first/'unchanged.txt').stat().st_ino==(second/'unchanged.txt').stat().st_ino
        report.update(unchanged_hardlink=linked)
        report['checks']=['旧快照保留 v1','新快照包含 v2 与新文件','记录未变文件是否共享 inode']
    elif name == 'objects':
        event=Event.from_row({'timestamp':'2026-10-05T09:00:00','level':'INFO','component':'app','duration_ms':'12.5'})
        assert event.duration_ms==12.5
        try: Event.from_row({'timestamp':'invalid'})
        except ValueError: pass
        else: raise AssertionError('缺失输入未被拒绝')
        report.update(event=asdict(event)); report['checks']=['字符串转数值','dataclass 序列化','缺失字段拒绝']
    elif name == 'tests':
        result=execute([PYTHON,'-E','-s','-m','unittest','discover','-s',SOURCE/'tests','-v'],path)
        print(result.stderr.rstrip()); assert 'OK' in result.stderr
        report['checks']=['合法、非法、空输入','状态 2/3/4/5','已有输出保留']
    elif name == 'packaging':
        copied=path/'source'; shutil.copytree(SOURCE/'package',copied)
        venv=path/'venv'
        execute([PYTHON,'-I','-m','venv','--system-site-packages',venv],path)
        python=venv/'bin/python'; dist=path/'dist'
        execute([python,'-m','pip','wheel','--no-index','--no-deps','--no-build-isolation','--wheel-dir',dist,copied],path)
        wheels=list(dist.glob('*.whl')); assert len(wheels)==1
        execute([python,'-m','pip','install','--no-index','--no-deps',wheels[0]],path)
        output=execute([venv/'bin/linux-greet','--name','Ubuntu'],path).stdout
        assert output.strip()=='你好，Ubuntu！'
        report['checks']=['离线构建 wheel','安装到本次 venv','已安装命令输出正确']
    elif name == 'concurrency':
        values=list(range(12))
        with ThreadPoolExecutor(max_workers=3) as pool:
            result=list(pool.map(lambda x:x*x,values))
        assert result==[x*x for x in values]
        report.update(input=values,output=result); report['checks']=['所有任务完成','map 返回顺序与输入一致','线程池关闭']
    elif name == 'cpp':
        binary=build_cpp(path)
        result=execute([binary,'30'],path)
        assert abs(float(result.stdout)-0.5235987756)<1e-6
        report['checks']=['库目标与程序链接','CTest 数值检查通过']
    elif name == 'debugging':
        binary=build_cpp(path)
        debug=execute(['/usr/bin/gdb','-nx','-batch','-ex','set debuginfod enabled off','-ex','break main','-ex','run 30','-ex','print argc',binary],path,expected=None)
        if debug.returncode==0 and '$1 = 2' in debug.stdout: report['gdb']='verified'
        else: report['gdb']='当前环境无法完成断点，查看命令证据并手动练习'
        faulty=path/'bounds-error'
        execute(['/usr/bin/g++','-std=c++17','-g','-O0','-fsanitize=address','-fno-omit-frame-pointer',SOURCE/'cpp/bounds_error.cpp','-o',faulty],path)
        result=execute([faulty],path,expected=None,echo=False)
        (path/'asan.txt').write_text(result.stderr)
        assert result.returncode!=0 and 'heap-buffer-overflow' in result.stderr
        report['checks']=['AddressSanitizer 定位堆越界','错误程序返回非零状态']
    elif name == 'git':
        def initialize(directory):
            directory.mkdir()
            for args in (('init','-b','main'),('config','user.name','课程示例作者'),
                         ('config','user.email','student@example.invalid'),('config','commit.gpgsign','false')):
                execute(['/usr/bin/git',*args],path,cwd=directory,echo=False)
        def git(directory,*args,expected=(0,)):
            return execute(['/usr/bin/git',*args],path,cwd=directory,expected=expected,echo=False)
        repo=path/'conflict-example'; initialize(repo)
        file=repo/'settings.txt'; file.write_text('mode=base\n')
        git(repo,'add','settings.txt'); git(repo,'commit','-m','建立共同起点')
        git(repo,'switch','-c','feature'); file.write_text('mode=feature\n')
        git(repo,'commit','-am','修改实验分支配置')
        git(repo,'switch','main'); file.write_text('mode=main\n')
        git(repo,'commit','-am','修改主分支配置')
        git(repo,'merge','feature',expected=(1,)); assert git(repo,'ls-files','-u').stdout.strip()
        git(repo,'merge','--abort'); assert file.read_text()=='mode=main\n'
        git(repo,'merge','feature',expected=(1,)); file.write_text('mode=combined\nnotes=main+feature\n')
        git(repo,'add','settings.txt'); git(repo,'commit','-m','解决配置冲突并保留双方意图')
        assert not git(repo,'status','--porcelain').stdout.strip()
        bisect=path/'bisect-example'; initialize(bisect)
        probe=bisect/'probe.py'; probe.write_text('from pathlib import Path\nraise SystemExit(1 if Path("value.txt").read_text()=="bad" else 0)\n')
        commits=[]
        for i in range(5):
            (bisect/'value.txt').write_text('bad' if i>=3 else 'good')
            (bisect/'version.txt').write_text(str(i))
            git(bisect,'add','.'); git(bisect,'commit','-m',f'记录第{i}版演示')
            commits.append(git(bisect,'rev-parse','HEAD').stdout.strip())
        try:
            git(bisect,'bisect','start','HEAD',commits[0])
            git(bisect,'bisect','run',PYTHON,'-I','probe.py')
            assert git(bisect,'rev-parse','HEAD').stdout.strip()==commits[3]
        finally: git(bisect,'bisect','reset')
        report['checks']=['真实冲突','abort 恢复原状态','解决后提交干净','bisect 找到首个坏提交']
    elif name == 'containers':
        copied=path/'container'; shutil.copytree(ROOT/'scripts/templates/container',copied)
        dockerfile=(copied/'Dockerfile').read_text()
        assert 'COPY app.py .' in dockerfile and 'CMD ["python", "app.py"]' in dockerfile
        result=execute(['/usr/bin/docker','compose','-f',copied/'compose.yaml','config','--format','json'],path,expected=None,echo=False)
        if result.returncode==0:
            config=json.loads(result.stdout); assert config['services']['lesson']['read_only']
            report['compose']='configuration verified'
        else: report['compose']='插件不可用，请手动验证配置；未运行容器'
        report['checks']=['Dockerfile 入口存在']; report['runtime']='未启动 daemon、构建镜像或容器'
    elif name == 'reading':
        package=SOURCE/'package'
        files=sorted(str(item.relative_to(package)) for item in package.rglob('*') if item.is_file())
        assert 'pyproject.toml' in files and 'src/linux_greeting/cli.py' in files
        report.update(files=files,entrypoint='setup.cfg → linux_greeting.cli:main')
        report['checks']=['从构建声明找到源码','从 console_scripts 找到入口']
    elif name == 'reproduce':
        bundle=path/'bundle'; bundle.mkdir()
        shutil.copy2(SOURCE/'experiment.py',bundle/'experiment.py')
        save(bundle,'parameters.json',{'seed':71,'count':10})
        execute([PYTHON,'-I','experiment.py','parameters.json','result.json'],path,cwd=bundle)
        digest=lambda item:hashlib.sha256(item.read_bytes()).hexdigest()
        manifest={'python':sys.version.split()[0], 'command':['python3','-I','experiment.py','parameters.json','result.json'],
                  'sha256':{item.name:digest(item) for item in bundle.iterdir()}}
        save(bundle,'manifest.json',manifest)
        with tarfile.open(path/'experiment.tar.gz','w:gz') as archive:
            for item in sorted(bundle.iterdir()): archive.add(item,arcname=item.name)
        restored=path/'restored'; restored.mkdir()
        with tarfile.open(path/'experiment.tar.gz') as archive:
            for name in ('experiment.py','parameters.json','result.json','manifest.json'):
                (restored/name).write_bytes(archive.extractfile(name).read())
        for name,digest_value in manifest['sha256'].items(): assert digest(restored/name)==digest_value
        execute([PYTHON,'-I','experiment.py','parameters.json','replayed.json'],path,cwd=restored)
        assert (restored/'replayed.json').read_bytes()==(bundle/'result.json').read_bytes()
        report['checks']=['源码/输入/输出摘要','归档恢复','同环境重跑结果逐字节一致']
    elif name == 'incident':
        failure=cli(path,path/'missing.csv',path/'missing-report.json',expected=(2,))
        assert '输入或输出错误' in failure.stderr
        source=fixture(path)
        cli(path,source,path/'threshold-report.json','--max-error-rate','0.2',expected=(4,))
        cli(path,source,path/'accepted-report.json','--max-error-rate','0.5')
        report['checks']=['缺失输入定位为状态 2','阈值超限状态 4','合理阈值下状态 0']
        report['cause']='三种条件不同，不能只用“运行失败”概括'
    elif name == 'capstone':
        source=fixture(path)
        cli(path,source,path/'report.json','--max-error-rate','0.5')
        data=json.loads((path/'report.json').read_text())
        assert data['valid_records']==8 and data['error_rate']==0.375
        cli(path,source,path/'threshold.json','--max-error-rate','0.2',expected=(4,))
        with tarfile.open(path/'inspection.tar.gz','w:gz') as archive:
            for name in ('events.csv','report.json','threshold.json'): archive.add(path/name,arcname=name)
        with tarfile.open(path/'inspection.tar.gz') as archive:
            assert archive.extractfile('report.json').read()==(path/'report.json').read_bytes()
        report['checks']=['参数化巡检','异常行报告','阈值状态','归档内容一致']
    save(path,'lab.json',report)
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return path


def validate():
    path=new_run('validate')
    execute([PYTHON,'-I',ROOT/'scripts/validate_all.py',path],path)
    return path


def smoke():
    path=new_run('smoke'); results=[]
    tasks=[('doctor',doctor)]+[(name,lambda n=name:lab(n)) for name in NAMES]+[('validate',validate)]
    for name,function in tasks:
        print(f'\n检查：{name}',flush=True)
        try: results.append({'task':name,'status':'passed','path':str(function())})
        except Exception as error:
            results.append({'task':name,'status':'failed','error':str(error)})
            save(path,'smoke.json',results); raise
    save(path,'smoke.json',results)
    print(f'全部 {len(results)} 项完成。证据：{path/"smoke.json"}')


def main():
    parser=argparse.ArgumentParser(description='Linux 进阶课独立入口')
    sub=parser.add_subparsers(dest='action',required=True)
    for name in ('doctor','validate','smoke'): sub.add_parser(name)
    target=sub.add_parser('lab'); target.add_argument('name',choices=NAMES)
    args=parser.parse_args()
    if args.action=='lab': lab(args.name)
    else: {'doctor':doctor,'validate':validate,'smoke':smoke}[args.action]()


if __name__=='__main__':
    try: main()
    except (OSError,RuntimeError,ValueError,AssertionError,subprocess.SubprocessError) as error:
        print(f'进阶实验未通过：{error}',file=sys.stderr)
        raise SystemExit(1)
