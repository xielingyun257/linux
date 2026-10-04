"""独立子进程练习：优雅退出、文件锁计数。"""
import argparse
import fcntl
import json
import os
from pathlib import Path
import signal
import threading


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('topic', choices=('graceful', 'increment'))
    parser.add_argument('directory', type=Path)
    args = parser.parse_args()
    directory = args.directory
    if args.topic == 'graceful':
        stopped = threading.Event()
        signal.signal(signal.SIGTERM, lambda *_: stopped.set())
        signal.signal(signal.SIGINT, lambda *_: stopped.set())
        ready_temporary = directory/'ready.tmp'
        ready_temporary.write_text(json.dumps({'pid':os.getpid()})+'\n')
        os.replace(ready_temporary, directory/'ready.json')
        try:
            while not stopped.wait(0.05):
                pass
        finally:
            (directory/'stopped.json').write_text(json.dumps({'clean_exit':True})+'\n')
    else:
        for _ in range(20):
            with (directory/'counter.lock').open('a') as lock:
                fcntl.flock(lock, fcntl.LOCK_EX)
                value = int((directory/'counter.txt').read_text())
                temporary = directory/f'counter-{os.getpid()}.tmp'
                temporary.write_text(str(value+1))
                os.replace(temporary, directory/'counter.txt')
                fcntl.flock(lock, fcntl.LOCK_UN)


if __name__ == '__main__':
    main()
