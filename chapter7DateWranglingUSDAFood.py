import json
import pandas
from pandas import Series, DataFrame
db = json.load(open('/home/christoph/PycharmProjects/PythonForDataAnalysis/pydata-book-master/ch07/foods-2011-10-03.json'))
print(db)
print(db[0].keys())
print()

keys=['description', 'group', 'id', 'manufacturer']
info = DataFrame(db,columns=keys)
#print(info)
print()
print(pandas.value_counts(info.group))
print()
nutrients=[]
for rec in db:
    fnuts=DataFrame(rec['nutrients'])
    fnuts["id"]=rec["id"]
    nutrients.append(fnuts)
nutrients = pandas.concat(nutrients, ignore_index=True)
nutrients = nutrients.drop_duplicates()
col_mapping = {'description' : 'food','group':
'fgroup'}
info = info.rename(columns=col_mapping, copy=False)
col_mapping = {'description' : 'nutrient',
'group' : 'nutgroup'}
nutrients = nutrients.rename(columns=col_mapping, copy=False)
ndata = pandas.merge(nutrients, info, on='id', how='outer')
print(ndata.ix[3000])
