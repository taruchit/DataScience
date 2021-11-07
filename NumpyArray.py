# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 23:27:34 2021

@author: pc
"""
#Impporting Numpy library
import numpy as np

#Creating Numpy array
numpy_array=np.array([1,2,3,4,5])

#Printing the Numpy array
print(numpy_array)

#Broadcast operation
broadcast_array=numpy_array*2
print(broadcast_array)

#Creating a matrix
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

matrix_numpy_array=np.array(matrix)
print(matrix_numpy_array)

'''Accessing an element from Matrix Numpy array
Row 0, column 2 -> 3
'''
print(matrix_numpy_array[0][2])

#Matrix filled by random integers
matrix_numpy_randomInt=np.random.randint(1,10,(4,4))
print(matrix_numpy_randomInt)