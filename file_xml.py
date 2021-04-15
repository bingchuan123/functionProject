# Author:Glaciers
# -*- coding.utf-8 -*-

# [可扩展标记语言](https://baike.baidu.com/item/可扩展标记语言/2885849)，是一种简单的数据存储语言，XML 被设计用来传输和存储数据。
# - 存储，可用来存放配置文件，例如：java的配置文件。
# - 传输，网络传输时以这种格式存在，例如：早期ajax传输的数据、soap协议等。

from xml.etree import ElementTree as ET

content = '''  
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2023</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
     <country name="Panama">
        <rank updated="yes">69</rank>
        <year>2026</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
'''

# 1、读取文件和内容

# # ET去打开xml文件
# tree = ET.parse(r"d:\functionProject\files\xo.xml")
# print(tree)  # <xml.etree.ElementTree.ElementTree object at 0x000002E7DD9D0580>
#
# # 获取根标签
# root = tree.getroot()
# print(root)  # <Element 'data' at 0x0000025175C75E50>
#
# root = ET.XML(content)
# print(root)  # <Element 'data' at 0x000001A53E3C4950>


# 2、读取节点数据
# 获取跟标签data
root = ET.XML(content)

country_object = root.find("country")
print(country_object.tag, country_object.attrib)     # country {'name': 'Liechtenstein'}

gdppc_object =country_object.find("gdppc")
print(gdppc_object.tag, gdppc_object.attrib, gdppc_object.text)