# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 16:22:34 2021

@author: pc
"""

#Importing Pandas library
import pandas as pd

#Reading a file
data=pd.read_csv('IPL.csv')

#Viewing top 4 rows of the dataset
print("Top 4 rows of dataset: -")
print(data.head(4))

#To fetch number of rows and columns in the dataset
print("To view number of rows and columns in the dataset: -")
print(data.shape)

#To fetch list of all column names
print("To view list of columns in the dataset: -")
print(data.columns)

#To check datatypes in the columns
print("To fetch datatypes of each column: -")
print(data.dtypes)

#To fetch list of null values in the data
print("To fetch the list of null values in the data: -")
print(data.isna().sum())

#Summary of data
print("Summary of the dataset: - ")
print(data.describe())

