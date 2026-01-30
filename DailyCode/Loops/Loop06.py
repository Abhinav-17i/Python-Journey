import random
sum = 0
old = 0
for i in range(1,101) :
    old = sum
    ran = random.randint(1,100)
    sum += ran
    print(f"{old} + {ran} = {sum}")