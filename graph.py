import time
import matplotlib.pyplot as plt

###

def blue(n):
    sum = 0
    for k in range(1, n + 1):
        sum += k
    return sum


def orange(n):
    sum = n * (n + 1) / 2
    return sum


#####

values = list(range(10, 100))   # 10..99
orangeResults = list(range(90)) # 0..89
blueResults = list(range(90))   # 0..89
orangeTimes = list(range(90))   # 0..89
blueTimes = list(range(90))     # 0..89

for x in range(10, 100):
    t1 = time.perf_counter()
    orangeResults[x - 10] = orange(x)
    t2 = time.perf_counter()
    orangeTimes[x - 10] = t2 - t1

    t1 = time.perf_counter()
    blueResults[x - 10] = blue(x)
    t2 = time.perf_counter()
    blueTimes[x - 10] = t2 - t1

plt.plot(values, orangeTimes, "*", color="orange")
plt.plot(values, blueTimes, "-", color="blue")
plt.savefig("graph.png")
plt.show()
print(values)
print(orangeResults)
print(blueResults)
