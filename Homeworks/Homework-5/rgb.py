import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Setup coordinate grid
x = np.arange(256).reshape(1, 256)
y = np.arange(256).reshape(256, 1)
dist = np.sqrt((x - 128)**2 + (y - 128)**2)
vignette = np.clip(1.0 - (dist / 181.0), 0, 1)

fig, ax = plt.subplots(figsize=(6, 6))
# Initialize with an empty RGB array
im = ax.imshow(np.zeros((256, 256, 3), dtype=np.uint8))
plt.axis('off')
plt.title("Broadcasting Art: Animated Plasma")

def update(frame):
    # 'frame' acts as the time variable to make it move
    phase = frame * 0.2
    
    # R: Moving ripples
    R = (128 + 127 * np.sin(dist / 5.0 - phase))
    # G: Shifting diagonal waves
    G = (x * 2 + y * 2 + phase * 10) % 256
    # B: Pulsing plasma
    B = (128 + 127 * np.cos(x / 10.0 + phase) * np.sin(y / 15.0))

    # Apply vignette and stack
    # We do the math as floats, then cast to uint8 at the very end
    rgb = np.dstack((
        (R * vignette),
        (G * vignette),
        (B * vignette)
    )).astype(np.uint8)
    
    im.set_data(rgb)
    return [im]

# blit=True makes the animation much smoother and faster
ani = FuncAnimation(fig, update, frames=200, interval=30, blit=True)
plt.show()