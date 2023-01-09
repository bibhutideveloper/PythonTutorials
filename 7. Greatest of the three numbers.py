n = int(input("Enter range: "))
total = 0

if n>0:
    for i in range(1,n+1):
        total += i
    print(total)
else:
    print("Enter number >1")
        
