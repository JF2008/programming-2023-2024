# Jonathan Feng
# Oct.16/2023
# Star Wars Bot

import time
import sys

def printout(words):
    for letter in words:
        time.sleep(0.02)
        sys.stdout.write(letter) 
        sys.stdout.flush()   
    print("\n")


printout("I will be deciding if you can join the Dark Side.")
time.sleep(1)
printout("answer carefully.")
time.sleep(0.5)

printout("Is red your favourite color? ")
fav_color = input()

time.sleep(1)

print("\n")
printout("Do you like capes? ")
like_capes = input()

time.sleep(0.5)
print("\n")
if fav_color.lower().strip(",.?! ") == "yes":
    printout("Dark side it is!")
elif like_capes.lower().strip(",.?! ") == "yes":
        printout("Dark side it is!")
else:
     printout("Light side, I see.")

