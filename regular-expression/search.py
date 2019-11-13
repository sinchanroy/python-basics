#! /usr/bin/env python

import re

str = "sinchan, 29, chennai"

list = []

list = re.search(",", str, 5)


print(list[0])
print(list[1])
print(list[2])

