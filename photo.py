#! /usr/bin/env python3
# coding: UTF-8

import os
import sys
import datetime
import shutil

FromDir = ''
ToDir = ''


def CheckAndMakeDir(date):
    if os.path.exists(ToDir + date):
        print('ディレクトリ', ToDir, date, 'がすでに存在しています。', sep='')
        sys.exit(1)
    else:
        os.makedirs(ToDir + date)


def CopyJpegFiles(date, newname):
    datestr = date.replace('/', '-')
    fromfiles = [f for f in os.listdir(FromDir) if datestr in f]
    fromfiles.sort()
    for count, fromfile in enumerate(fromfiles):
        _, ext = os.path.splitext(fromfile)
        if 'mp4' in ext:
            pass
        else:
            tofile = newname + '-' + format(count + 1, '02') + ext
            shutil.copy2(FromDir + fromfile, ToDir + date + '/' + tofile)


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
    CheckAndMakeDir(date)
    CopyJpegFiles(date, name)
