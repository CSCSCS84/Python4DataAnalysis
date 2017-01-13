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

#Pivoting “long” to “wide” Format
#long is a table with many rows, wide with many columns
#use pivot method, see chapter for more
