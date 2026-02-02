print("Welcome to the number guessing game!\n")
user = int(input("Enter a number from 1 to 10 :\n"))

secret = 3

while user !=  secret :
    print("Try again")
    user = int(input("Enter a number from 1 to 10 :\n"))

print("You guessed correctly. You win!!!")