user = input("Enter a number: ")

print(f"Reverse = {user[::-1]}")
d = ""
for i in user[::-1] :
    d += i
print(d)    