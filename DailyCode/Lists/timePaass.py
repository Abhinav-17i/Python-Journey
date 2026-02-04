nums = [1, 2, 3, 2, 4, 2, 5,1,7,9,8,4,1,7,2,1,8,9,5,5,4,2,1,3,7,8,9,3]
target = int(input("Enter number to count: "))

count = 0

for n in nums:
    if n == target:
        count += 1

print("Appears", count, "times")
