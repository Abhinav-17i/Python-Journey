print("Welcome to the pizza deliveries!")
size = input("What size pizza would you like? S,M or L:\n")
pepperoni = input("Would you like peperoni on your pizza Y or N:\n")
cheese =  input("Do you want extra cheese on your pizza? Y OR N:\n")
Bill = 0

if size=="L" :
    Bill += 25
elif size == "M" :
    Bill += 20
else:
    Bill += 15

if pepperoni == "Y":
    if size == "S":
        Bill += 2
    else:
        Bill += 3    
if cheese == "Y":
    Bill += 1

print(f"Thanks for ordering,your total bill is: ${Bill}")           