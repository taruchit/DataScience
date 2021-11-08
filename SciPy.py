# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 14:21:04 2021

@author: pc
"""

#Importing SciPy library
import scipy

#Importing derivative from scipy
from scipy.misc import derivative

#Defining a function
def quadratic_equation_function(x):
    return x**2+x+1

#Calculating the first derivative of the function at x=2
print("Calculating derivation of equation with x=2")
print(derivative(func=quadratic_equation_function,x0=2))

#Importing comb from scipy
from scipy.special import comb

'''Calculating total number of combinations from 4 different values taken 2 at a time
4C2'''
com=comb(4,2)
print("Combination: 4C2: -")
print(com)

#Importing prem from scipy
from scipy.special import perm

#Importing numoy
import numpy as np

'''Calculating total number of permutations from 4 different values taken 2 at a time
4P2'''
per=perm(4,2)
print("Permutation 4P2: -")
print(per)

#Linear Algebra

#Importing linear algebra module: linag 
from scipy import linalg

#Square matrix
matrix=np.array([[1,5,2],
                [3,2,1],
                [1,2,1]])

#Calculating determinant of the matrix
matrix_determinant=linalg.det(matrix)
print("Determinant of the matrix: - ")
print(matrix_determinant)

#Calculating inverse of the matrix
matrix_inverse=linalg.inv(matrix)
print("Inverse of the matrix: -")
print(matrix_inverse)