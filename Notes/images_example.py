# images example
# jonathan
# dec 14

from PIL import Image


def pixel_to_name(pixel: tuple) -> str:
    """Given a 3-tuple, return a string representing
    its colour

    Params:
        pixel = 3-tuple of values (red, green, blue)

    Returns:
        name of the colour
    """
    red, green, blue = pixel

    if red < 25 and blue < 25 and green > 249:
        return "green"
    else:
        return "colour unknown"


# open up kid green
with Image.open("./Images/kid-green.jpg") as im:
    # create variables that store the width and height
    image_height = im.height
    image_width = im.width

    # open background image
    bg_im = Image.open("./Images/beach.jpg")

    # starting at the top and working our way down
    # visit the pixels from left to right
    for y in range(image_height):
        for x in range(image_width):
            pixel = im.getpixel((x, y))

            if pixel_to_name(pixel) == "green":
                # replace it with bg_im pixel in same loc
                bg_pixel = bg_im.getpixel((x, y))

                im.putpixel((x, y), bg_pixel)

    bg_im.close()

    # Save image
    im.save("./Images/output.jpg")

