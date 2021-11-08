# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 19:33:33 2021

@author: pc
"""

#Importing Seaborn
import seaborn as sns

import numpy as np

import pandas as pd

#Creating a random dataset
data=np.random.multivariate_normal([0,0],[[4,2],[2,2]], size=2000)

print(data)

data=pd.DataFrame(data,columns=['x','y'])

print(data)

#Density plots : kdeplot
#shade=True
for col in 'xy':
    sns.kdeplot(data[col],shade=True)
    
#Density plots
#shade=False
for col in 'xy':
    sns.kdeplot(data[col],shade=False)


#Density plots: distplot
#kde-True
for col in 'xy':
    sns.displot(data[col],kde=True)
    
#kde=False
for col in 'xy':
    sns.displot(data[col],kde=False)

for col in 'xy':
    sns.displot(data[col])
    

#Pair Plot
iris=sns.load_dataset("iris")
print(iris.head())

sns.pairplot(iris,hue='species',height=2.5)

sns.pairplot(iris)