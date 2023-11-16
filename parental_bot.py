# jonathan feng

score = 0

q1 = input("Did you eat? ").lower()
q2 = input("Did you study? ").lower()
q3 = input("Did you do your laundry? ").lower()
q4 = input("Did you call grandma? ").lower()

if q1 == "yes":
    score += 1
if q2 == "yes":
    score += 1
if q3 == "yes":
    score += 1
if q4 == "yes":
    score += 1

if score <= 2:
    print("Ok.")
elif score <= 4:
    print("Good!")