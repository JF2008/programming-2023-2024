# Turtle example
# Author: Jonathan
# 21 November 2023

import turtle

# constants
turtle_magnitude = 100

# create a turtle

michael = turtle.Turtle() #get turtle


# Get some intructions from the user
print("""To give commands, type:
      f - to go forward
      l - to go left
      r - to go right
      b - go back
      Stop - stop""")

done = False

while not done:
    command = input("Where should I go?").strip(",.?! ").lower()

    # BAsed on intructions move the turtle on the screen



    if command == "f":
        michael.forward(turtle_magnitude)
    if command == "l":
        michael.left(90)
        michael.forward(turtle_magnitude)
    if command == "r":
        michael.right(90)
        michael.forward(turtle_magnitude)
    if command == "b":
        michael.back(turtle_magnitude)
    elif command == "stop":
        done = True




turtle.done()