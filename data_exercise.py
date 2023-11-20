# File Exercises
# Author: Jonathan Feng
#

"""Instructions:

Put this file in your programming folder.
Download the data-example.csv file and put it in this same folder.
For each problem, design a solution.
Each part builds on the previous step, so don't skip any.
You can refer to the work that we did last day for any hints.
Do not use any generative AI for the solutions."""

# Since our file has some symbols in it, this is the most
# effective way at opening up the file.

with open("./data_example.csv", encoding="utf-8") as f:
    firstline = f.readline()
    
# Note that I've set the encoding parameter to "utf-8"

# --- Problems


# Problem 1:
# Open the file and print the contents of the second line in the file.

    print(f.readline())


# Problem 2:
# Good! Now that you've done that, open the file, and print out every line of data.
    for line in f:
        print(line)

# Problem 3:
# If you've made it this far, well done. Next task:
# Convert that line of data into a list.
        list = line.split(",")

# Problem 4:
# Give yourself a pat on the back.
# See if you can count how many people like "Chicken Adobo" as their
# favourite food.
with open("./data_example.csv", encoding="utf-8") as f:
    chicken_Adobo_count = 0
    for line in f:
        current_likes = line.split(",")
        for item in current_likes:
            if item == "Chicken Adobo":
                chicken_Adobo_count += 1
    print(f"chicken adobo count: {chicken_Adobo_count}")
        

# Problem 5:
# You should have gotten four people for the last problem. If not,
# see if why your code doesn't work.
# Else, you can move on to this part, which is, find out how many
# people have the first letter of their first name start with "A".

with open("./data_example.csv", encoding="utf-8") as f:
    poeple_with_A = 0
    for line in f:
        current_list = line.split(",")
        name = current_list[0]
        for letter in name:
            if letter == "A":
                poeple_with_A += 1
            break
    print(f"Poeple with A: {poeple_with_A}")
# Problem 6:
# 19 people! Excellent. How many people come from Guangzhou?

with open("./data_example.csv", encoding="utf-8") as f:
    Guangzhou_count = 0
    for line in f:
        current_list = line.split(",")
        city = current_list[4]
        if city == "Guangzhou\n":
            Guangzhou_count += 1
    print(f"Poeple who came form gaungzhou: {Guangzhou_count}")


# Problem 7:
# Just one is from Guangzhou! Alright, last one. How many people have a credit card
# number that is even. There are a couple of ways to solve this.
# You can either do this with the string or with the int.

with open("./data_example.csv", encoding="utf-8") as f:
    even_numbers = [2, 4, 6, 8, 0]
    even_number_count = 0
    header = f.readline()
    for line in f:
        list = line.split(",")
        current_credit_card_number = list[3]
        if int(current_credit_card_number) % 2 == 0:
            even_number_count += 1
    print(f"poeple with even credit card numbers: {even_number_count}")

        

# Problem 8*:
# Sorry, no answer for the above one. This one is a challenge question.
# Can you design a way to find the most popular food?

with open("./data_example.csv", encoding="utf-8") as f:
    most_popular_food = ""
    header = f.readline()
    food_list = []
    for line in f:
        list = line.split(",")
        Fav_food = list[1]
        food_list.append(Fav_food)
    def most_frequent(List):
        return max(set(List), key = List.count)
    print(f"The most popular food is: {most_frequent(food_list)}")









