import numpy
from pandas import Series, DataFrame
import pandas
#from pandas_datareader import data, wb
from numpy import nan as NA

obj1=Series([1,3,-1,2])
print(obj1)

obj2=Series([1,3,-1,2],index=["a","b","c","d"])
print(obj2)
print(obj2[obj2>0])

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
states = ['California', 'Ohio', 'Oregon', 'Texas']

obj4 = Series(sdata, states)
print(obj4)
print(pandas.isnull(obj4))
print(pandas.notnull(obj4))
#adding will result in NaN if one of entry in obj3 or obj4 is NaN
print(obj3+obj4)
print()
obj3.name="population"
print(obj3)
print()

#DataFrame
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
print(frame)
print()
#change order of rows
frame=DataFrame(data,columns=["state", "year","pop"])
print(frame)
print()
frame2=DataFrame(data, columns=["year","state","pop","debt"],index=["one","two","three","four","five"])
print(frame2)
#getting row year
print(frame2.year)
#getting column with index
print(frame2.ix["one"])
#assign value to NaN row
frame2["debt"]=16.5
print(frame2)

val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2["debt"]=val
print(frame2)
frame2["easter"]=1
del frame2["easter"]
print(frame2)

#The column returned when indexing a DataFrame is a view on the un-
#derlying data, not a copy. Thus, any in-place modifications to the Series
#will be reflected in the DataFrame. The column can be explicitly copied
#using the Series’s copy method.

print()

#Another common form of data is a nested dict of dicts format:
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3=DataFrame(pop)
print(frame3)
print()

#Index Objects
#Index objects are immutable

#reindexing of time series
#obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3=obj3.reindex(range(6), method='ffill')
print(obj3)

#Dropping entries from an axis
obj = Series(numpy.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj=obj.drop("c")
print(new_obj)
print(obj)

#dropping more than one column:
data = DataFrame(numpy.arange(16).reshape((4, 4)),
index=['Ohio', 'Colorado', 'Utah', 'New York'],
columns=['one', 'two', 'three', 'four'])

data_new=data.drop(["Ohio","Utah"])
print(data_new)
print()

#Indexing, selection, and filtering
obj = Series(numpy.arange(4.), index=['a', 'd', 'c', 'b'])
print(obj[2:4])
#Slicing with labels behaves differently than normal Python slicing in that the endpoint
#is inclusive:
print(obj["a":"c"])

data = DataFrame(numpy.arange(16).reshape((4, 4)),
index=['Ohio', 'Colorado', 'Utah', 'New York'],
columns=['one', 'two', 'three', 'four'])
print(data<5)
print(data[data["two"]>3])
print()

#label indexing on the row
print(data.ix['Colorado', ['two', 'three']])

#Arithmetic and data alignment
s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
s3=s1+s2
print(s3)
print()

#Arithmetic methods with fill values
df1 = DataFrame(numpy.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = DataFrame(numpy.arange(20.).reshape((4, 5)), columns=list('abcde'))

df3=df1.add(df2,fill_value=0)
print(df3)
df1=df1.reindex(columns=df2.columns,fill_value=0)
print(df1)

#Operations between DataFrame and Series
arr = numpy.arange(12.).reshape((3, 4))
print(arr-arr[0])

#the same holds for DataFrame +/- Series
frame = DataFrame(numpy.arange(12.).reshape((4, 3)), columns=list('bde'),
index=['Utah', 'Ohio', 'Texas', 'Oregon'])

print(frame-frame.ix[0])
series2 = Series(range(3), index=['b', 'e', 'f'])
print(frame + series2)
series3 = frame['d']
print(series3)
print(frame.sub(series3, axis=0))

#Function application and mapping
#ufuncs(element wise array methods)
frame = DataFrame(numpy.random.randn(4, 3), columns=list('bde'),
index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
#print(numpy.abs(frame))
f=lambda x: x.max() - x.min()
print(frame.apply(f))
print(frame.max(axis=1))

#elementwise python function
format = lambda x: '%.2f' % x
print(frame.applymap(format))
#or:
print(frame["b"].map(format))
print()

#Sorting and ranking
frame = DataFrame(numpy.arange(8).reshape((2, 4)), index=['three', 'one'],
columns=['d', 'a', 'b', 'c'])
print(frame)
print(frame.sort_index(axis=1))

print(frame.sort_index(axis=1,ascending=False))
bj = Series([4, 7, -3, 2])
print(bj.sort_values())
print()

#sort by values of a row
frame = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print(frame)
print(frame.sort_values(by="b"))
#also possible to sort by multiple columns
frame.sort_values(by=['a', 'b'])

#rank method
obj = Series([7, -5, 7, 4, 2, 0, 4])
print(obj.rank())
print(obj.rank(method="min"))
print()
frame = DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1],
'c': [-2, 5, 8, -2.5]})
print(frame.rank(axis=1))
print()

#Axis indexes with duplicate values
obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print(obj.index.is_unique)
print(obj["a"])
print()

