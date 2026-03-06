import numpy as np

# Step #1: Create AQI values and Neighorhood Identifiers
np.random.seed(42)
mean = 75
standard_deviation = 20
neighborhoods = 28 

# Take the created aqi values to convert them into integers
aqi_values_integers = np.random.normal(mean, standard_deviation, neighborhoods).astype(int)

# Create neighborhoods (0-27)
number_neighborhoods = np.array([f"N{j:02d}" for j in range(neighborhoods)])

# Step #2: Create Initial Print Statements of the AQI values and Neighborhood mapping
print("--- Original Data ---")
print("Neighborhood Array: ", number_neighborhoods)
print("AQI Values: ", aqi_values_integers)
print("\n--- Neighborhood AQI Mapping ---")
for number_neighbor, aqi in zip(number_neighborhoods, aqi_values_integers):
    print(f"{number_neighbor} : AQI = {aqi}")

# Step #3: Sorting AQI Values (Actual Values, not Indices)
aqi_sorted_values = np.sort(aqi_values_integers)
print("\n--- AQI Statistics ---")
print("Top 5 Lowest AQI Values (Ascending):", aqi_sorted_values[:5])
print("Top 5 Highest AQI Values (Descending): ", aqi_sorted_values[::-1][:5])

# Step #4: Ranking the top 5 cleanest neighborhoods and top 5 polluted neighborhoods with argsort()
# Using argsort to return the indices that would sort the array
aqi_sorted_values = np.argsort(aqi_values_integers)

# Print the Top 5 Cleanest Neighborhoods
print("\n--- Top 5 Cleanest Neighborhoods ---")
for j in aqi_sorted_values[:5]:
    print(f"{number_neighborhoods[j]} : AQI = {aqi_values_integers[j]}")

# Print the Top 5 Most Polluted Neighborhoods
print("\n--- Top 5 Most Polluted Neighborhoods ---")
for j in aqi_sorted_values[::-1][:5]:
    print(f"{number_neighborhoods[j]} : AQI = {aqi_values_integers[j]}")

# Step #5: Intervention: Air Filtering System
air_filteration = [2, 7, 14, 21]
aqi_values_integers[air_filteration] -= 15

print("\n--- Post-Intervention Data")
print("Updated AQI Values by Indices 2, 7, 14, 21 reduced by 15: ")
print(aqi_values_integers)
print(f"Updated Mean AQI: {np.mean(aqi_values_integers):.2f}")

# Step #6: Recompute the rankings after the intervention
updated_aqi = np.argsort(aqi_values_integers)
print("\n--- Top 5 Worst Neighborhoods Post-Intervention ---")
for j in updated_aqi[::-1][:5]:
    print(f"{number_neighborhoods[j]} : AQI = {aqi_values_integers[j]}")