# winter holidays review
# author: Jonathan Feng
# 8 jan 2024

# -- create a function called winter holidays
# --takes one perameter that is a string
# -- returns summary of events from holiday

import sys
import random
import time

# this is just to make it more fancy
def printout(words):
    for char in words:
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()   
    print("\n")

def winter_holiday(good_or_bad: str) -> str:
    """ give a summary of our winter holiday 
    Params: 
        good or bad - indicate what kind of events to summarize
    Returns:
        an event that happened during the holidays"""
    response = ""
    good_events = ["I went to a restuarant!", "I went to my friends house!", "I read a good book during the holidays", "I got a cool christmas gift for christmas :D"]
    bad_events = ["I had a bad dream", "I was tired", "my arm was sore"]
    if good_or_bad.strip(",.! ").lower() == "good":
        response = random.choice(good_events)
    elif good_or_bad.strip(",.! ").lower() == "bad":
        response = random.choice(bad_events)

    return response
    

def main() -> None:
    printout("your input(good or bad): ")
    user_input = input()
    print("--------------------------")
    printout(winter_holiday(user_input))


if __name__ == "__main__":
    main()
