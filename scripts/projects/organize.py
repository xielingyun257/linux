"""整理自动生成的练习资料，归档后逐文件验证，不覆盖用户资料。"""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tarfile


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def main(output):
    source = output / 'input'
    source.mkdir()
    (source / '课程 笔记.txt').write_text('学习 Linux\n先预测再运行\n', encoding='utf-8')
    (source / 'measurements.csv').write_text('x,y\n1,2\n3,4\n', encoding='utf-8')
    (source / 'README.md').write_text('# 原始练习资料\n', encoding='utf-8')
    organized = output / 'organized'
    manifest = {}
    for item in sorted(source.iterdir()):
        category = {'.txt': 'text', '.csv': 'data'}.get(item.suffix, 'other')
        destination = organized / category / item.name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, destination)
        manifest[str(destination.relative_to(organized))] = sha256(item.read_bytes())
        assert destination.read_bytes() == item.read_bytes()
    archive_path = output / 'backup.tar.gz'
    with tarfile.open(archive_path, 'w:gz') as archive:
        archive.add(organized, arcname='organized')
    restored = output / 'restored'
    restored.mkdir()
    with tarfile.open(archive_path, 'r:gz') as archive:
        # 已知文件名来自本脚本刚生成的清单；不用通用 extractall。
        for relative, digest in manifest.items():
            data = archive.extractfile('organized/' + relative).read()
            destination = restored / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
            assert sha256(data) == digest
    report = {'files': len(manifest), 'sha256': manifest, 'restoration_verified': True,
              'source_preserved': len(list(source.iterdir())) == 3}
    assert report['files'] == 3 and report['source_preserved']
    (output / 'manifest.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('3 个文件已分类；原始资料保留；备份恢复后的 SHA-256 全部一致。')


if __name__ == '__main__':
    main(Path(sys.argv[1]))
