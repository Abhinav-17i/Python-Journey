numbers = [5, 2, 9, 1, 7]

smallest = numbers[0]

for n in numbers:
    if n < smallest:
        smallest = n

print("Smallest:", smallest)
