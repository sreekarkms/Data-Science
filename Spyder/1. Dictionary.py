# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 04:09:05 2022

@author: HI
"""

plang1={1:'JAVA',2:'Python',3:'R- Language',4:'C'}
print(plang1)
print(plang1[3])
print(plang1.get(400,'Not present in the dictionary'))
plang1[1]='Python for data science'
print(plang1[1])
age={'Alice':22,'Bob':23}
print(age)
age.update({'Carol':24})
print(age)
age.get('Bob')
age.items()
age.values()
age.keys()
age.pop('Alice')
age.popitem()
print('---------------------------------')
print(age)