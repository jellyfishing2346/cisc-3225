import numpy as np
import matplotlib.pyplot as plt

# Step #1: Create the coordinate grid
x = np.arange(256).reshape(1, 256)
y = np.arange(256).reshape(256, 1)
distance_from_center = np.sqrt((x-128)**2 + (y-128)**2)

# Step #2: Geometric layers
# Changing the 'phase' to see the ripples move!
phase = 0.5

# Step #3: R: Concentric ripples using a sine wave for distance
ripples = (128 + 127 * np.sin(distance_from_center / 5.0 + phase)).astype(np.uint8)

# Step #4: G: A shifting diagonal wave pattern using modulo and addition
wave_pattern = ((x * 2) + (y * 2) % 256).astype(np.uint8)

# Step #5: B: A plasma-like interference pattern combining sine waves of x and y 
plasma_pattern = (128 + 127 * np.cos((x/ 10.0) + phase) * np.sin(y/15.0)).astype(np.uint8)

# Create a vinette mask (1.0 at center, fading to 0.0 at edges)
# I use 181 as the approximate max distance to the corners
vingette_mask = np.clip(1.0 - (distance_from_center / 181.0), 0, 1)

# Applying vingette to each channel before stacking
# Note: I mutiply the float mask by the uint8 color, then cast back to uint8
R_vingette_mask = (ripples * vingette_mask).astype(np.uint8)
G_vingette_mask = (wave_pattern * vingette_mask).astype(np.uint8)
B_vingette_mask = (plasma_pattern * vingette_mask).astype(np.uint8)

# Step #6: Stack the calculations for an RGB image
rgb_value = np.dstack((R_vingette_mask, G_vingette_mask, B_vingette_mask)).astype(np.uint8)
# Step #7: Print the final result
plt.figure(figsize=(6,6))
plt.imshow(rgb_value)
plt.title("Broadcasting Art: Plasma Ripples")
plt.axis('off')
plt.show()