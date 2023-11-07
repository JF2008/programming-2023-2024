continents = ['Asia', 'South America', 'North America', 'Africa', 'Europe', 'Antarctica', 'Australia']

name = input("Hi what is your name?")
print(f"Hello, {name} its nice to meet you")

visited = 0

for cont in continents:
    value = input(f"Have you been to {cont}?")
    if value.lower() == "yes":
        visited += 1

print(f"You have been to {visited}/7 continents")