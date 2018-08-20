import math
import random

cx1 = random.uniform(-10, 10)
cy1 = random.uniform(-10, 10)
cz1 = random.uniform(-10, 10)
print("C1=[", cx1, ", ", cy1, ", ", cz1, "]")
r1 = random.uniform(1, 8)
print("R1=", r1)
print("\n")

cx2 = random.uniform(-10, 10)
cy2 = random.uniform(-10, 10)
cz2 = random.uniform(-10, 10)
print("C2=[", cx2, ", ", cy2, ", ", cz2, "]")
r2 = random.uniform(1, 8)
print("R2=", r2)
print("\n")

dx = cx2 - cx1
dx2 = dx * dx
dy = cy2 - cy1
dy2 = dy * dy
dz = cz2 - cz1
dz2 = dz * dz
distance = math.sqrt(dx2 + dy2 + dz2)
print("DISTANCE: ", distance)
sumR = r1 + r2
print("SUM RADIUS: ", sumR)
print("COLLISION: ", distance < sumR)
