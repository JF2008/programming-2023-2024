# Similar hobbies
# Jonathan Feng


print("Please enter hobbies, separated by spaces.")
person1 = input("Person 1: ").lower()
person2 = input("Person 2: ").lower()

p1 = person1.split(" ")
p2 = person2.split(" ")

sim_score = 0

for hobbies in p1:
    if hobbies in p2:
        sim_score += 1

print(f"You have {sim_score} hobbies in common")