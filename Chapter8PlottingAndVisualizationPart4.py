import numpy
from numpy.random import randn
import matplotlib.pyplot as plt
from datetime import datetime
import pandas
from pandas import Series, DataFrame

macro = pandas.read_csv('/home/christoph/PycharmProjects/PythonForDataAnalysis/pydata-book-master/ch08/macrodata.csv')
print(macro)
data = macro[['cpi', 'm1', 'tbilrate', 'unemp']].dropna()
data=numpy.log(data).diff()
plt.scatter(data["m1"],data["unemp"])
plt.show()

#In exploratory data analysis it’s helpful to be able to look at all the scatter plots among
#a group of variables; this is known as a pairs plot or scatter plot matrix
pandas.scatter_matrix(data, diagonal='kde', color='k', alpha=0.3)
plt.show()