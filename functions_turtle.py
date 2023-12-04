# functions and turtle 
#author: jonathan 
# 28 nov 2023

import turtle

alfred_river_wilson = turtle.Turtle()
alfred_river_wilson.color("lightgreen")
alfred_river_wilson.shape("turtle")


def squared(num: float) -> float:
    """Returns the given number squared"""
    return num**2


def draw_square(side_length: float) -> None:
    for _ in range(4):
        alfred_river_wilson.forward(side_length)
        alfred_river_wilson.left(90)


def draw_tree(level: int, height: int) -> None:
    """A recursive function that draws a tree
    with initial given height

    Params:

    level - number representing levels of branches
    height - height of the main trunk in pixels
    """

    if level > 0:
        # 1. Draw the branch
        alfred_river_wilson.forward(height)

        # 2. Turn to the left
        alfred_river_wilson.left(39)

        # 3. Draw a smaller tree (current level - 1)
        draw_tree(level - 1, height / 1.5)

        # 4. Turn to the right
        alfred_river_wilson.right(39 * 2)

        # 5. Draw a smaller tree (current level - 1)
        draw_tree(level - 1, height / 1.5)

        # 6. Move back to beginning
        alfred_river_wilson.left(39)
        alfred_river_wilson.back(height)
    else:
        # create a level 0 tree, which is a leaf
        original_colour = alfred_river_wilson.color()
        alfred_river_wilson.color("green")
        alfred_river_wilson.stamp()
        alfred_river_wilson.color(original_colour[0])


# Setting ARWilson to draw the tree
# alfred_river_wilson.hideturtle()
alfred_river_wilson.setheading(90)
alfred_river_wilson.width(4)
alfred_river_wilson.color("brown")
alfred_river_wilson.shape("arrow")
alfred_river_wilson.speed(3)

draw_tree(10, 150)

turtle.done()