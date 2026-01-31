List = [2,-3,0,5,-1,0,7]

positive = ""
negative = ""
zero = ""
 
p = []
n = []
z = []

for i in List :
    if i < 0 :
         n.append(i)
    elif i == 0 :
        z.append(i)
    else :
        p.append(i)

for i in p :
    positive += str(i) + "  "
for i in n :
    negative += str(i) + "  "
for i in z :
    zero += str(i) + "  "  

print(f'''Positive numbers in list = {positive}
Negative numbers in list = {negative}
zeroes in list = {zero}
''')
