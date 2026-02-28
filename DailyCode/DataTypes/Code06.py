age = int(input("Enter your age: "))
invitation = input("Do you have invitation (True/False): ")
vip = input("Are you VIP (True/False): ")

invitation = invitation == "True"
vip = vip == "True"

allowed = (age >= 18 and invitation) or vip

print("Entry Allowed:", allowed)