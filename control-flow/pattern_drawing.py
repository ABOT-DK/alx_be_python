patter = int(input("Enter the size of the pattern:"))
row = 0

while row < patter:  
    for i in range(patter):
        print("*", end="")
    print()
    row += 1
    