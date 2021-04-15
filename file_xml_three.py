# Author:Glaciers
# -*- coding.utf-8 -*-

# 构建文档
from xml.etree import ElementTree as ET

'''
<home>
    <son name="儿1">
        <grandson name="儿11"></grandson>
        <grandson name="儿12"></grandson>
    </son>
    <son name="儿2"></son>
</home>
'''

# 创建根标签
root = ET.Element('home')

# 创建节点大儿子
son1 = ET.Element('son', {'name': '儿1'})

# 创建节点小儿子
son2 = ET.Element('son', {'name': '儿2'})

# 在大儿子中创建两个孙子
grandson1 = ET.Element('grandson', {'name': '儿11'})
grandson2 = ET.Element('grandson', {'name': '儿12'})
son1.append(grandson1)
son1.append(grandson2)

# 把儿子添加到根节点中
root.append(son1)
root.append(son2)

tree = ET.ElementTree(root)
tree.write(r'D:\functionProject\files\ooo.xml', encoding="utf-8", short_empty_elements=False)

