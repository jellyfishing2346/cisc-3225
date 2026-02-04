

import timeit
import random

def win1(nums, k):
    results = []
    for i in range(len(nums) - k + 1):
        results.append(sum(nums[i:i+k]))
    return results

def win2(nums, k):
    total = sum(nums[:k])
    results = [total]
    for i in range(len(nums) - k):
        total -= nums[i]
        total += nums[i+k]
        results.append(total)
    return results

def win3(nums, k):
    return [sum(nums[i:i+k]) for i in range(len(nums) - k + 1)]

nums = [random.randint(0, 100) for _ in range(1000)]
k = 4

# correctness check
assert win1(nums, k) == win2(nums, k) == win3(nums, k)

t1 = timeit.timeit(lambda: win1(nums, k), number=1_000)
t2 = timeit.timeit(lambda: win2(nums, k), number=1_000)
t3 = timeit.timeit(lambda: win3(nums, k), number=1_000)

print(f"t1:{t1}, t2:{t2}, t3:{t3}")
