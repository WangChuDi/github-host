
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   liuyuqi
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2020/04/26 23:01:40
@Version :   1.0
@License :   Copyright © 2017-2020 liuyuqi. All Rights Reserved.
@Desc    :   github.com
'''

import shutil
import os,sys,ctypes
import datetime
import get_ip_utils
import platform

# 需要获取ip的网址
sites = [
    " github.com",
" store.steampowered.com",
" steam-chat.com",
" steamcdn-a.akamaihd.net",
" cdn.akamai.steamstatic.com",
" community.akamai.steamstatic.com",
" media.steampowered.com",
" steamcommunity.com",
" www.steamcommunity.com",
" api.steampowered.com",
" api.github.com",
" gist.github.com",
" raw.github.com",
" githubusercontent.com",
" raw.githubusercontent.com",
" camo.githubusercontent.com",
" cloud.githubusercontent.com",
" avatars.githubusercontent.com",
" avatars0.githubusercontent.com",
" avatars1.githubusercontent.com",
" avatars2.githubusercontent.com",
" avatars3.githubusercontent.com",
" user-images.githubusercontent.com",
" pages.github.com",
" github.io",
" www.github.io"
]

addr2ip = {}
hostLocation = r"hosts"

def dropDuplication(line):
    flag = False
    if "#*******" in line:
        return True
    for site in sites:
        if site in line:
            flag = flag or True
        else:
            flag = flag or False
    return flag

# 更新host, 并刷新本地DNS
def updateHost():
    today = datetime.date.today()
    for site in sites:
        trueip=get_ip_utils.getIpFromipapi(site)
        if trueip != None:
            addr2ip[site] = trueip
            print(site + "\t" + trueip)
    with open(hostLocation, "r") as f1:
        f1_lines = f1.readlines()
        with open("temphost", "w") as f2:
            for line in f1_lines:                       # 为了防止 host 越写用越长，需要删除之前更新的含有github相关内容
                if dropDuplication(line) == False:
                    f2.write(line)
            f2.write("#*********************github " +
                     str(today) + " update********************\n")
            f2.write("#******* get latest hosts: http://blog.yoqi.me/lyq/16489.html\n")
            for key in addr2ip:
                f2.write(addr2ip[key] + "\t" + key + "\n")
    os.remove(hostLocation)
    os.rename("temphost",hostLocation)

if __name__ == "__main__":
    updateHost()
