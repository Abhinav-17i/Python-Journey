print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______
____/______/______/______/______/_____"=.o|o_.--""___/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')

print("\n")
print("Welcome to Treasure Island!")
print("You are at a crossroad. Where do you want to go?")

direction = input("Type left or right\n").strip().lower()

if direction == "right":
    print(
        "You've arrived near a lake. "
        "There's an island in the middle of the lake.\n"
        "Would you like to wait for a boat or swim across?"
    )

    swim = input("Choose wait or swim\n").strip().lower()

    if swim == "wait":
        print(
            "You've successfully arrived at the island.\n"
            "There are three doors in front of you."
        )

        door = input(
            "Choose a door to go through: red, blue or yellow.\n"
        ).strip().lower()

        if door == "yellow":
            print("Congratulations! You got the treasure.")
        elif door == "red" or door == "blue":
            print("You got eaten by a monster. Game over.")
        else:
            print("Invalid choice. Please choose red, blue, or yellow.")

    else:
        print("You got eaten by a crocodile. Game over.")

else:
    print("You fell in a pit. Game over.")
