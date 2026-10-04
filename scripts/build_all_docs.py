"""完整重建入口：先保留原基础生成方式，再生成进阶及总目录。"""
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parent.parent


if __name__=='__main__':
    for script in ('build_course_docs.py','build_advanced_docs.py'):
        subprocess.run(['/usr/bin/python3','-I',str(ROOT/'scripts'/script)],cwd=ROOT,check=True)
