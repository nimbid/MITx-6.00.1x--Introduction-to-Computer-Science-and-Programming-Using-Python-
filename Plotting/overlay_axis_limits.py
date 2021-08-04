import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

# Overlaid plots by changing axis limits.
plt.figure('Linear')
plt.clf()
plt.xlabel('Samples')
plt.ylabel('Linear Function')
plt.ylim(0,1000)
plt.plot(mySamples,myLinear)
plt.figure('Quadratic')
plt.clf()
plt.xlabel('Samples')
plt.ylabel('quad')
plt.ylim(0,1000)
plt.plot(mySamples,myQuadratic)
plt.figure('Cubic')
plt.clf()
plt.xlabel('Samples')
plt.ylabel('Cubic Function')
plt.plot(mySamples,myCubic)
plt.figure('Exponential')
plt.clf()
plt.xlabel('Samples')
plt.ylabel('Exponential Function')
plt.plot(mySamples,myExponential)
# Reopening the figure can allow renaming the axes.
plt.figure('Quadratic')
plt.ylabel('Quadratic Function')
plt.title('Quadratic order of growth')
plt.show()
