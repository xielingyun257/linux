"""验证完整 60 节课程、新入口与原有源码不变。"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parent.parent


def run(args):
    result=subprocess.run([str(x) for x in args],cwd=ROOT,capture_output=True,text=True,timeout=40)
    if result.returncode: raise AssertionError(result.stdout+result.stderr)
    return result.stdout


def main(output):
    original=output/'base-validation'; original.mkdir()
    print(run(['/usr/bin/python3','-I',ROOT/'scripts/validate_course.py',original]).rstrip())
    base=json.loads((ROOT/'scripts/assets/course_manifest.json').read_text())
    advanced=json.loads((ROOT/'scripts/assets/advanced_manifest.json').read_text())
    assert len(base)==36 and len(advanced)==24
    assert Counter(row['group'] for row in advanced)=={'shell':6,'systems':6,'engineering':8,'workflows':4}
    assert len({row['id'] for row in base+advanced})==60
    for row in advanced:
        readme=(ROOT/row['readme']).read_text(encoding='utf-8')
        theory=(ROOT/row['theory']).read_text(encoding='utf-8')
        for heading in ('前置知识','原理与步骤','动手实验','结果与边界','变式练习','自检'):
            assert f'## {heading}' in readme,(row['id'],heading)
        assert len(theory)>400,(row['id'],'理论页过短')
    baseline=json.loads((ROOT/'scripts/assets/baseline_sources.json').read_text())
    for name,digest in baseline.items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,f'原有源码发生变化：{name}'
    rows=json.loads(run(['/usr/bin/bash','scripts/learn.sh','catalog','--json']))
    assert len(rows)==60
    store=output/'example-progress.json'
    run(['/usr/bin/bash','scripts/learn.sh','record','H01','--status','done','--note','验证用记录','--store',store])
    progress=json.loads(run(['/usr/bin/bash','scripts/learn.sh','progress','--json','--store',store]))
    assert progress['done']==1 and progress['records']['H01']['note']=='验证用记录'
    invalid=subprocess.run(['/usr/bin/bash','scripts/learn.sh','record','UNKNOWN','--store',store],cwd=ROOT,capture_output=True,text=True)
    assert invalid.returncode==2
    assert json.loads(store.read_text())['records']==progress['records']
    report={'base_lessons':36,'advanced_lessons':24,'total_lessons':60,
            'original_sources_unchanged':len(baseline),'catalog_entries':len(rows),
            'progress_roundtrip':True,'invalid_id_preserves_progress':True,
            'documents':json.loads((original/'validation.json').read_text())}
    (output/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'全课程通过：基础 36 + 进阶 24；原有 {len(baseline)} 个源码摘要未变；目录与进度往返有效。')


if __name__=='__main__': main(Path(sys.argv[1]))
