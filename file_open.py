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
import os

file_path = os.path.abspath(__file__)
res = requests.get(
    url="http://f.video.weibocdn.com/xt0RE01Klx07LO9MEyNW01041202l1Hj0E010.mp4?label=mp4_720p&template=720x1280.24.0"
        "&trans_finger=c3f00996be5378650057cf237d7bfffd&media_id=4624885536981026&tp=8x8A3El:YTkl0eM8&us=0&ori=1&bf=4"
        "&ot=v&lp=00002KCE4n&ps=4pdsh0&uid=3ZoTIp&ab=,1493-g0,1192-g0,1191-g0,"
        "1258-g0&Expires=1618157721&ssig=WUaCT31R9Y&KID=unistore,video",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/86.0.4240.198 Safari/537.36 "
    }
)

file_path = os.path.dirname(file_path)
print(file_path)

# with open(r"files\huke.mp4"), mode="wb") as video:
with open(os.path.join(file_path, "files", "huke.mp4"), mode="wb") as video:
    video.write(res.content)
