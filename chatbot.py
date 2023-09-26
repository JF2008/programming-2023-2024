"""
chatbot
Author: Jonathan Feng
Date: Sept.21/2023

"""
import random
import time

y = ""
Favourite_food_responses = ["wow that sounds nice", 
"I love that food too", 
f"{y} is my favourite food too!", 
]
Food_response = random.choice(Favourite_food_responses)

#Greet user and store it
print("hi I am a intelligent chatbot")
time.sleep(2)
x = input("what is your name?")

#respond with users name
time.sleep(1)
print(f"nice to meet you {x}")

#Ask user for favourite food
y = input("What is also your favourite food?")

#replies with good answer
time.sleep(1)
print(Food_response)


