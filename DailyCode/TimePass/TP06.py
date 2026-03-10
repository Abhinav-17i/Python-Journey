list = [2,4,9,5,8,6,1,7]

n = int(input("Enter the number you want to find: "))

found =  False
for i in range (0,len(list)) :
    if list[i] == n :
        print(f"The entered number found at index {i}")
        found = True
        break
if not found :
    print("Not Found")
    # print("Nahi mila")


