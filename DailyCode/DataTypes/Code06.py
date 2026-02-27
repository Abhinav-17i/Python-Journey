age = int(input("Enter your age: "))
invitation = input("Do you have invitation (True/False): ")
vip = input("Are you VIP (True/False): ")

# Convert string input to Boolean
invitation = invitation == "True"
vip = vip == "True"

# Boolean condition
allowed = (age >= 18 and invitation) or vip

print("Entry Allowed:", allowed)