"""
solor rr r r  rr r rsyntem

SQUIRERLE GAY SSOOOOOOOS ACORMS

sorry I'm high
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

planets = {
    "Mercury": [0.4, 4.1, 0.4, "gray"],
    "Venus": [0.7, 1.6, 0.9, "navajowhite"],
    "Earth": [1.0, 1.0, 1.0, "royalblue"],
    "Mars": [1.5, 0.5, 0.5, "orangered"],
    "Jupiter": [5.2, 0.08, 11.2, "sandybrown"],
    "Saturn": [9.5, 0.03, 9.4, "khaki"],
    "Uranus": [19.2, 0.01, 4.0, "lightblue"],
    "Neptune": [30.1, 0.006, 3.9, "mediumblue"]
}


sun = ax.scatter([0], [0], [0], s=300, color='yellow', edgecolors='orange')


planet_points = {}
for planet, data in planets.items():
    distance = data[0]
    x, y, z = distance, 0, 0
    size = 10 * data[2]
    planet_points[planet] = ax.scatter([x], [y], [z], s=size, color=data[3], alpha=0.8)


theta = np.linspace(0, 2*np.pi, 100)
for planet, data in planets.items():
    distance = data[0]
    x = distance * np.cos(theta)
    y = distance * np.sin(theta)
    z = np.zeros_like(theta)
    ax.plot(x, y, z, color='gray', alpha=0.2)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-35, 35])
ax.set_ylim([-35, 35])
ax.set_zlim([-35, 35])
ax.set_title("solor sys,t,r,r,,r,r,")


def update(frame):
    for planet, data in planets.items():
        distance = data[0]
        speed = data[1]
        angle = (frame * speed) % 360
        rad = np.radians(angle)
        x = distance * np.cos(rad)
        y = distance * np.sin(rad)
        z = 0 
        planet_points[planet]._offsets3d = ([x], [y], [z])
    return list(planet_points.values())

animation = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), 
                          interval=50, blit=False)

plt.tight_layout()
plt.show()
