import argparse


def main():
    parser = argparse.ArgumentParser(description='已安装的 Python 命令行入口')
    parser.add_argument('--name', default='Linux 学习者')
    args = parser.parse_args()
    print(f'你好，{args.name}！')
