import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Step #1: Create the coordinate grid
x = np.arange(256).reshape(1, 256)
y = np.arange(256).reshape(256, 1)
distance_from_center = np.sqrt((x-128)**2 + (y-128)**2)

# Create a vignette mask (1.0 at center, fading to 0.0 at edges)
vingette_mask = np.clip(1.0 - (distance_from_center / 181.0), 0, 1)

fig, ax = plt.subplots(figsize=(6,6))
im = ax.imshow(np.zeros((256,256,3), dtype=np.uint8))
plt.title("Broadcasting Art: Plasma Ripples (Animated)")
plt.axis('off')

def update(frame):
	phase = frame * 0.1
	# R: Concentric ripples using a sine wave for distance
	ripples = (128 + 127 * np.sin(distance_from_center / 5.0 + phase)).astype(np.uint8)
	# G: A shifting diagonal wave pattern using modulo and addition
	wave_pattern = ((x * 2) + (y * 2) % 256).astype(np.uint8)
	# B: A plasma-like interference pattern combining sine waves of x and y 
	plasma_pattern = (128 + 127 * np.cos((x/ 10.0) + phase) * np.sin(y/15.0)).astype(np.uint8)
	# Apply vignette to each channel
	R_vingette_mask = (ripples * vingette_mask).astype(np.uint8)
	G_vingette_mask = (wave_pattern * vingette_mask).astype(np.uint8)
	B_vingette_mask = (plasma_pattern * vingette_mask).astype(np.uint8)
	rgb_value = np.dstack((R_vingette_mask, G_vingette_mask, B_vingette_mask)).astype(np.uint8)
	im.set_data(rgb_value)
	return [im]

ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()