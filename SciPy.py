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
print(derivative(func=quadratic_equation_function,x0=2))