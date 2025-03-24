import numpy as np
import pygame
from pygame.locals import QUIT
def normalize(v):
    return v / np.linalg.norm(v)
def dot(v1, v2):
    return np.dot(v1, v2)
def subtract(v1, v2):
    return v1 - v2
def add(v1, v2):
    return v1 + v2
def multiply(v, s):
    return v * s
class Sphere:
    def __init__(self, center, radius, color):
        self.center = np.array(center)
        self.radius = radius
        self.color = np.array(color)
    def intersect(self, origin, direction):
        oc = subtract(origin, self.center)
        a = dot(direction, direction)
        b = 2.0 * dot(oc, direction)
        c = dot(oc, oc) - self.radius * self.radius
        discriminant = b * b - 4.0 * a * c
        if discriminant < 0:
            return None
        else:
            t1 = (-b - np.sqrt(discriminant)) / (2.0 * a)
            t2 = (-b + np.sqrt(discriminant)) / (2.0 * a)
            return min(t1, t2) if t1 > 0 else max(t1, t2)
width, height = 400, 400
camera_origin = np.array([0, 0, -1])
light_position = np.array([0, 5, -5])
sphere = Sphere(center=[0, 0, 3], radius=1, color=[255, 0, 0])
def trace_ray(origin, direction, spheres, light_position):
    closest_t = float('inf')
    closest_sphere = None
    hit_point = None
    normal = None
    for sphere in spheres:
        t = sphere.intersect(origin, direction)
        if t is not None and t < closest_t:
            closest_t = t
            closest_sphere = sphere
            hit_point = add(origin, multiply(direction, t))
            normal = normalize(subtract(hit_point, sphere.center))
    if closest_sphere is None:
        return np.array([0, 0, 0])  
    light_dir = normalize(subtract(light_position, hit_point))
    illumination = max(dot(normal, light_dir), 0)
    color = multiply(closest_sphere.color, illumination)
    return color
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("g")
fov = np.pi / 3  
aspect_ratio = width / height
spheres = [sphere]
running = True
for y in range(height):
    for x in range(width):
        px = (2 * (x + 0.5) / width - 1) * np.tan(fov / 2) * aspect_ratio
        py = -(2 * (y + 0.5) / height - 1) * np.tan(fov / 2)
        direction = np.array([px, py, 1])
        direction = normalize(direction)
        color = trace_ray(camera_origin, direction, spheres, light_position)
        screen.set_at((x, y), tuple(np.clip(color, 0, 255).astype(int)))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            break
pygame.time.wait(3000)
pygame.quit()
