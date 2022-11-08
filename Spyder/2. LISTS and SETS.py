# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 22:35:38 2022

@author: HI
"""

myList=[23,True,'cheese',3.14]
print(myList)
myList[0]
myList[1]
myList.append(5)
print(myList)
a=[5,10,50,100]
b=a[0:2]
print(b)
"""

SET
->set is used to store set of values without duplicates
->LISTS and DICTIONARIES are mutable
-> STRINGS ,TUPLES and SETS are IMMUTBLE
->STRINGS, LISTS and TUPLES are ORDERED
->SETS and DICTIONARIES are unordered

It Prints only unique value
Open and Cose curly brces
example
{'Sreekar','Gopi','Sirisha'}

"""
"""-----------------------------------------------------"""

""" 
Set DONOT CONTAIN DUPLICATE VALUE

"""


cset={11,11,12}
print(cset)
"""-----------------------------------------------------"""
aset={10,20,30,40}
bset=aset
aset=aset|{55}
print(aset)
"""
IT IS MUTABLE

"""
"""------------------------------------------------------"""

"""

SET does not support INDEXING 

"""
myset={'Apples','Oranges','Bananas'}
print(myset)
'''myset[0]'''

myset|{'SEEKAR'}
print(myset)

"""------------------------------------------------------"""
alist=[11,10,20,22,33,44,55]
aset=set(alist)
"""CONVERTING LIST TO SET"""
"""FOR ADDITION WE CAN ONLY USE "|" """

"""ADDITION"""
print(aset|bset)
print(sorted(aset|bset))

"""INTERSECTION"""
print(aset&bset)

"""DIFFERENCE"""
print(aset-bset)

"""SYMMETRIC DIFFERENCE"""
print(aset^bset)

"""---------------------------------------------------------"""

"""
SUMMARY

Data Type:

String ->"" ->storing the character

Tuple -> (,,)->immutable -> not changable

Dictionary ->{key: value} -> key and values -> used for indexing -mutable 

list-> [,,] -> mutable -> changable

set -> {,,} -> without Duplicates -> union, intersection, difference, symmetric difference

"""





