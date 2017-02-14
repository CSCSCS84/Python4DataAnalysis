import pandas
from pandas import Series, DataFrame
import numpy

#Combining and Merging Data Sets
#Database-style DataFrame Merges

#Merge or join operations combine data sets by linking rows using one or more keys.
#These operations are central to relational databases

df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
'data1': range(7)})

df2 = DataFrame({'key': ['a', 'b', 'd'],
'data2': range(3)})

print(df1)
print(df2)

print(pandas.merge(df1,df2))
#column d is not in the merge; one to many relation; a and b appeare more than once in df1, but only once in df2

#specify key
print(pandas.merge(df1,df2,on="key"))

df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
'data1': range(7)})
df4 = DataFrame({'rkey': ['a', 'b', 'd'],
'data2': range(3)})

print(pandas.merge(df3,df4, left_on="lkey",right_on="rkey"))

#outer join (default is inner join)
print(pandas.merge(df3,df4, left_on="lkey",right_on="rkey", how="outer"))
print()

df5 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
'data1': range(6)})

df6 = DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
'data2': range(5)})
print(df5)
print(df6)

print(pandas.merge(df5,df6, on="key"))
#Many-to-many joins form the Cartesian product of the rows.
print(pandas.merge(df5,df6, on="key", how="inner"))
print()

left = DataFrame({'key1': ['foo', 'foo', 'bar'],
'key2': ['one', 'two', 'one'],
'lval': [1, 2, 3]})

right = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
'key2': ['one', 'one', 'one', 'two'],
'rval': [4, 5, 6, 7]})
print(left)
print(right)

#merge with multiple keys:
print(pandas.merge(left,right, on=["key1","key2"]))
print()

#Merging on Index
left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
'value': range(6)})

right1 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

print(pandas.merge(left1,right1,left_on="key",right_index=True))
print()

#With hierarchically-indexed data, things are a bit more complicated:
lefth = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'key2': [2000, 2001, 2002, 2001, 2002],
'data': numpy.arange(5.)})

righth = DataFrame(numpy.arange(12).reshape((6, 2)),
index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
[2001, 2000, 2000, 2000, 2001, 2002]],
columns=['event1', 'event2'])

print(lefth)
print(righth)

print(pandas.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True))
print()

#Using the indexes of both sides of the merge is also not an issue:
left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'],
columns=['Ohio', 'Nevada'])

right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])
print(pandas.merge(left2,right2, right_index=True, left_index=True))

#DataFrame has a more convenient join instance for merging by index.
#DataFrame’s join method
#performs a left join on the join keys
print(left1.join(right1, on='key'))
print()

#Concatenating Along an Axis
s1 = Series([0, 1], index=['a', 'b'])
s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = Series([5, 6], index=['f', 'g'])
print(pandas.concat([s1,s2,s3]))
print()

