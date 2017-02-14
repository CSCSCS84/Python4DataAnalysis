import numpy
from numpy.random import randn
import matplotlib.pyplot as plt
from datetime import datetime
import pandas

#Annotations and Drawing on a Subplot

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

crisis_data = [
(datetime(2007, 10, 11), 'Peak of bull market'),
(datetime(2008, 3, 12), 'Bear Stearns Fails'),
(datetime(2008, 9, 15), 'Lehman Bankruptcy')
]

data = pandas.read_csv('/home/christoph/PycharmProjects/PythonForDataAnalysis/pydata-book-master/ch08/spx.csv', index_col=0, parse_dates=True)
daystart=datetime(2007,1,1)
daysend=datetime(2011,1,1)
spx = data['SPX']
spx.plot(ax=ax, style='k-')
ax.set_xlim(daystart, daysend)
ax.set_ylim([600, 1800])
ax.set_title("Important dates in financial crisis")
for date, label in crisis_data:
    ax.annotate(label, xy=(date,spx.asof(date)+50),xytext=(date, spx.asof(date)+200 ),
                arrowprops=dict(facecolor='black'),
                horizontalalignment='left', verticalalignment='top')
rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
ax.add_patch(rect)
plt.plot(data)

#other file extensions are also valid like pdf
plt.savefig('figpath.svg',bbox_inches='tight')


#matplotlib Configuration
#font_options = {'family' : 'monospace','weight' : 'bold','size': 'small'}
#plt.rc('font', **font_options)
plt.show()
