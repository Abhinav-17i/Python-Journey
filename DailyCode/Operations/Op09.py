amount = float(input("Enter total purchase amount: "))
is_member = input("Are you a member? (yes/no): ").lower()

discount = 0.2 if amount > 1000 else 0.1 if amount > 500 else 0

discount += 0.05 if is_member == "yes" else 0

final_price = amount - (amount * discount)

print("\nDiscount Applied:", discount * 100, "%")

print("Final Price to Pay:", final_price)