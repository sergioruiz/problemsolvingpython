import random
import math
import matplotlib.pyplot as plt

# c1 = [c1x, c1y, c1r]
c1 = list()
c1.append(random.uniform(0, 5))
c1.append(random.uniform(0, 5))
c1.append(random.uniform(0.8, 1.4))

# c2 = [c2x, c2y, c2r]
c2 = list()
c2.append(random.uniform(0, 5))
c2.append(random.uniform(0, 5))
c2.append(random.uniform(0.8, 1.4))

# Plot the circles:
# circle = plt.Circle((x,y), r, options)
circle1 = plt.Circle((c1[0], c1[1]), c1[2], color='r')
circle2 = plt.Circle((c2[0], c2[1]), c2[2], color='b')

fig, ax = plt.subplots()
plt.axis('equal')
ax.set_xlim(-2, 7)
ax.set_ylim(-2, 7)
ax.add_artist(circle1)
ax.add_artist(circle2)

text1 = "C1=[{:4.2f}, {:4.2f}, {:4.2f}]".format(c1[0], c1[1], c1[2])
ax.annotate(text1, xy=(c1[0], c1[1]), color='lime', weight='bold')
text2 = "C2=[{:4.2f}, {:4.2f}, {:4.2f}]".format(c2[0], c2[1], c2[2])
ax.annotate(text2, xy=(c2[0], c2[1]), color='lime', weight='bold')

# Compute if they're colliding:
dx = (c2[0] - c1[0])**2
dy = (c2[1] - c1[0])**2
dist = math.sqrt(dx + dy)
sumr = c1[2] + c2[2]

# Display collision information:
text3 = "NO COLLISION"
if dist < sumr:
    text3 = " COLLISION!!!"
    fig.text(0, 0, text3, color='red')
else:
    fig.text(0, 0, text3)

# Save the figure:
fig.savefig('collision.png')

# Show the plot:
plt.show()
