import numpy
import pandas

#NumPy, for example, features low-level but extremely fast binary data loading and storage, including
#support for memory-mapped array.
df = pandas.read_csv('ch06/ex1.csv')
print(df)