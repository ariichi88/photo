#! /usr/bin/env python3
# coding: UTF-8
# test

import os
import sys
import datetime
import shutil
import re

FROM_DIR = '/home/username/Dropbox/カメラアップロード/'
TO_DIR = '/home/username/Photo/'


def check_date_format(date):
    res = re.match(r'20[0-9][0-9]/[0-1][0-9]/[0-3][0-9]', date)
    if res:
        return True
    else:
        return False


def check_and_make_dir(date):
    if os.path.exists(TO_DIR + date):
        print('すでにインポート済みです', sep='')
        sys.exit(1)
    else:
        os.makedirs(TO_DIR + date)


def copy_jpg_files(date, name):
    date_str = date.replace('/', '-')
    from_files = [f for f in os.listdir(FROM_DIR) if date_str in f]
    from_files.sort()
    count = 1
    for _, from_file in enumerate(from_files):
        _, ext = os.path.splitext(from_file)
        if 'jpg' in ext:
            to_file = name + '-' + format(count, '02') + ext
            shutil.copy2(FROM_DIR + from_file, TO_DIR + date + to_file)
            count = count + 1


if __name__ == '__main__':
    arg = sys.argv

    if len(arg) == 2:
        dt = datetime.datetime.now()
        date = dt.strftime('%Y/%m/%d')
        name = arg[1]
    elif len(arg) == 3:
        date = arg[1]
        name = arg[2]
    else:
        print('使用法　photo.py [date] newname')
        print('日付のフォーマットyyyy/mm/dd')
        sys.exit(1)

    if check_date_format(date):
        check_and_make_dir(date)
        copy_jpg_files(date, name)
    else:
        print('日付のフォーマットが違います')
        print('フォーマット　yyyy/mm/dd')
        sys.exit(1)
