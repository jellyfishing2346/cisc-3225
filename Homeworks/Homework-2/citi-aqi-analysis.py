# Name: Faizan Khan
# Date: 2026-02-28
# Assignment: City-AQI Analysis (CISC 3225)
# Location: New York City Neighborhoods

import numpy as np


# --- Step #1: Generate the Data ----
# Task: Generate 28 readings where the mean is 75 and standard deviation is 20
aqi_related_readings = np.random.normal(75, 20, 28).astype(int)
print(f"Part I - Full AQI Array (28 Neighborhoods):\n{aqi_related_readings}\n")

# --- Step #2: Provide a summary of the AQI Readings ---
aqi_mean = np.mean(aqi_related_readings)
aqi_max  = np.max(aqi_related_readings)
aqi_min  = np.min(aqi_related_readings)
aqi_unhealthy = np.sum(aqi_related_readings >= 100)
aqi_good = np.sum(aqi_related_readings < 50)

print(f"Part II - Summary Statistics:")
print(f"Mean of AQI Readings: {aqi_mean: .2f}")
print(f"Max of AQI Readings: {aqi_max: .2f}")
print(f"Min of AQI Readings: {aqi_min: .2f}")
print(f"Unhealth count of AQI Readings (>= 100): {aqi_unhealthy}")
print(f"Good count of AQI Readings (<50): {aqi_good}\n")

# --- Step #3: Identify High-Risk Areas ---
high_risk_areas = aqi_related_readings >= 100
print(f"Part III - Risk Analysis:")
print(f"Boolean Mask (AQI Readings >= 100):\n{high_risk_areas}")
print(f"Actual High-Risk AQI Values: {aqi_related_readings[high_risk_areas]}")
print(f"Total # of High-Risk Neighborhoods: {np.sum(high_risk_areas)}")

# --- Step #4: Targeted Intervention ---
intervention_spots = [2, 7, 14, 21]
# Create a copy of the original data to ensure proper comparsion
aqi_values_updated = aqi_related_readings.copy()
aqi_values_updated[intervention_spots] -= 15

mean_updated = np.mean(aqi_values_updated)

print("Part IV - Intervention Results:")
print(f"Updated AQI Intervention Spots(2, 7, 14, 21 reduced by 15):\n{aqi_values_updated}")
print(f"Updated City-Wide Mean: {mean_updated: .2f}")
print(f"Total Change in Mean: {aqi_mean - mean_updated: .2f}")

"""
Part IV - Intervention Results Q & A
1. Did the intervention significantly change the city-wide average?
Answer: No, because despite reducing the AQI by 15 points in four specific neigborhood spots, 
the city wide mean only dropped by 2.14 points (a drop from aqi_mean to mean_updated in my specific run).
2. Why might local improvements not strongly affect global averages?
Answer: The reason is due to the dilution effect in statistics. When I average a local change
across a larger sample size (28 neighborhoods), the impact is divided by the total count (60/28≈2.14).
In a real city such as New York, this states that while localized air filtration helps specific residents, 
it doesn't solve the atmospheric issues in the city at a broader scale. 
"""

# --- Step #5: Ranking Severity (Extra Credit) ---
aqi_sorted_values = np.sort(aqi_values_updated)
print("\nPart V - Severity Ranking:")
print(f"Top 5 Lowest AQI Values (Ascending): {aqi_sorted_values[:5]}")
print(f"Top 5 Highest AQI Values (Descending): {aqi_sorted_values[-5:][::-1]}")

"""
Part V - Severity Ranking Q & A
1. Is ranking neighborhoods by AQI useful?
Answer: It is useful by resource triage as ranking can allow neighborhoods to immediately identify "hotspots"
such as neighborhoods that had an AQI of 117 or 103 that require urgent health attention or emergency health
equipment distribution. 
2. Is it always fair to focus on the worst 5?
Answer: Not always because it neglects the middle group of neighborhoods. If I only focus on the "worst 5",
then neigbhorhoods 6-10 that might have an "Unhealthy" or "Moderate" range will get no support allowing 
their quality to worsen further without intervention. 
3. What is information is lost when we sort?
Answer: The information that is at risk to be lost is spatial/geographical context. 
A sorted list tells us how many neighborhoods are at risk, but it doesn't state if they are physically next to each
other. Losing this location information makes it very impossible to trace the pollution back to a specific source, 
like a factory or highway. 
"""

# --- Step #6: Outlier Scenario ---
aqi_outlier = aqi_values_updated.copy()
aqi_outlier[0] = 250
aqi_outlier_mean = np.mean(aqi_outlier)

print("\nPart VI - Outlier Analysis")
print(f"Mean with extreme outlier (250): {aqi_outlier_mean: .2f}")
print(f"Increase in mean due to single outlier): {aqi_outlier_mean - mean_updated: .2f}")

"""
Part VI - Outlier Scenario Q & A
1. How sensitive is the mean for extreme values?
Answer: The mean is highly sensitive. As my output shows a single extreme event in one neighborhood (setting AQI to 250)
dragged the entire city's average up by 6.07 values. This single data point raises the whole city's average by 6.07 points.
This single data point makes the whole city appear significantly more polluted than it actually is. 
2. Should a single outlier influence city-wide policy?
Answer: It shouldn't because a single outlier is often an anamoly, such as sensor error or localized incident 
(like a building fire). Base-level policy should rely on more "robust" statistics like the median or trimmed mean, 
which ignore extreme outliers to provide a more accurate picture of what the typical resident is experiencing. 
"""