#Summarizing and Computing Descriptive Statistics
df = DataFrame([[1.4, numpy.nan], [7.1, -4.5],
[numpy.nan, numpy.nan], [0.75, -1.3]],
index=['a', 'b', 'c', 'd'],
columns=['one', 'two'])
print(df)
print(df.sum())
print(df.sum(axis=1))
print(df.mean())
#NA values are excluded unless the entire slice (row or column in this case) is NA. This
#can be disabled using the skipna option:
print(df.mean(axis=1,skipna=False))
print(df.cumsum)
#describe is one
#such example, producing multiple summary statistics in one shot:
print(df.describe())
print()
#On non-numeric data, describe produces alternate summary statistics:
obj = Series(['a', 'a', 'b', 'c'] * 4)
print(obj)
print(obj.describe())
print()

#Correlation and Covariance
#see pages 139-140

#Unique Values, Value Counts, and Membership
obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
unique=obj.unique()
print(unique)
print(obj.value_counts())
mask = obj.isin(['b', 'c'])
print(mask)
print(obj[mask])

#Handling Missing Data

#Filtering Out Missing Data
data = Series([1, NA, 3.5, NA, 7])
print(data.dropna())
print(data)
#With DataFrame objects, these are a bit more complex. You may want to drop rows
#or columns which are all NA or just those containing any NAs. dropna by default drops
#any row containing a missing value:
data = DataFrame([[1., 6.5, 3.], [1., NA, NA],
[NA, NA, NA], [NA, 6.5, 3.]])
cleanedData=data.dropna()
print(cleanedData)
print()
#Passing how='all' will only drop rows that are all NA:
cleanedRows=data.dropna(how="all")
print(cleanedRows)

cleanedCols=data.dropna(axis=1,how="all")
print(cleanedCols)
print()

df = DataFrame(numpy.random.randn(7, 3))
df.ix[:4, 1] = NA; df.ix[:2, 2] = NA
print(df.dropna(thresh=1))
print()
print(df.dropna(thresh=2))
print()
print(df.dropna(thresh=3))
#remove all rows with less than thresh non NA or empty values
print()

#Filling in Missing Data
dfFilled=df.fillna(0)
print(dfFilled)
#fill columns using dict
dfFilledCol=df.fillna({1:0.5,3:2.1})
print(dfFilledCol)
print()

#fillna returns a new object, but you can modify the existing object in place
print(df)
_ = df.fillna(0, inplace=True)
print(df)
print(df)

#The same interpolation methods available for reindexing can be used with fillna :
df = DataFrame(numpy.random.randn(6, 3))
df.ix[2:, 1] = NA; df.ix[4:, 2] = NA
print(df)
_=df.fillna(method="ffill",limit=2,inplace=True)
print(df)

#Hierarchical Indexing
#Hierarchical indexing is an important feature of pandas enabling you to have multiple
#(two or more) index levels on an axis. Somewhat abstractly, it provides a way for you
#to work with higher dimensional data in a lower dimensional form.
data = Series(numpy.random.randn(10),
index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
[1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print(data)
print(data.index)
print(data["b"])
print(data[:,2])
print()
#format the table into a two dimensional table:
print(data.unstack())
print()

#With a DataFrame, either axis can have a hierarchical index:
frame = DataFrame(numpy.arange(12).reshape((4, 3)),
index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
columns=[['Ohio', 'Ohio', 'Colorado'],
['Green', 'Red', 'Green']])
print(frame)
frame.index.names = ['key1', 'key2']
print(frame.swaplevel("key1","key2"))
print(frame.sortlevel(1))
print(frame.swaplevel("key1","key2").sortlevel(1))

#Data selection performance is much better on hierarchically indexed
#objects if the index is lexicographically sorted starting with the outer-
#most level, that is, the result of calling sortlevel(0) or sort_index() .

#Summary Statistics by Level
print(frame.sum(level=1))
print()
frame.columns.names=["state","color"]
print(frame.sum(level='color', axis=1))

#Using a DataFrame’s Columns
frame = DataFrame({'a': range(7), 'b': range(7, 0, -1),
'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
'd': [0, 1, 2, 0, 1, 2, 3]})
frame2 = frame.set_index(['c', 'd'])
#c and d are not printed as columns, they are printed as indexes
print(frame2)
#printed as columns and as indeces:
print(frame.set_index(['c', 'd'], drop=False))

#reset_index , on the other hand, does the opposite of set_index ; the hierarchical index
#levels are are moved into the columns:
print(frame2.reset_index())
print()
#Integer Indexing
ser = Series(numpy.arange(3.))
#this would produce an error:
#ser[-1]

#On the other hand, with a non-integer index, there is no potential for ambiguity:
ser2 = Series(numpy.arange(3.), index=['a', 'b', 'c'])
print(ser2[-1])

#Panel Data
#While not a major topic of this book, pandas has a Panel data structure, which you can
#think of as a three-dimensional analogue of DataFrame. Much of the development focus
#of pandas has been in tabular data manipulations as these are easier to reason about,
#and hierarchical indexing makes using truly N-dimensional arrays unnecessary in a lot
#of cases.
#see page 152 for more information
