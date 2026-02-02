
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def window_sum(nums, k):
   
    results = []
    for i in range(len(nums) - k + 1):
        results.append(sum(nums[i:i+k]))
    return results 

print(window_sum(nums, 3))
# Time complexity: O(n*k)

def window_optimized(nums, k):
    total = sum(nums[:k])
    results = [total]
    for i in range(len(nums)-k):
        total -=  nums[i]
        total +=  nums[i+k]
        results.append(total)
    return results

print(window_optimized(nums,3))
# Time complexity: O(n)

t1 = timeit(lambda:window_sum(nums), number=10000)
        

   
