def genFib():
    fib_1 = 1 # fib(n-1)
    fib_2 = 0 # fib(n-2)
    while True:
        nextFib = fib_1 + fib_2
        yield nextFib
        fib_2 = fib_1
        fib_1 = nextFib

newfib = genFib()
newfib.__next__()
newfib.__next__()
newfib.__next__()
newfib.__next__()

# Every time __next__() is called, it runs until the next yield and stops.
# Instead of while True, if the loop terminated, we would get a StopIteration exception.
