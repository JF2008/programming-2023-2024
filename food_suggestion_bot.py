# Food suggestion Bot
# Author: Ubial
# Date: 6 October 2023

'''
Bot aks the user what their favourite food is.
the bot identifies the type/cuisine
of the food and offes a suggestion
for what restaurant.
'''
import time
import random

# Introduce the bot to the user
# Asks user for favourite food
print("Hello, I am here to suggest a restaurant to you")
time.sleep(1)
fav_food = input("what is your favourite food")
time.sleep(1)
# If answer with italian dish we suggest a italien dish

italien_food = ["pizza", "pasta", "cannelon", "tiramisu"]
jap_food = ["shushi", "miso soup"]

# .Lower() and .Strip() are both string methods I used in this example.
if fav_food.lower().strip(",.?! ") in italien_food:  # Also in this example .lower() and .strip() catches for any possible semantic errors
    print("go to this restaurant:")
    time.sleep(1)
    print("I suggest bella roma iltalian food")
    time.sleep(1)
    print("Go to this address: 123 road")
elif fav_food.lower().strip(",.?! ") in jap_food: # Also in this example .strip() and .lower() makes the code robust
    print("go to this restaurant:")
    time.sleep(1)
    print("I suggest Gami shushi")
    time.sleep(1)
    print("Go to this address: 999 road")
else:
    print("could not find anything.")
    
