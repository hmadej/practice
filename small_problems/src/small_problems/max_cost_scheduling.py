from typing import List, Dict, Tuple, Set
from time import process_time
from random import randint

# assumes jobs are ordered by increasing start times -> 1, 2, 3, ...

def memo(f):
    memo = dict()
    def wrapper(x):
        if (key := frozenset(x)) not in memo:
            memo[key] = f(x)
        return memo[key]
    return wrapper


@memo
def take(jobs: List) -> int:
    if len(jobs) == 0:
        return 0

    start_index = 1
    start, end, cost = jobs[0]

    for index, job in enumerate(jobs[1:]):
        if end <= job[0]:
            start_index = index
            break
    print(start_index)

    return max(cost + take(jobs[start_index+1:]), take(jobs[1:]))
    
@memo
def binary_take(jobs: List) -> int:
    if len(jobs) == 0:
        return 0
 
    start, end, cost = jobs[0]
    start_index = binary_search(end, jobs[1:])
    print(start_index)
    
    return max(cost + take(jobs[start_index+1:]), take(jobs[1:]))


def binary_search(target, l: List) -> int:
    half_size = len(l) // 2
    index = half_size
    while ((value := l[index]) != target and half_size != 1):
        half_size = (half_size // 2)
        if value[0] > target:
            index -= half_size
        else:
            index += half_size
    return index


start  = [randint(1,1000) for _ in range(50)]
end    = [randint(1,1000)+1 for _ in range(50)]
volume = [randint(50,1000) for _ in range(50)]

jobs = sorted(list(zip(start, end, volume)), key = lambda x: x[0])


t = process_time()
res = take(jobs)
elapsed_t = process_time() - t
print(res, elapsed_t)


t = process_time()
res2 = binary_take(jobs)
elapsed_t2 = process_time() - t
print(res2, elapsed_t2)

