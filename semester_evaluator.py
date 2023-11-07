#jonathan

sem_courses = input("how many courses are you taking this semester")
sem_courses = int(sem_courses)
scores = []

for i in range(sem_courses):
    value = input(f"how do you rate your course {i + 1} out of 5?")
    scores.append(value)
total = 0

for i in range(sem_courses):
    total += int(scores[i])
final_score = total/sem_courses

if final_score < 1:
    print(f"{final_score}? Ouch")
elif final_score < 3:
    print(f"{final_score}? not a bad semester")
else: print(f"{final_score}? glad to hear that")