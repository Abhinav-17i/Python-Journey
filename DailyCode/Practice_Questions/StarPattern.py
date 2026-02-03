user = int(input("Enter a number\n"))

for i in range(1, user + 1):
    for j in range(i):
        print("*", end="")
    print()
