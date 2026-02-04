
import random
from collections import Counter
import timeit

nums = [random.randint(0,100) for _ in range(1000)]

def freqdict1(nums):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    return counts

def freqdict2(nums):
    return Counter(nums)

def freqdict3(nums):
    return {x:nums.count(x) for x in set(nums)}

def printdict(d):
    for x in d:
        print(f"key: {x}, value: {d[x]}")
    print()


#print(f"results from freqdict1:")
#printdict(freqdict1(nums))
#print(f"results from freqdict2:")
#printdict(freqdict2(nums))
#print(f"results from freqdict3:")
#printdict(freqdict3(nums))

t1 = timeit.timeit(lambda:freqdict1(nums),number=10000)
t2 = timeit.timeit(lambda:freqdict2(nums),number=10000)
t3 = timeit.timeit(lambda:freqdict3(nums),number=10000)

print(f"t1: {t1}, t2: {t2}, t3: {t3}")
