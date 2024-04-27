"""
Purpose:
Run Fibonacci (or any function) with different
methods of caching to compare total time.
Output results into a RICH table on the cli.

Instructions to run:
python3.10 cache/time_caches.py

Careful with large N's. Program is not optimized for
excessive recursion depth.
"""

from functools import cache, lru_cache
from typing import Callable, Tuple, Dict
import time

from rich.console import Console
from rich.table import Table

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

def no_cache_fibo(n: int) -> int:
    if n < 1:
        return 0
    return n + no_cache_fibo(n-1)

def run(N: int, func: Callable[[int], int]) -> Tuple[int, int]:
    start = time.time_ns()
    result = func(N)
    end = time.time_ns()
    return (result, end-start)

def main():
    N = 250

    funcs = [no_cache_fibo, cache_fibo, lru_cache_fibo]

    results: Dict[str, Tuple[int, int]] = {str(f.__name__): run(N, f) for f in funcs}

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Cache Mechanism")
    table.add_column("Result")
    table.add_column("Time (ns)")
    table.add_column("N")

    for result in results:
        table.add_row(
            result, str(results[result][0]), str(results[result][1]), str(N)
        )

    console = Console()
    console.print(table)

if __name__ == "__main__":
    main()