#By default concat works along axis=0 , producing another Series. If you pass axis=1 , the
#result will instead be a DataFrame ( axis=1 is the columns):
print(pandas.concat([s1,s2,s3],axis=1))
s4 = pandas.concat([s1 * 5, s3])
print(s4)
print()
#You can even specify the axes to be used on the other axes with join_axes :
print(pandas.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b']]))
#only the axes on join_axes are used

#One issue is that the concatenated pieces are not identifiable in the result. Suppose
#instead you wanted to create a hierarchical index on the concatenation axis. To do this,
#use the keys argument:
result = pandas.concat([s1, s1, s3], keys=['one', 'two', 'three'])
print(result)
print()

#In the case of combining Series along axis=1 , the keys become the DataFrame column
#headers:
print(pandas.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three']))
print()

#The same logic extends to DataFrame objects:
df1 = DataFrame(numpy.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
columns=['one', 'two'])

df2 = DataFrame(5 + numpy.arange(4).reshape(2, 2), index=['a', 'c'],
columns=['three', 'four'])

print(pandas.concat([df1,df2],axis=1, keys=["level1","level2"]))

#If you pass a dict of objects instead of a list, the dict’s keys will be used for the keys
#option:
print(pandas.concat({'level1': df1, 'level2': df2}, axis=1))
print()


df1 = DataFrame(numpy.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = DataFrame(numpy.random.randn(2, 3), columns=['b', 'd', 'a'])

#A last consideration concerns DataFrames in which the row index is not meaningful in
#the context of the analysis:
print(pandas.concat([df1,df2],ignore_index=True))
print()
#with True, index is 0,1,2,3,4 else, index is 0,1,2,0,1

#Reshaping and Pivoting
#stack : this “rotates” or pivots from the columns in the data to the rows
#unstack : this pivots from the rows into the columns
data = DataFrame(numpy.arange(6).reshape((2, 3)),
index=pandas.Index(['Ohio', 'Colorado'], name='state'),
columns=pandas.Index(['one', 'two', 'three'], name='number'))
result=data.stack()
print(result)
print()

#Stacking a DataFrame means moving (also rotating or pivoting) the innermost column
#index to become the innermost row index.
print()
print(result.unstack(0))
#or
print(result.unstack("state"))
print()

#When unstacking in a DataFrame, the level unstacked becomes the lowest level in the
#result:

df = DataFrame({'left': result, 'right': result + 5},
columns=pandas.Index(['left', 'right'], name='side'))
print(df)
print(df.unstack("state"))
print()

#Pivoting “long” to “wide” Format
#long is a table with many rows, wide with many columns
#use pivot method, see chapter for more


#Data Transformation
#Removing Duplicates

#indicates whether each row is a duplicate or not:
#data.duplicated()
#
#data.drop_duplicates()
#data.drop_duplicates(['k1'])
#Passing take_last=True will return the last one:

#Transforming Data Using a Function or Mapping:

data = DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami',
'corned beef', 'Bacon', 'pastrami', 'honey ham',
'nova lox'],
'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

meat_to_animal = {
'bacon': 'pig',
'pulled pork': 'pig',
'pastrami': 'cow',
'corned beef': 'cow',
'honey ham': 'pig',
'nova lox': 'salmon'
}

#Suppose you wanted to add a column indicating the type of animal that each food came
#from

print(data["food"].map(meat_to_animal))

#problem: in data also Upper case letters
data["animal"]=data["food"].map(str.lower).map(meat_to_animal)
print(data)
print()

#Replacing Values
#data.replace([-999, -1000], np.nan)

#Renaming Axis Indexes
#skipped chapter

#Discretization and Binning

#Suppose you have data about a group of people in a study, and you want to group them
#into discrete age buckets:
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
#returns an object like [18,25], [18,25]... because first two entries in ages are betwenn 18-25
cats=pandas.cut(ages,bins)
print(cats)
print(pandas.value_counts(cats))
print()
#Which side is closed can be changed by passing right=False :

#You can also pass your own bin names by passing a list or array to the labels option
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
print(pandas.cut(ages, bins, labels=group_names))
print()

#equal-length bins based on the minimum and maximum values in the data:
data = numpy.random.rand(20)
print(pandas.cut(data, 4, precision=2))

#Since qcut uses sample quantiles instead, by definition you will obtain roughly equal-size bins:
data = numpy.random.randn(1000) # Normally distributed
cats = pandas.qcut(data, 4) # Cut into quartiles
print(pandas.value_counts((cats)))
print()

#Detecting and Filtering Outliers
data = DataFrame(numpy.random.randn(1000, 4))
print(data.describe())

#each row with at least one entry bigger than 3
print(data[(numpy.abs(data) > 3).any(1)])
print()

#Permutation and Random Sampling
df = DataFrame(numpy.arange(5 * 4).reshape(5, 4))
per=numpy.random.permutation(5)
print(df.take(per))
print()

#Computing Indicator/Dummy Variables:
df = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
'data1': range(6)})
print(df)
#creates tabel with columsn a,b,c. if key in row is x, than values is 1, else 0
print(pandas.get_dummies(df['key']))
print()

mnames = ['movie_id', 'title', 'genres']
movies = pandas.read_table('/home/christoph/PycharmProjects/PythonForDataAnalysis/pydata-book-master/ch02/movielens/movies.dat', sep='::', header=None,
names=mnames)

generIt=(set(x.split("|")) for x in movies.genres)
#print(*generIt)
print(set.union(*generIt))


#tring Object Methods
#methods like split or join
#In [216]: val.index(',')
#val.find(':')
#Note the difference between find and index is that index raises an exception if the string
#isn’t found (versus returning -1):


#Regular expressions
#Creating a regex object with re.compile is highly recommended if you intend to apply
#the same expression to many strings; doing so will save CPU cycles.

#Vectorized string functions in pandas
#advantage: this functions skip null values in the vector
#examples: contains (checks for a pattern in each string of the vector)
