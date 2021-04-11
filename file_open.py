# Author:Glaciers
# -*- coding.utf-8 -*-

# 上下文管理
"""
之前对文件进行操作时，每次都要打开和关闭文件，比较繁琐且容易忘记关闭文件。
以后再进行文件操作时，推荐大家使用with上下文管理，它可以自动实现关闭文件。

with open("xxxx.txt", mode='rb') as file_object:
    data = file_object.read()
    print(data)
"""

# 1、补充代码：实现下载视频并保存到本地
import requests

res = requests.get(
    url="http://f.video.weibocdn.com/0vpw83cslx07LNW8chS801041200gc4q0E010.mp4?label=mp4_ld&template=624x360.25.0&trans_finger=40a32e8439c5409a63ccf853562a60ef&ori=0&ps=1EO8O2oFB1ePdo&Expires=1618155997&ssig=%2FKSmAyrBgf&KID=unistore,video",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
)

with open("huke.mp4", mode="rb") as video:
    video.write(res.content)
