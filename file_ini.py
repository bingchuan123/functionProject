# Author:Glaciers
# -*- coding.utf-8 -*-

# ini文件是Initialization File的缩写，平时用于存储软件的的配置文件。例如：MySQL数据库的配置文件。
# 这种格式是可以直接使用open来出来，考虑到自己处理比较麻烦，所以Python为我们提供了更为方便的方式。

import configparser
import os

# file_path = os.path.abspath(__file__)
# my_ini_file = os.path.join(file_path, "files", "my.ini")

config = configparser.ConfigParser()
config.read(r"D:\functionProject\files\my.ini", encoding="utf-8")

# 1、获取所有的节点
result = config.sections()
print(result)  # ['mysqld', 'mysqld_safe', 'client']

# 2、获取节点下的键值
result = config.items("mysqld_safe")
print(result)  # [('log-error', '/var/log/mariadb/mariadb.log'), ('pid-file', '/var/run/mariadb/mariadb.pid')]

for key, value in config.items("mysqld_safe"):
    print(key, value)

# 3、获取某个节点下的键对应的值
result = config.get("mysqld", "collation-server")
print(result)

# 4、其他内容
# 4.1、是否存在节点
v1 = config.has_section("client")
print(v1)

# 4.2、添加一个节点
config.add_section("group")
config.set("group", "name", "alex")  # 添加一个节点，并为他添加一个键值对
config.set("client", "name", "alex")  # 为现有的节点添加一个键值对，有的就改
config.set("client", "name", "glaciers")  # 为现有的节点添加一个键值对，有的就改
config.write(open(r"D:\functionProject\files\new.ini", mode="w", encoding="utf-8"))

# 4.3、删除
config.remove_section("client")  # 删除一个节点
config.remove_option("mysqld", "datadir")  # 删除节点下的其中一个键值对
config.write(open(r"D:\functionProject\files\new.ini", mode="w", encoding="utf-8"))
