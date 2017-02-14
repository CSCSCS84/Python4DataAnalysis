import numpy
from numpy.random import randn
import matplotlib.pyplot as plt

#A Brief matplotlib API Primer

fig = plt.figure()
#to adjust the figure
fig.subplots_adjust(left=0.0, bottom=None, right=1.2, top=None,
wspace=0, hspace=None)
ax1 = fig.add_subplot(2, 2, 1)

ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
#fig.show()
#plt.plot()
#o option for plotting the points
plt.plot(randn(50000).cumsum(), 'go--',label="random walk")
#g-- is the same as:
#linestyle='--', color='g'
_ = ax1.hist(randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(numpy.arange(30), numpy.arange(30) + 3 * randn(30))
plt.plot(drawstyle='steps-post', label='steps-post')
plt.show()

#Adjusting the spacing around subplots

#Ticks, Labels, and Legends
#sets the axes range to 0 to 10
#plt.xlim([0, 10])
#plt.show()

fig = plt.figure(); ax = fig.add_subplot(1, 1, 1)
ax.plot(randn(1000).cumsum())
#sets the label of the plot
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],
rotation=30, fontsize='small')
ax.set_title("My first plot title")

plt.show()


