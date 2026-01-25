print("Welcome to the roller coaster")
Height = int(input("Whats your height in cm?\n"))

if Height>=120:
    print("You can ride the roller coaster")
    age = int(input("Whats your age?\n"))
    if age<12:
     print("Please pay $5")
    elif age<=18:
     print("Please pay $7")
    else:
     print("Please py $10")    
else:
    print("You can't ride the roller coaster")