#! /usr/bin/env python 

import xml.etree.ElementTree as ET
tree = ET.parse('uwm.xml')
root = tree.getroot()
print(root)
print(root.tag)
print(root.attrib)
for child in root:
    print(child.tag, child.attrib)
