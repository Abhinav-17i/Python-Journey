List = [2,-3,0,5,-1,0,7]

pos = 0
negative = 0
zero = 0

for i in List :
    if i < 0 :
        negative +=1
    elif i == 0 :
        zero += 1
    else :
        pos += 1

print(f'''Positive numbers in list = {pos}
Negative numbers in list = {negative}
zeroes in list = {zero}
''')