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

# Using subplots.
plt.figure('Linear v Quadratic')
plt.clf()
plt.subplot(211)
plt.ylim(0,900)
plt.plot(mySamples,myLinear,'b-',label = 'Linear',linewidth = 2.0)
plt.subplot(212)
plt.ylim(0,900)
plt.plot(mySamples,myQuadratic,'ro', label = 'Quadratic',linewidth = 3.0)
plt.legend(loc = 'upper left')

plt.figure('Cubic vs Exponential')
plt.clf()
plt.subplot(121)
plt.ylim(0,140000)
plt.plot(mySamples,myCubic,'g^',label = 'Cubic',linewidth = 4.0)
plt.subplot(122)
plt.ylim(0,140000)
plt.plot(mySamples,myExponential,'r--',label = 'Exponential',linewidth = 5.0)
plt.legend()

plt.show()
