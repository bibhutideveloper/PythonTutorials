a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if (a>b and a>c):
    print(a," is greatest.")
elif (b>a and b>c):
    print(b, " is greatest.")
elif (c>a and c>b):
    print(c," is greatest.")
else:
    print("All the  numbers are same.")