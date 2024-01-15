# Robot Puppy
# Author: Jonathan Feng
# Jan.15/2024

import colour_helper
from PIL import Image

Red_ball_img = Image.open("./Images/Red Ball.jpeg")

Red_pixel = []

for y in range(Red_ball_img.height):
    for x in range(Red_ball_img.width):
        # Get the pixel information
        current_pixel = Red_ball_img.getpixel((x, y))

        if colour_helper.pixel_to_name(current_pixel) == "red":
            Red_pixel.append((x, y))

max_val = max(Red_pixel)
min_val = min(Red_pixel)

sumy = max_val[1] + min_val[1]
mid_y = sumy / 2
sumx = min_val[0] + max_val[0]
mid_x = sumx / 2

print(f"The mid point of ball is: {mid_x}, {mid_y}")
