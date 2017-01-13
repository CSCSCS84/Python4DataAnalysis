import pandas
import csv
from pandas import Series, DataFrame
import json
from lxml.html import parse
import urllib3
import requests
import sqlite3
import pandas.io.sql as sql

path="/home/christoph/PycharmProjects/PythonForDataAnalysis/pydata-book-master/ch06/"
df = pandas.read_csv(path+"ex1.csv")
print(df)
df=pandas.read_table(path+"ex1.csv", sep=",")
print(df)
print()

#file without header:
df2= pandas.read_csv(path+"ex2.csv")
print(df2)
df3=pandas.read_csv(path+"ex2.csv",names=["a","b","c","d","m"])
print(df3)

#names as index
names = ["a", "b", "c", "d", "message"]
df4=pandas.read_csv(path+"ex2.csv",names=names,index_col="message")
print(df4)

#hierachical index
df5=pandas.read_csv(path+"csv_mindex.csv",index_col=["key1","key2"])
print(df5)

#seperator is white space or \n
df6=pandas.read_csv(path+"ex3.txt",sep="\s+")
print(df6)
print()
#Because there was one fewer column name than the number of data rows, read_table
#infers that the first column should be the DataFrame’s index in this special case.

df6=pandas.read_csv(path+"ex4.csv",skiprows=[0,2,3])
print(df6)
print()

#Missing data is usually either not present (empty string) or marked by some
#sentinel value. By default, pandas uses a set of commonly occurring sentinels, such as
# NA , -1.#IND , and NULL :

df7 = pandas.read_csv(path+"ex5.csv")
print(df7)
print(df7.notnull())

#Different NA sentinels can be specified for each column in a dict:
sentinels={"something": ["one","two"], "message":["NA","world"]}
df8=pandas.read_csv(path+"ex5.csv", na_values=sentinels)
print(df8)
print()

#Reading Text Files in Pieces
df8 = pandas.read_csv(path+'ex6.csv',nrows=5)
print(df8)
print()

#To read out a file in pieces, specify a chunksize as a number of rows:
chunker=pandas.read_csv(path+"ex6.csv",chunksize=1000)
print(chunker)
#for piece in chunker:
#    print(piece)

#TextParser is also equipped with a get_chunk method which enables you to read pieces
#of an arbitrary size.
print(chunker.get_chunk(10))

#Writing Data Out to Text Format
data = pandas.read_csv(path+'ex5.csv')
data.to_csv(path+"ex5b.csv",sep="j")

data.to_csv(path+"ex5c.csv", na_rep='NULL')
#write data without header and without index
data.to_csv(path+"ex5d.csv",index=False, header=False)

#write subset of columns to file
data.to_csv(path+"ex5e.csv", index=False, columns=['a', 'b', 'c'])

#see the docstrings for to_csv and from_csv in IPython for more information.

#Manually Working with Delimited Formats
#It’s not uncommon to receive a file with one or more malformed lines that trip up
#read_table .
#For any file with a single-character delimiter, you can use Python’s built-in csv module.
f = open(path+'ex7.csv')
reader = csv.reader(f)

for r in reader:
    print(r)
print()
#does not work:
#df9=pandas.read_csv(path+"ex7.csv")
#writing into a DataFrame in some steps:
lines = list(csv.reader(open(path+"ex7.csv")))
header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))}
print(data_dict)

data_frame=DataFrame(data_dict)
print(data_frame)

#csv module overs some more options for reading and writing files

#JSON Data
#JSON is very nearly valid Python code with the exception of its null value null and
#some other nuances (such as disallowing trailing commas at the end of lists). The basic
#types are objects (dicts), arrays (lists), strings, numbers, booleans, and nulls. All of the
#keys in an object must be strings. There are several Python libraries for reading and
#writing JSON data. I’ll use json here as it is built into the Python standard library.

obj = """
{"name": "Wes",
"places_lived": ["United States", "Spain", "Germany"],
"pet": null,
"siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"},
{"name": "Katie", "age": 33, "pet": "Cisco"}]
}
"""
result=json.loads(obj)
print(result)
#json.dumps on the other hand converts a Python object back to JSON:

#Conveniently, you can pass a list of JSON objects
#to the DataFrame constructor and select a subset of the data fields:
siblings = DataFrame(result['siblings'], columns=['name', 'age'])
print(siblings)

#XML and HTML: Web Scraping
#Python has many libraries for reading and writing data in the ubiquitous HTML and
#XML formats. lxml (http://lxml.de) is one that has consistently strong performance in
#parsing very large files. lxml has multiple programmer interfaces
url='http://finance.yahoo.com/q/op?s=AAPL+Options'
http = urllib3.PoolManager()
response = http.request('GET', url)
html = response.read()
#skipped chapter

#Binary Data Formats
#One of the easiest ways to store data efficiently in binary format is using Python’s built-
#in pickle serialization. Conveniently, pandas objects all have a save method which
#writes the data to disk as a pickle:

#functions in pandas are: read_csv, save, load
#pickle is only recommended as a short-term storage format.


#Using HDF5 Format
#There are a number of tools that facilitate efficiently reading and writing large amounts
#of scientific data in binary format on disk. A popular industry-grade library for this is
#HDF5,
#pandas has a minimal dict-like HDFStore class, which uses PyTables to store pandas
#objects:
store = pandas.HDFStore('mydata.h5')
store["obj1"] = data_frame

print(store["obj1"])

#If you work with huge quantities of data, I would encourage you to explore PyTables
#and h5py to see how they can suit your needs.

#Reading Microsoft Excel Files
#pandas also supports reading tabular data stored in Excel 2003 (and higher) files using
#the ExcelFile class.

#chapter skipped

#Interacting with HTML and Web APIs
#To search
#for the words “python pandas” on Twitter, we can make an HTTP GET request like so:
#Does not work:
url = 'http://search.twitter.com/1.1/search/tweets.json?q=python%20pandas'
resp = requests.get(url)
print(resp)
data = json.loads(resp.text)
print(data.keys())

#rest of rest of this chapter skipped

#Interacting with Databases
query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
c REAL,
d INTEGER
);"""

con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()

data = [('Atlanta', 'Georgia', 1.25, 6),
('Tallahassee', 'Florida', 2.6, 3),
('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
con.executemany(stmt, data)
con.commit()
result=con.execute("select * from test")
rows = result.fetchall()
print(rows)
print()
print()

#easy sql execution
print(sql.read_sql('select * from test', con))
