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
    alfred_river_wilson.speed(0)
    if level > 0:

        alfred_river_wilson.forward(height)
        
        alfred_river_wilson.left(39)
        
        draw_tree(level - 1, height * 0.75)
        
        alfred_river_wilson.right(39 * 2)
        
        draw_tree(level - 1, height * 0.75)

        alfred_river_wilson.left(39)
        alfred_river_wilson.back(height)
    else:
       
        original_colour = alfred_river_wilson.color()
        alfred_river_wilson.color("green")
        alfred_river_wilson.stamp()
        alfred_river_wilson.color(original_colour[0])

alfred_river_wilson.setheading(90)
alfred_river_wilson.width(4)
alfred_river_wilson.color("brown")
alfred_river_wilson.shape("arrow")
alfred_river_wilson.speed(3)

draw_tree(5, 100)

turtle.done()