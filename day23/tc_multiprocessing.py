import math
import time
from multiprocessing import Pool
from os import cpu_count

numbers = [50000, 60000, 55000, 45000, 70000]
def compute_factorial(n):
    return math.factorial(n)

starttime1 = time.time()
seq_results=[]
for n in numbers:
    seq_results.append(compute_factorial(n))
    print(f"sequential:factorial({n}) calculated")

seqtime=time.time() - starttime1
print(f"\nsequential time: {seqtime}")

starttime2 = time.time()
with Pool(cpu_count()) as p:
    parallel_results=p.map(compute_factorial, numbers)
for n in numbers:
    print(f"multiprocessing:factorial({n}) calculated")
paralleltime = time.time() - starttime2
print(f"\nmultiprocessing time: {paralleltime}")