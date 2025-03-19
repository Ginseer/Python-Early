# -*- coding: utf-8 -*-
"""
UTC ID: TYV379
Name: joseph Edwards
Date: 06/20/2021
"""


import pandas as pd
import matplotlib.pyplot as plt
#print(df)

df = pd.read_csv('iris.csv')

df.columns = ['Number','sepal length', 'sepal width', 'petal length', 'petal width', 'species']

pd.set_option('precision', 2)

print(df.head())
print(df.tail())

print(df.describe())

df.hist()
plt.show()
    