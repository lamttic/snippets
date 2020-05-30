memory = {}

def fib(n):
    if n in memory:
        return memory[n]

    if n <= 2:
        return 1

    result = fib(n - 1) + fib(n - 2)
    memory[n] = result

    return result


if __name__ == '__main__':
    print(1 == fib(1), fib(1))
    print(1 == fib(2), fib(2))
    print(2 == fib(3), fib(3))
    print(3 == fib(4), fib(4))
    print(5 == fib(5), fib(5))
    print(8 == fib(6), fib(6))
