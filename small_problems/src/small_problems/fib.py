from typing import Dict, Generator
from functools import lru_cache

def naive_fib(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return naive_fib(n - 1) + naive_fib(n - 2)


memo: Dict[int, int] = {0:0, 1:1}
def memo_fib(n: int) -> int:
    if n not in memo:
        memo[n] = memo_fib(n - 1) + memo_fib(n - 2)
    return memo[n]

@lru_cache(maxsize=None)
def cache_fib(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return cache_fib(n - 1) + cache_fib(n - 2)


def iter_fib(n: int) -> int:
    if n == 0: return n
    last: int = 0 
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

def gen_fib(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next



