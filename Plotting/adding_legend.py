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

# Adding legend.
plt.figure('Linear v Quadratic')
plt.clf()
plt.plot(mySamples,myLinear,label = 'Linear')
plt.plot(mySamples,myQuadratic, label = 'Quadratic')
plt.legend(loc = 'upper left')

plt.figure('Cubic vs Exponential')
plt.clf()
plt.plot(mySamples,myCubic,label = 'Cubic')
plt.plot(mySamples,myExponential,label = 'Exponential')
plt.legend()

plt.show()
