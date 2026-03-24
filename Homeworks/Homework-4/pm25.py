import numpy as np

np.set_printoptions(precision=2, suppress=True)

pm25 = np.array([
    [12, 18, 25, 31, 29, 15], 
    [20, 22, 35, 42, 38, 28], 
    [8, 12, 18, 21, 19, 14], 
    [15, 25, 30, 34, 40, 22]
])

# Part I - Basics
print(f"Shape of pm25: {pm25.shape}")
print(f"Stations of pm25: {pm25.shape[0]}")
print(f"Days of pm25: {pm25.shape[1]}\n")

# Part II - Average PM2.5 per station
station_mean = np.mean(pm25, axis=1, keepdims=True)
pm25_from_stations = pm25 - station_mean
print("Difference from station average:\n", pm25_from_stations, "\n")

# Part III: Normalize each station
station_maximum = np.max(pm25, axis=1, keepdims=True)
station_normalized = pm25 / station_maximum
print("Normalized values (0.0 to 1.0):\n", station_normalized, "\n")

# Part IV: EPA Standard Completion
epa_standard = 35
difference_std = pm25 - epa_standard
print("Difference from EPA standard (35):\n", difference_std, "\n")

# Part V: AQI Category Thresholds
unhealthy_category = pm25 > 35
print("Boolean mask for 'Unhealthy' (>35):\n", unhealthy_category, "\n")

# Part VI: Calibration
calibrate = np.array([1.5, -0.5, 0.8, 1.9])
adjusted_measurements = pm25 + calibrate.reshape(-1,1)
print("Calibrated Measurements:\n", adjusted_measurements)