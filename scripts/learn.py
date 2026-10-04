"""课程目录与由学习者主动填写的本地进度。运行实验不会自动标完成。"""
import argparse
from datetime import datetime, timezone
import fcntl
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent


def catalog():
    rows=[]
    for filename,level in (('course_manifest.json','基础'),('advanced_manifest.json','进阶')):
        path=ROOT/'scripts/assets'/filename
        for row in json.loads(path.read_text(encoding='utf-8')):
            rows.append({**row,'level':level})
    return rows


def store_path(value):
    path=value.resolve()
    if ROOT not in path.parents: raise ValueError('进度文件必须保存在仓库内')
    return path


def load(path):
    if not path.exists(): return {'schema_version':1,'records':{}}
    data=json.loads(path.read_text(encoding='utf-8'))
    if data.get('schema_version')!=1 or not isinstance(data.get('records'),dict):
        raise ValueError('进度文件格式不正确，原文件保留')
    return data


def main():
    parser=argparse.ArgumentParser(description='课程目录、阶段状态与本地学习记录')
    sub=parser.add_subparsers(dest='action',required=True)
    listing=sub.add_parser('catalog'); listing.add_argument('--json',action='store_true')
    progress=sub.add_parser('progress'); progress.add_argument('--json',action='store_true')
    record=sub.add_parser('record'); record.add_argument('id')
    record.add_argument('--status',choices=('learning','done','review'),default='learning')
    record.add_argument('--note',default='')
    for item in (progress,record): item.add_argument('--store',type=Path,default=ROOT/'scripts/runtime/study_progress.json')
    sub.add_parser('check')
    args=parser.parse_args()
    if args.action=='check':
        sys.path.insert(0,str(ROOT/'scripts/advanced'))
        from support import execute,new_run,PYTHON
        output=new_run('catalog-check')
        execute([PYTHON,'-I',ROOT/'scripts/validate_all.py',output],output)
        return
    rows=catalog(); identifiers={row['id'] for row in rows}
    if args.action=='catalog':
        if args.json: print(json.dumps(rows,ensure_ascii=False))
        else:
            for row in rows: print(f'{row["id"]} [{row["level"]}] {row["title"]}\n  {row["readme"]}')
        return
    path=store_path(args.store)
    if args.action=='record':
        if args.id not in identifiers: raise ValueError('未知课程编号，先用 catalog 查询')
        path.parent.mkdir(parents=True,exist_ok=True)
        with path.with_suffix('.lock').open('a') as lock:
            fcntl.flock(lock,fcntl.LOCK_EX)
            data=load(path)
            data['records'][args.id]={'status':args.status,'note':args.note,
                                     'updated':datetime.now(timezone.utc).isoformat()}
            temporary=path.with_suffix('.tmp')
            temporary.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            os.replace(temporary,path)
        print(f'{args.id} 已记为 {args.status}；进度保存在 {path}')
        return
    data=load(path); current={key:value for key,value in data['records'].items() if key in identifiers}
    report={'total':len(rows),'done':sum(row.get('status')=='done' for row in current.values()),
            'learning':sum(row.get('status')=='learning' for row in current.values()),
            'review':sum(row.get('status')=='review' for row in current.values()),'records':current}
    if args.json: print(json.dumps(report,ensure_ascii=False))
    else:
        print(f'完成 {report["done"]}/{report["total"]}；学习中 {report["learning"]}；待复习 {report["review"]}')
        for row in rows:
            item=current.get(row['id'])
            if item: print(f'{row["id"]} {item["status"]}：{item["note"]}')
        next_item=next((row for row in rows if current.get(row['id'],{}).get('status')!='done'),None)
        if next_item: print(f'按顺序的下一课：{next_item["id"]} {next_item["title"]}')


if __name__=='__main__':
    try: main()
    except (OSError,ValueError,json.JSONDecodeError) as error:
        print(f'学习记录未更新：{error}',file=sys.stderr)
        raise SystemExit(2)
