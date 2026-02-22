fruits = ("apple", "banana", "mango", "orange", "grapes")

print("First fruit:", fruits[0])

print("Last fruit:", fruits[-1])

print("Total fruits:", len(fruits))

if "mango" in fruits:
    print("Mango is in the tuple")
else:
    print("Mango is not in the tuple")

print("All fruits:")
for fruit in fruits:
    print(fruit)