import numpy
from numpy.random import randn
import matplotlib.pyplot as plt
from datetime import datetime
import pandas
from pandas import Series, DataFrame

#Plotting Functions in pandas

s = Series(numpy.random.randn(10).cumsum(), index=numpy.arange(0, 100, 10))
s.plot()
#plt.show()

#plotting of data frame
df = DataFrame(numpy.random.randn(10, 4).cumsum(0),
columns=['A', 'B', 'C', 'D'],
index=numpy.arange(0, 100, 10))
df.plot(kind="bar",alpha=0.7)
#plt.show()

#
df = DataFrame(numpy.random.rand(6, 4),
index=['one', 'two', 'three', 'four', 'five', 'six'],
columns=pandas.Index(['A', 'B', 'C', 'D'], name='Genus'))
print(df)
#stacked=True: each row is stacked together
df.plot(kind="bar",stacked=True)
#plt.show()

tips = pandas.read_csv('/home/christoph/PycharmProjects/PythonForDataAnalysis/pydata-book-master/ch08/tips.csv')
print(tips)
party_counts = pandas.crosstab(tips.day, tips.size)
print(party_counts)


party_pcts = party_counts.div(party_counts.sum(1).astype(float), axis=0)
print(party_pcts)
party_pcts.plot(kind='bar', stacked=True)
#plt.show()

#Histograms and Density Plots
#tips["tips_pct"]=tips["tip"]/tips["total_bill"]
#tips['tips_pct'].hist(bins=50)
#tips.plot.kde()
plt.show()