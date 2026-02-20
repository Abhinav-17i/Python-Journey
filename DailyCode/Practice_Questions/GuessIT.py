password = "python123"
guess = ""

while guess != password:
    guess = input("Enter the secret password: ")
    
    if guess != password:
        print("Wrong password! Try again :\(")

print("Access Granted! Welcome Hacker !!")