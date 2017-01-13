import json
from _testcapi import pymarshal_write_long_to_file
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from cairocffi import *
import numpy as np

pathUserData = '/home/christoph/PycharmProjects/PythonForDataAnalysis/pydata-book-master/ch02/names/yob1880.txt'

columnNames = ['name', 'gender', 'births']

names1880 = pd.read_table(pathUserData, sep=',', header=None,
                          names=columnNames, engine='python')

# print(names1880)

birthByGender = names1880.groupby('gender').births.sum()

# print(birthByGender)
pieces = []
for year in range(1880, 2011):
    namesOfYear = pd.read_table(
        '/home/christoph/PycharmProjects/PythonForDataAnalysis/pydata-book-master/ch02/names/yob%d.txt' % year, sep=',',
        header=None,
        names=columnNames, engine='python')
    namesOfYear['year'] = year
    pieces.append(namesOfYear)

names = pd.concat(pieces, ignore_index=True)
# print(birthByGender)

total_births = names.pivot_table('births', index='year', columns='gender', aggfunc=sum)

# print(total_births)

total_births.plot(title='Total births by sex and year')


# plt.show()


def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]


grouped = names.groupby(['year', 'gender'])
top1000 = grouped.apply(get_top1000)

boys = top1000[top1000.gender == 'M']

# print(boys[:1000])

girls = top1000[top1000.gender == 'F']

# print(girls[:1000])

total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc='sum')

print(total_births)

subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]

subset.plot(subplots=True, figsize=(12, 10), grid=False,
            title="Number of births per year")

plt.show()

get_last_letter = lambda x: x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'
table = names.pivot_table('births', index=last_letters,
                          columns=['gender', 'year'], aggfunc=sum)

subtable = table.reindex(columns=[1910, 1960, 2010], level='year')

letter_prop = subtable / subtable.sum().astype(float)

fig, axes = plt.subplots(2, 1, figsize=(10, 8))
letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female',
                      legend=False)

plt.show()
