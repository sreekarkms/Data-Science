# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 23:08:23 2022

@author: HI
"""

"""
If you want to store data in the form of array you can go for Numpy Package

-> Numpy means "numerical python"
-> it is used mainly for storing data in array like rows and columns

"""
import numpy as np
#defining a List
data1=[[1,2,3,4,],[5,6,7,8]]
#CREATING an ARRAY
arr1=np.array(data1)

#Finding class of a data structure
arr1._class_
print(data1._class_) 
#Dimension of the Array
print(arr1.ndim)

#Shape of the Array
print(arr1.shape)

#Data type the array holde
print(arr1.dtype)

#creating array of zeros
a=np.zeros((3,6))
print(a)