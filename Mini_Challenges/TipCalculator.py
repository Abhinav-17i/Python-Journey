print("Welcome to tip Calculator!")
bill = float(input("what's the total bill: "))
tip = float(input("How much % would you like to tip?(10.12 or 15)\n"))
split = float(input("How many people will the bill be split into: "))

Total_pay = (bill*(tip/100)+bill)/split

print("Welcome to tip Calculator!")

print(f"Each person should pay: {round(Total_pay, 3)}")
