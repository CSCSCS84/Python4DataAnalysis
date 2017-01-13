import json
#import panda
from collections import Counter
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
from cairocffi import *
import numpy as np


path='/home/christoph/PycharmProjects/PythonForDataAnalysis/pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt'

#open(path).readline()

records = [json.loads(line) for line in open(path)]

#for x in records:
 #   print (x)

#print (records[0]['tz'])

time_zones = [rec['tz'] for rec in records if 'tz' in rec]

#for x in time_zones:
    #print(x)

count=Counter(time_zones).most_common(10)

#for x in count:
   # print(x)

frame=DataFrame(records)

#print(frame)

#print(frame['tz'][:10])

tz_counts=frame['tz'].value_counts()

#print(tz_counts[:10])

clean_timezone=frame['tz'].fillna('Missing')

clean_timezone[clean_timezone=='']='Unknown'

tz_counts=clean_timezone.value_counts()

#print(tz_counts[:10])




#plt.figure(figsize=(10, 4))

tz_counts[:10].plot(kind='barh', rot=0)

#plt.plot([1,2,3,4], [1,4,9,16], 'ro')
#plt.axis([0, 6, 0, 20])


#plt.show()

cframe = frame[frame.a.notnull()]

windows=cframe['a'].str.contains("Windows")

windows_counts=windows.value_counts()

print (windows_counts)

operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows', 'Not Windows')

#print(operating_system[:5])

by_tz_os=cframe.groupby(['tz',operating_system])

print(by_tz_os)

agg_counts = by_tz_os.size().unstack().fillna(0)

print(agg_counts)

