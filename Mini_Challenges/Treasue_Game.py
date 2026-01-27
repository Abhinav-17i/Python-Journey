print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')
print("\n")
print("Welcome to the Treasure Island!\nYou are at a crossroad.Where do you want to go?")
Direction = input("Type left or right\n").lower()
if Direction == "right":
    print("You're arrived near a lake,There's an island in middle of the lake.\nWould you like to wait for a boat or swim across.")
    Swim = input("Chosse wait or swim\n").lower()
    if Swim == "wait":
        print("You've successfully arrived at the island.\nThere are three doors in front of you.")
        Door = input("Choose a door to go through.red,blue or yellow.\n").lower()
        if Door == "red" or Door == "blue" :
            print("You got eaten by a monster.Game over.")
        else:
            print("Congratulations! You got the treasure.")
    else:
        print("You got eaten by a Crocodile.Game over.")
            

else: 
    print("You fell in a pit.Game over")    
