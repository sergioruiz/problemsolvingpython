import random
# Lists

theEmptyList = []
print(theEmptyList)

#          0    1   2   3
numbers = [11, 99, 66, 22]
print(numbers[2])

#           string        float   int
#               0            1     2
mixed = ["just a string", 3.1415, 199]
print(mixed)
print(len(mixed))
# lists are mutable:
mixed[0] = "another string"

for i in mixed:
    print(i)

listByRange = list(range(1, 101))
for e in range(len(listByRange)):
    listByRange[e] = random.randint(-10, 10)

# List slicing:   listName[from:to]
# print indices from 10 to 19:
print(listByRange[10:20])
# print indices from 90 to the end:
print(listByRange[90:])
# print indices from 0 to 9
print(listByRange[0:10])

# Find out if -3 is in the list:
print("Is -3 on listByRange?")
print(-3 in listByRange)

def factorial(x):
    theList = list(range(1, x+1))
    result = 1
    for i in theList:
        result = result * i
    return result

f = factorial(4)
print(f)

# len returns the num. of items
print(len(listByRange))
print(sum(listByRange))
print("MAX=", max(listByRange))
print(min(listByRange))

# Write a function to compare two lists.
# 1. It checks if the lists have the same length
# 2. Compares element-by-element
# 4. Returns True or False