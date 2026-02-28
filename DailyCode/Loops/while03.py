#Multiplication table

n = int(input("Enter the number : "))

mul = 0

for i in range(1,11) :
    mul = n * i

    print(f"{n} x {i} = {mul}")
    

    