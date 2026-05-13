
# Import necessary libraries
import numpy as np
import pandas as pd


# Define the page names
pages = ["A", "B", "C", "D"]


# Define the transition matrix (columns sum to 1)
M = np.array([
    [0.0, 0.5, 0.0, 0.0],
    [1.0, 0.0, 0.5, 0.0],
    [0.0, 0.5, 0.0, 1.0],
    [0.0, 0.0, 0.5, 0.0],
])


# Initial rank vector (equal probability)
rank = np.array([0.25, 0.25, 0.25, 0.25])


# 1. Display the transition matrix as a DataFrame with page names as labels
print(pd.DataFrame(M, index=pages, columns=pages))
print(rank)


# 2. Check that each column of the matrix adds up to 1
print("Column sums:", M.sum(axis=0))


# 3. Update the rank vector once using matrix multiplication
rank = M @ rank
print("Updated rank vector (after one multiplication):")
print(rank)


# 4. Reset rank vector to equal values
rank = np.ones(len(pages)) / len(pages)

# 5. Update rank vector 200 times (non-damped version)
for _ in range(200):
    rank = M @ rank

print("Final rank vector after 200 iterations:")
print(rank)


# 6. Damped PageRank calculation
d = 0.85  # Damping factor
N = len(pages)
rank = np.ones(N) / N  # Reset to equal values

# 7. Run the damped version for 20 steps
for _ in range(20):
    rank = d * (M @ rank) + (1 - d) * (np.ones(N) / N)

# 8. Convert the final rank vector into a Pandas Series, sort, and print
rank_series = pd.Series(rank, index=pages)
rank_series = rank_series.sort_values(ascending=False)
print("Final ranks (highest to lowest):")
print(rank_series)