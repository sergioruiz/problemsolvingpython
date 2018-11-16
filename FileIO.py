import matplotlib.pyplot as plt
xs = list()
ys = list()
zs = list()

myFile = open("Book1.csv", "r")
for line in myFile:
    line = line.replace('\n','')
    values = line.split(",")
    xs.append(float(values[0]))
    ys.append(float(values[1]))
    zs.append(float(values[2]))

print(xs)
print(ys)
print(zs)

plt.plot(xs, ys, "+", color="red")
plt.plot(xs, zs, "*", color="blue")
plt.show()
