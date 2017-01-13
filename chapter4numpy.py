import numpy

data=numpy.array([[ 0.9526, -0.246 , -0.8856],
[ 0.5639, 0.2379, 0.9104]])

print(data.dtype)
print(data.ndim)
print(data.shape)

zeros=numpy.zeros(10)
print(zeros)
print(zeros.dtype)

arange=numpy.arange(15)

print(arange)

#cast array
arr = numpy.array([1, 2, 3, 4, 5])
print(arr.dtype)
float_arr = arr.astype(numpy.float64)

arr = numpy.array([[1., 2., 3.], [4., 5., 6.]])

print(arr*arr)
print(7*arr)
print(arr**0.5)

arr=numpy.arange(10)

print(arr[4:7])
arr[1:4]=9
print(arr)

#note: arr is changed! arrView is not a copy, it is a view
arrView=arr[1:5]
arrView[1]=12345
print(arr)

arr2d = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
print(arr2d[0:1,:2])

#set values with condition
arr2d[arr2d<2]=0
print(arr2d)
print()

#fancy indexing
arr=numpy.array([[0,0],
                [1,1],
                [2,2],
                [3,3]])

print(numpy.array(arr[[3,2]]))
print(numpy.array(arr[[-3,-1]]))
print()
arr = numpy.arange(32).reshape((8, 4))
print(arr)
print()
print(arr[[1,5,7,2],[0,3,1,2]])
print()
print(arr[numpy.ix_([1,5,7,2],[0,3,1,2])])
#Keep in mind that fancy indexing, unlike slicing, always copies the data into a new array.


#Transposing Arrays and Swapping Axes

A=numpy.arange(15).reshape((3, 5))
print(A.T)
#AA^T
print(numpy.dot(A,A.T))
print()
arr = numpy.arange(16).reshape((2, 2, 4))
print(arr)
print(arr.transpose((1,0,2)))
print()
print(arr.swapaxes(1, 2))
#swapaxes similarly returns a view on the data without making a copy.

print()

#Universal Functions: Fast Element-wise Array Functions
arr=numpy.arange(10)
print(numpy.sqrt(arr))
print()
#np.exp(arr)
#numpy.maximum(x, y) y is a 1x10 array, maximum returns elementwise maximum
#numpy.modf(arr) : it returns the fractional and integral parts of a floating point array

#Data Processing Using Arrays
points = numpy.arange(-5, 5, 0.01)
xs,ys = numpy.meshgrid(points, points)
print(xs)
print(ys)
print()
z=numpy.sqrt(xs**2 +ys**2)
print(z)

#Expressing Conditional Logic as Array Operations


xarr = numpy.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = numpy.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = numpy.array([True, False, True, True, False])

#pure python version:
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
#faster version:
result = numpy.where(cond, xarr, yarr)
#if condition cond_ij is true, take xarr_ij, else yarr_ij; works also for scalar input:
result=numpy.where(cond,2,-1)
print(result)

#Mathematical and Statistical Methods
arr = numpy.random.randn(5, 4)
print(arr)
print(numpy.mean(arr))
print(numpy.sum(arr))

print(arr.mean(axis=1))


arr = numpy.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr)
print(arr.cumsum(1))
print(arr.cumprod(0))
#argument is the axis
print()

#Methods for Boolean Arrays
arr=numpy.random.randn(100)
print((arr>0).sum())

#Sorting
arr.sort()
#numpy.unique , which returns the sorted unique values in an array:
names = numpy.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(numpy.unique(names))
print()

#File Input and Output with Arrays
arr=numpy.arange(10)
numpy.save("some_array",arr)
arr2=numpy.load('some_array.npy')
print(arr2)
#saves arrays in a zip with two files
numpy.savez('array_archive.npz', a=arr, b=arr)
arch=numpy.load('array_archive.npz')
print(arch["a"])
print()

#random walk with numpy
numberOfSteps=1000
randomInt=numpy.random.randint(0,2,numberOfSteps)
print(randomInt)
step=numpy.where(randomInt>0,1,-1)
walk=numpy.cumsum(step)
print(walk)
print((numpy.abs(walk)>10).argmax())