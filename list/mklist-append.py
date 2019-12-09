#! /usr/bin/env python 

lst = []
for i in range(1,100):
 data = { 'index' : i, 'name' : 'sinchan'+str(i), 'score':  {'maths': 100+i, 'science': 200+i} }   
 lst.append(data)

print(lst)
