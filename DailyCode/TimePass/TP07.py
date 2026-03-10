user = input("Enter a number: ")

d = ""

for i in reversed(user) :
    d += i

print(f"Reverse = {d}")