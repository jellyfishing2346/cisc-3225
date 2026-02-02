# Question 1
data = [3, 7, 2, 7, 9, 3, 2]

sorted(set(data)) # [2, 3, 7, 9]

# Question 2

counts = {}
for x in data: 
    counts[x] = counts.get(x, 0) + 1 #{3: 2, 7: 2, 2: 2, 9: 1}


# Question 3
nums = [1, 2, 3, 4, 5]
result = []
for i in range(len(nums) - 1):
    result.append(nums[i+1]-nums[i]) # [1, 1, 1, 1]



