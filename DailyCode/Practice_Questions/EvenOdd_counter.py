#This have to enter a number 'n' and this code will figure out how many even and odd numbers are there from 1to 'n'
print("Welcome to even & odd counter this code will guess how many even and odd numbers are there from 1 to any number you enter.")

n = int(input("Enter a number :\n"))

even = 0
odd = 0

for i in range(1,n + 1) :
    if i%2 == 0 :
        even += 1
    else :
        odd +=1

print(f"There are {even} even numbers from 1 to {n}.")
print(f"There are {odd} odd numbers from 1 to {n}.")

        
