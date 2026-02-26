numbers = (12, 7, 9, 20, 33, 18, 5)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Tuple:", numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)