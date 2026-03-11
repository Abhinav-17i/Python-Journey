A = [1, 2, 3, 4]
B = [3, 4, 5, 6]

result = []

for x in A + B:
    if x not in result:
        result.append(x)

print(result)
