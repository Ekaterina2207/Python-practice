def main_cash(func):
    if not hasattr(main_cash, "cache"):
        main_cash.cache = {}

    def wrapper(*args, **kwargs):
        key = (func.__name__, args, tuple(kwargs.items()))

        if key in main_cash.cache:
            return main_cash.cache[key]
        else:
            result = func(*args, **kwargs)
            main_cash.cache[key] = result
            return result

    return wrapper

@main_cash
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(0))
print(Fibonacci(2))
print(Fibonacci(5))
print(Fibonacci(10))
print(Fibonacci(20))