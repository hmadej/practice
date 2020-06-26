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
            break
        start_index += 1

    return max(cost + take(jobs[start_index+1:]), take(jobs[1:]))
    

@memo
def binary_take(jobs: List) -> int:
    if len(jobs) == 0:
        return 0
 
    start, end, cost = jobs[0]
    start_index = binary_search(end, jobs[1:])
    if (end > jobs[start_index][0]):
        start_index += 1
    
    return max(cost + binary_take(jobs[start_index+1:]), binary_take(jobs[1:]))

def binary_search(target, l: List) -> int:
    if (size := len(l)) == 0:
        return 0
    bottom = 0
    top = size
    while (bottom < top):
        middle = (bottom + top) // 2
        if l[middle][0] < target:
            bottom = middle + 1
        else:
            top = middle
    return bottom


start  = [randint(1,2500) for _ in range(5000)]
end    = [randint(1,1000) + x for x in start]
volume = [randint(5,100) for _ in start]

jobs = sorted(list(zip(start, end, volume)), key = lambda x: x[0])


t = process_time()
res = take(jobs)
elapsed_t = process_time() - t
print(res, elapsed_t)


t = process_time()
res2 = binary_take(jobs)
elapsed_t2 = process_time() - t
print(res2, elapsed_t2)
