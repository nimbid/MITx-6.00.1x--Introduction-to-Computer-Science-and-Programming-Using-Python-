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

# Overlaid plots in same display.
plt.figure('Linear v Quadratic')
plt.clf()
plt.plot(mySamples,myLinear)
plt.plot(mySamples,myQuadratic)

plt.figure('Cubic vs Exponential')
plt.clf()
plt.plot(mySamples,myCubic)
plt.plot(mySamples,myExponential)

plt.show()
