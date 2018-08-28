num = int(input("Enter a number!"))
c = num
fac = 1
while c > 1:
    fac = fac * c
    c = c - 1
print("F(", num, ")=", fac)
