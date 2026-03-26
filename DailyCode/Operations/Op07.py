num = int(input("Enter a number: "))

result = "Power of 2" if (num > 0 and (num & (num - 1)) == 0) else "Not a power of 2"

print(result)