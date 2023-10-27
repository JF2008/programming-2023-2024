# Bubble Tea
# Jonathan Feng
# Oct.27

# ask 5 users what their favourite bubble tea is
# Ptint out all data

# Ask the user what their favourite bubble place is

# Options: CoCo, Chatime, Suntea, Xing fu Tang

coco_likes = 0
suntea_likes = 0
chattime_likes = 0
xing_likes = 0

print("What's your favourite bubble tea place?")

fave_bbt = input().strip(",.?! ").lower()

if fave_bbt == "coco":
    coco_likes += 1
elif fave_bbt == "chatime":
    chattime_likes += 1
elif fave_bbt == "suntea":
    suntea_likes += 1
