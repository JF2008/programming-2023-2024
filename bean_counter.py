# Jelly Bean Colour Counter                                
# Author: Jonathan Feng
# 9 January 2024

# Version 0.3
#  - Count red, green, and yellow pixels/beans
#  - Report on the percentage of all red, green, and yellow beans
#  - create map for green and yellow beans

from PIL import Image

import colour_helper

RED_PIXEL = (160, 0, 0)
GREEN_PIXEL = (0, 160, 0)
YELLOW_PIXEL = (255,255,0)

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")

red_pixels = []
green_pixels = []
yellow_pixels = []

# Visit every pixel in the image
for y in range(jelly_bean_img.height):
    for x in range(jelly_bean_img.width):
        # Get the pixel information
        current_pixel = jelly_bean_img.getpixel((x, y))

        if colour_helper.pixel_to_name(current_pixel) == "red":
            red_pixels.append((x, y))
        elif colour_helper.pixel_to_name(current_pixel) == "jelly bean green":
            green_pixels.append((x, y))
        elif colour_helper.pixel_to_name(current_pixel) == "jelly bean yellow":
            yellow_pixels.append((x, y))

orig_image_width = jelly_bean_img.width
orig_image_height = jelly_bean_img.height

green_pixel_map = Image.new("RGB", (orig_image_width, orig_image_height))
yellow_pixel_map = Image.new("RGB", (orig_image_width, orig_image_height))

for pixel_loc in green_pixels:
    green_pixel_map.putpixel(pixel_loc, GREEN_PIXEL)

for pixel_loc in yellow_pixels:
    yellow_pixel_map.putpixel(pixel_loc, YELLOW_PIXEL)

# Save the image
green_pixel_map.save("./Images/green_pixel_map.jpg")
green_pixel_map.close()

yellow_pixel_map.save("./Images/yellow_pixel_map.jpg")
yellow_pixel_map.close()

# Count all the locations of red pixels
red_pixel_count = len(red_pixels)
green_pixel_count = len(green_pixels)
yellow_pixel_count = len(yellow_pixels)
total_pixels = jelly_bean_img.width * jelly_bean_img.height

# Divide by the total pixels in the image
red_pixel_percentage = red_pixel_count / total_pixels * 100
green_pixel_percentage = green_pixel_count / total_pixels * 100
yellow_pixel_percentage = yellow_pixel_count / total_pixels * 100

# Generate the report
print(f"Red Jelly Beans: {round(red_pixel_percentage, 2)}%")
print(f"Green Jelly Beans: {round(green_pixel_percentage, 2)}%")
print(f"Yellow Jelly Beans: {round(yellow_pixel_percentage, 2)}%")

jelly_bean_img.close()

                                                                       

