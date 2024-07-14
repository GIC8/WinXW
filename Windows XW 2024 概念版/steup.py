# -*- coding: utf-8 -*-
# /BLACKBOXES/BOOT

# /BLACKBOXES/KEY-VALUE
TC = True
import sys
import os
from datetime import datetime

NoneT = None
Inf = float('inf')
workdir = os.getcwd()
system = os.system
now = datetime.now

# /BLACKBOXES/LOG
if not os.path.exists('debug.log'):  # 文件不存在时创建
    open('debug.log', 'w', encoding='utf-8').close()
with open('debug.log', 'a+', encoding='utf-8') as f:
    f.write(f'[{now().strftime('%Y-%M-%D')}][debug.log]\n')


def log(s, thread='main', level='debug'):
    if not os.path.exists('debug.log'):
        raise SystemExit('STOP:missing debug.log')

    with open('debug.log', 'a+', encoding='utf-8') as f:
        f.write(f'[{now().strftime('%H:%M:%S')}][{thread}/{level}]:{s}\n')


# /BLACKBOXES/MAIN
def write(s):
    log(s, 'main', 'info')
    sys.stdout.write(s + '\n')


def write_err(s):
    log(s, 'main', 'error')
    sys.stderr.write(s + '\n')


def main():
    write('Boot at BIOS')
    write('Boot with USB Drive')
    write('安装程序正在启动...')
    write('Windows XW 2024 概念版')


if '__main__' == __name__:
    main()
