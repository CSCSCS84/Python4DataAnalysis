import numpy
from numpy.random import randn
import matplotlib.pyplot as plt
from datetime import datetime
import pandas
from pandas import Series, DataFrame


#Plotting Maps: Visualizing Haiti Earthquake Crisis Data
data = pandas.read_csv("/home/christoph/PycharmProjects/PythonForDataAnalysis/pydata-book-master/ch08/Haiti.csv")
print(data[["INCIDENT DATE","LATITUDE","LONGITUDE"]])
print(data.describe())

#cleaning the data because there are some abberrant locations
data = data[(data.LATITUDE > 18) & (data.LATITUDE < 21) &
(data.LONGITUDE > -75) & (data.LONGITUDE < -70)
& data.CATEGORY.notnull()]
print(data.describe())

def to_cat_list(catstr):
    stripped = (x.strip() for x in catstr.split(','))
    return [x for x in stripped if x]
def get_all_categories(cat_series):
    cat_sets = (set(to_cat_list(x)) for x in cat_series)
    return sorted(set.union(*cat_sets))
def get_english(cat):
    code, names = cat.split('.')
    if '|' in names:
        names = names.split(' | ')[1]
        return code, names.strip()

#skipped rest of the chapter