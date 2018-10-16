# https://matplotlib.org/api/
# _as_gen/matplotlib.pyplot.quiver.html
import matplotlib.pyplot as plt

originsX = list([0, 0])
originsY = list([0, 0])
endsX = list([7, -5])
endsY = list([5, -3])

plt.quiver(originsX, originsY,
           endsX, endsY, scale=1, units='xy',
           color=['red', 'blue'])
plt.axis('equal')
plt.xticks(range(-10,10))
plt.yticks(range(-10,10))
plt.grid()
plt.show()
