import random
Friends = ["Abhinav","Rushikesh","Tanmay","Nishant","Harshal"]
print(f"the one paying bill is {Friends[random.randint(0,4)]}")

#Another way

print("The one paying the bill is " + random.choice(Friends))