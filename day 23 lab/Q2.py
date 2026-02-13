import math
import time
import multiprocessing

numbers = [50000, 60000, 55000, 45000, 70000]

def factorial_calc(n):
    fact = math.factorial(n)
    return (n, fact)

# Sequential Computation
start_time = time.time()

sequential_results = []
for num in numbers:
    sequential_results.append(factorial_calc(num))

sequential_time = time.time() - start_time
print("Sequential Factorial Calculation Completed")
print("Sequential Time Taken:", sequential_time, "seconds\n")

# Multiprocessing Computation 
start_time = time.time()

with multiprocessing.Pool() as pool:
    parallel_results = pool.map(factorial_calc, numbers)

multiprocessing_time = time.time() - start_time
print("Multiprocessing Factorial Calculation Completed")
print("Multiprocessing Time Taken:", multiprocessing_time, "seconds\n")

for n, fact in parallel_results:
    print(f"Factorial of {n} has {len(str(fact))} digits")

print("\nTime Comparison:")
print("Sequential Time:", sequential_time, "seconds")
print("Multiprocessing Time:", multiprocessing_time, "seconds")