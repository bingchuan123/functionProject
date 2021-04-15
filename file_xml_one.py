# Author:Glaciers
# -*- coding.utf-8 -*-

# [可扩展标记语言](https://baike.baidu.com/item/可扩展标记语言/2885849)，是一种简单的数据存储语言，XML 被设计用来传输和存储数据。
# - 存储，可用来存放配置文件，例如：java的配置文件。
# - 传输，网络传输时以这种格式存在，例如：早期ajax传输的数据、soap协议等。
# 读取节点数据
from xml.etree import ElementTree as ET

content = """
<data>
    <country name="Liechtenstein">
        <rank>2</rank>
        <year>2023</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
     <country name="Panama">
        <rank>69</rank>
        <year>2026</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
"""

# 获取跟标签data
root = ET.XML(content)

# 获取data标签的孩子标签
"""
for child in root:
    # child.tag = country
    # child.attrib = {"name":"Liechtenstein"}
    print(child.tag, child.attrib)
    for node in child:
        print(node.tag, node.attrib, node.text)


for child in root.iter('year'):
    print(child.tag,child.text)


v1 = root.findall('country')
print(v1)

v2 = root.find('country').find('rank')
print(v2.text)

"""

# 修改节点内容和属性
rank = root.find('country').find('rank')
print(rank.text)

rank.text = '999'   # 修改节点的内容
rank.set('update', '2020-11-11')    # 设置节点的标签
print(rank.text, rank.attrib)
############ 保存文件 ###########
tree = ET.ElementTree(root)
tree.write(r"D:\functionProject\files\new.xml", encoding="utf-8")

# 删除节点
root.remove(root.find('country'))
print(root.findall('country'))
tree.write(r"D:\functionProject\files\newnew.xml", encoding="utf-8")

