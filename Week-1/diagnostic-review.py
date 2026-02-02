# Question 1
data = [3, 7, 2, 7, 9, 3, 2]

sorted(set(data)) # [2, 3, 7, 9]

# Question 2

counts = []
for x in data: 
    counts[x] = counts.get(x, 0) + 1

# Question 3


