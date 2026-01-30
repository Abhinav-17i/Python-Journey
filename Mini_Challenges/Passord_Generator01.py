import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','&','*']

no_user = int(input("How many numbers do you want in password?\n"))

letters_user = int(input("How many letters do you want in your password?\n"))

symbols_user = int(input("How many symbols do you want in your password?\n"))

password = ""

for i in range(1,letters_user + 1) :
    password += random.choice(letters) 

for j in range(1,symbols_user + 1) :
    password += random.choice(symbols)

for k in range(1,no_user + 1) :
    password += random.choice(numbers)

print("Your password is ",password)