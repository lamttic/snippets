def cache_decorator(func):
    memory = dict()

    def wrapper_decorator(n):
        print(memory)
        if n in memory:
            return memory[n]

        f = func(n)
        memory[n] = f
        return f

    return wrapper_decorator

@cache_decorator
def factorial(n):
    result = 1

    for value in range(1, n+1):
        result *= value

    return result

@cache_decorator
def total_sum(n):
    return sum(range(1, n+1))


print(factorial(10))
print(total_sum(10))
print(factorial(10))
print(total_sum(10))

