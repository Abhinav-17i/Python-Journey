print("Welcome to the roller coaster")
Height = int(input("Whats your height in cm?\n"))
Bill = 0
if Height>=120:
    print("You can ride the roller coaster")
    age = int(input("Whats your age?\n"))
    if age<12:
     Bill = 5
     print("Please pay $5")
    elif age<=18:
     Bill = 7
     print("Please pay $7")
    else:
     Bill = 10
     print("Please pay $10")
    photo = input("Dou you want to tatke a photo? y for Yes and n for no: ")
    if photo == "y" :
      Bill += 3
      print(f"Your total bill is: ${Bill}")     
else:
    print("You can't ride the roller coaster")