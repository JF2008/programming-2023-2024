user_burger = input("Would you like a burger for $5 ")
user_fries = input("would you like fries for $3? ")
total = 0
if user_burger.lower().strip(",.?! ") == "yes":
    total += 5
if user_fries.lower().strip(",.?! ") == "yes":
    total += 3

print(f"Your total is ${total * 1.14}")







