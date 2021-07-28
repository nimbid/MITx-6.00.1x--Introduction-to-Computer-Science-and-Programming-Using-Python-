# Write a generator, genPrimes, that returns the sequence of prime numbers on
# successive calls to its next() method: 2, 3, 5, 7, 11, ...

def genPrimes():
    primeList = [2]
    num = 2
    yield num
    isPrime = False
    while True:
        for p in primeList:
            if num % p != 0:
                isPrime = True
            else:
                isPrime = False
                break
        if isPrime == True:
            primeList.append(num)
            yield num
        num += 1
