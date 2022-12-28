#!/usr/bin/python3
'''to compress and move a dir'''
from fabric.api import local
import datetime


def do_pack():
    local('rm -Rf dest/vers; mkdir -p dest/vers')
    date_string = datetime.datetime.now()
    current_time = date_string.strftime("%Y%m%d%H%M%S")
    archive = f'testfile_{current_time}.tgz'
    local(f"tar -cvzf dest/vers/{archive} src")
    path = local("tree -i -f dest/ | grep 'test.'")
    size_file = local(f"stat -c%s dest/vers/{archive}")
    print(f"web_static packed: {path} -> {size_file}")
    print()
    print('Done')
