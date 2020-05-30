def fib_decorator(func):
    memory = {}

    def inner_decorator(n):
        if n in memory:
            return memory[n]

        f = func(n)
        memory[n] = f
        return f

    return inner_decorator

@fib_decorator
def fib(n):
    if n <= 2:
        return 1

    return fib(n-2) + fib(n-1)


if __name__ == '__main__':
    print(1 == fib(1), fib(1))
    print(1 == fib(2), fib(2))
    print(2 == fib(3), fib(3))
    print(3 == fib(4), fib(4))
    print(5 == fib(5), fib(5))
    print(8 == fib(6), fib(6))
