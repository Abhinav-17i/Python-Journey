import random
#it's a mistake please ignore.
# User_choice = int(input("What do you choose?\nType 0 for rocks,1 for paper,2 for scissors\n"))
# rock = "Rock"
# paper = "Paper"
# scissor = "Scissors"

# if User_choice  == 0 :
#     print("Computer chose: " +rock)

# elif User_choice == 1:
#     print("Computer chose: " + paper)

# elif User_choice == 2:
#     print("Computer chose: " + scissor)

# else :
#     print("Wrong input")

user = int(input("What do you choose?\nType 0 for rocks,1 for paper,2 for scissors\n"))
if user == 0 :
    print('''You chose :
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif user == 1:
    print('''You chose :
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif user == 2:
    print(''' You chose :
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')  
else : 
    print("Invalid input") 
    exit()      

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock,paper,scissor]

ran = random.choice(choices)
comp = print("Computer chose : \n" + ran)
if user == 0 :
    if ran == rock :
        print("It's a draw")
    elif ran == paper:
        print("You lose")
    else :
        print("You win")
elif user == 1:
    if ran == rock :
        print("You win")
    elif ran == paper:
        print("It's a draw")
    else :
        print("You lose")
elif user == 2:
    if ran == rock :
        print("You lose")
    elif ran == paper:
        print("You win")
    else :
        print("It's a draw")
else :
    print("Invalid input.")
