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

# Changing scales.
plt.figure('Linear v Quadratic Log')
plt.clf()
plt.plot(mySamples,myLinear,'b-',label = 'Linear',linewidth = 2.0)
plt.plot(mySamples,myQuadratic,'ro', label = 'Quadratic',linewidth = 3.0)
plt.yscale('log')
plt.legend(loc = 'upper left')

plt.figure('Cubic vs Exponential Linear')
plt.clf()
plt.plot(mySamples,myCubic,'g^',label = 'Cubic',linewidth = 4.0)
plt.plot(mySamples,myExponential,'r--',label = 'Exponential',linewidth = 5.0)
plt.legend()

plt.show()
