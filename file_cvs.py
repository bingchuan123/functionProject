# Author:Glaciers
# -*- coding.utf-8 -*-
"""
import os
import requests

file_path = os.path.abspath(__file__)
file_path = os.path.dirname(file_path)
print(file_path)

"""
# **逗号分隔值**（Comma-Separated Values，**CSV**，有时也称为**字符分隔值**，
# 因为分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）。
#
# 对于这种格式的数据，我们需要利用open函数来读取文件并根据逗号分隔的特点来进行处理。
"""

# 练习题案例：下载文档中的所有图片且以用户名为图片名称存储。
# 打开文件
with open(os.path.join(file_path, "files", "mv.cvs"), mode="r", encoding="utf-8") as download_file:
    # 去掉第一行无用数据
    download_file.readline()
    for line in download_file:
        # 得到每一行的用户名、链接地址
        user_id, username, ip = line.split(",")
        # 根据url下载图片
        res = requests.get(
            url=ip,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                              "(KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
            }
        )
        # 检查images目录是否存在？不存在，则创建images目录
        if not os.path.exists(os.path.join(file_path, "files", "images")):
            # 创建images目录
            os.makedirs(os.path.join(file_path, "files", "images"))

            # 将图片的内容写入到文件
            with open(os.path.join(file_path, "files", "images/{}.png".format(username)), mode="wb") as img_object:
                img_object.write(res.content)
"""

import os
import requests

with open('files/mv.csv', mode='r', encoding='utf-8') as file_object:
    file_object.readline()
    for line in file_object:
        user_id, username, url = line.strip().split(',')
        print(username, url)
        # 1.根据URL下载图片
        res = requests.get(
            url=url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
        )
        # 检查images目录是否存在？不存在，则创建images目录
        if not os.path.exists("images"):
            # 创建images目录
            os.makedirs("images")

        # 2.将图片的内容写入到文件
        with open("images/{}.png".format(username), mode='wb') as img_object:
            img_object.write(res.content)