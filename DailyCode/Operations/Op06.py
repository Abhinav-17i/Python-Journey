age = int(input("Enter your age: "))

has_id = input("Do you have ID? (yes/no): ")

if age >= 18 and has_id == "yes":
    print("Eligible to vote")
else:
    print("Not eligible")