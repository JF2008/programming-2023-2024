# Bubble Tea
# Jonathan Feng
# Oct.27

# ask 5 users what their favourite bubble tea is
# Ptint out all data

# Ask the user what their favourite bubble place is

# Options: CoCo, Chatime, Suntea, Xing fu Tang

NUM_RESPONDENTS = 5

coco_likes = 0
chatime_likes = 0
suntea_likes = 0
other = 0
xingfutang_likes = 0
bbqueen_likes = 0

for _ in range(NUM_RESPONDENTS):
    print("What's your favourite bubble tea place?")

    fave_bbt = input().strip(",.?! ").lower()

    if fave_bbt == "coco":
        coco_likes += 1
    elif fave_bbt == "chatime":
        chatime_likes += 1
    elif fave_bbt == "suntea":
        suntea_likes += 1
    elif fave_bbt == "xingfutang":
        xingfutang_likes += 1
    elif fave_bbt == "bbqueen":
        bbqueen_likes += 1
    else:
        other += 1

# Print a summary of the results
coco_percentage = coco_likes / NUM_RESPONDENTS * 100
chatime_percent = chatime_likes / NUM_RESPONDENTS * 100
suntime_percent = suntea_likes / NUM_RESPONDENTS * 100
xing_percent = xingfutang_likes / NUM_RESPONDENTS * 100
bbqueen_percent = bbqueen_likes / NUM_RESPONDENTS * 100
other_percent = other / NUM_RESPONDENTS * 100

print(f"CoCo Likes: {coco_likes}   Percentage: {round(coco_percentage, 2)}%")
print(f"chatime Likes: {chatime_likes}   Percentage: {round(chatime_percent, 2)}%")
print(f"Suntea Likes: {suntea_likes}   Percentage: {round(suntime_percent, 2)}%")
print(f"xingfutang Likes: {xingfutang_likes}   Percentage: {round(xing_percent, 2)}%")
print(f"bbqueen Likes: {bbqueen_likes}   Percentage: {round(bbqueen_percent, 2)}%")
print(f"Other Likes: {other}   Percentage: {round(other_percent, 2)}%")



