import time

def execution_time(func):
    def wrapper(n):
        start = time.time()
        result = func(n)
        end = time.time()
        print(f"Function '{func.__name__}' executed in {end - start:.6f} seconds")
        return result
    return wrapper


def factorial_calc(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_calc(n - 1)


@execution_time
def factorial(n):
    return factorial_calc(n)
result = factorial(10)
print("Factorial:", result)
