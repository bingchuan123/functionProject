# Author:Glaciers
# -*- coding.utf-8 -*-

import os

file_path = os.path.abspath(__file__)
file_path = os.path.dirname(file_path)

# 上下文管理
"""
之前对文件进行操作时，每次都要打开和关闭文件，比较繁琐且容易忘记关闭文件。
以后再进行文件操作时，推荐大家使用with上下文管理，它可以自动实现关闭文件。

with open("xxxx.txt", mode='rb') as file_object:
    data = file_object.read()
    print(data)
"""

# 1、补充代码：实现下载视频并保存到本地
"""

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
"""

# 2、日志分析，计算某用户`223.73.89.192`访问次数。日志文件如下：`access.log`
"""
ip = "223.73.89.192"
count = 0

# "r":读一个字符；"rb":读一个字节。
with open(os.path.join(file_path, "files", "access.log"), mode="r", encoding="utf-8") as file_ip:
    for line in file_ip:
        if line.startswith(ip):
            count += 1
print("访问次数为:{}".format(count))
"""

# 3、日志分析升级，计算所有用户的访问次数。

# 定义一个空字典，准备写入数据
user_dict = {}

# 循环每一行，取前面的IP字段，进行计数统计
with open(os.path.join(file_path, "files", "access.log"), mode="r", encoding="utf-8") as file_ip:
    # 循环每一行数据
    for line in file_ip:
        # 取所有的IP字段,每行的第0个索引
        user_ip = line.split(" ")[0]
        # 判断用户IP是否存在于字典中，如果不存在，则开始计数为初始值：1
        if user_ip not in user_dict:
            user_dict[user_ip] = 1
        # 否则用户IP存在于字典中，则开始计数为已计数值+1
        else:
            user_dict[user_ip] += 1
print(user_dict)
