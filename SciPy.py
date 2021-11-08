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