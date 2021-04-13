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
print(result)   # [('log-error', '/var/log/mariadb/mariadb.log'), ('pid-file', '/var/run/mariadb/mariadb.pid')]