from functools import cache, lru_cache
import time

import sys




@cache
def cache_fibo(n: int) -> int:
    if n < 1:
       return 0
    return n + cache_fibo(n-1)

@lru_cache(maxsize=128)
def lru_cache_fibo(n: int) -> int:
    if n < 1:
       return 0
    return n + lru_cache_fibo(n-1)


def fibo(n: int) -> int:
    if n < 1:
        return 0
    return n + fibo(n-1)


N = 265


start_t1 = time.time_ns()
result1 = fibo(N)
end_t1 = time.time_ns()


start_t2 = time.time_ns()
result2 = cache_fibo(N)
end_t2 = time.time_ns()

start_t3 = time.time_ns()
result3 = lru_cache_fibo(N)
end_t3 = time.time_ns()

time1 = end_t1 - start_t1
time2 = end_t2 - start_t2
time3 = end_t3 - start_t3


print(f"running fibbonacci for N times.")
print(f"no cached result {result1} time: {time1}")
print(f"cache result {result2} time: {time2}")
print(f"LRU cache result {result3} time: {time3}")

