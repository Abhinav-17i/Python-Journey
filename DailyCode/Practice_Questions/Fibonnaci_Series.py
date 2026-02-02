#Question 7
user =  int(input("Enter the fibonacci series length: "))

count = 0

a = 0
b = 1

while count < user :
    oldA = a
    print(a,end=" ")
    a =  b
    b = oldA + b
    count += 1