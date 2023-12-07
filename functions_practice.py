# jonathan feng
# nov

# Function

# Functions Practice
# Author: Ubial
# 24 November 2023


def print_area_of_a_square(sidelength: float) -> None:
    """Calculates the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square"""

    area = sidelength**2

    print(
        f"The area of a square with side length = {sidelength} is: {area} square units"
    )


def area_of_a_square(sidelength: float) -> float:
    """Returns the area of a square with given
    sidelength

    Params:

    sidelength - length of one side of a square
    """
    area = sidelength**2

    return area


# print_area_of_a_square(12.2)
# print_area_of_a_square(13)
# sum_areas = area_of_a_square(12.2) + area_of_a_square(13)
# print(area_of_a_square(2))

# print(print_area_of_a_square(2))

# Question 1:
# Create a function called stars()
# Takes an int as a parameter
# Returns a string of stars of given length


# Aside: Signature of a function
#     - name of the function
#     - inputs/parameters / type
#     - return type


def stars(num_stars: int) -> str:
    """Returns a string of stars of given length"""

    return "*" * num_stars


print(stars(5))
print(stars(100))

# Question 2:
# Create a function called biggest_of_three()
# Takes three parameters, all floats
# Returns the biggest one


def biggest_of_three(num_one: float, num_two: float, num_three: float) -> float:
    """Returns the biggest of three given numbers.

    Params:
    num_one - the first number
    num_two - the second number
    num_three - the third number

    Returns:
    the biggest of the three numbers
    """
    if num_one > num_two and num_one > num_three:
        return num_one
    elif num_two > num_three:
        return num_two
    else:
        return num_three


print(biggest_of_three(1000, 100, 10))
print(biggest_of_three(100, 1000, 10))
print(biggest_of_three(10, 100, 1000))

# Question 3
# Question 4
# Create functions called pyramid() and pyramid_mirror()
# Takes one number as a parameter
# Give a pyramid either regular way or mirrored


def pyramid(num_layers: int) -> None:
    """Prints out a pyramid of given number of layers.

    Params:
    num_layers - number of layers in the pyramid
    """

    for current_layer in range(1, num_layers + 1):
        print(stars(current_layer))

pyramid(2)
pyramid(3)
pyramid(20)

def pyramid_mirror(num_layers: int) -> None:
    """Print a pyramid mirrored of given number
    of layers.

    Params:
    num_layers - number of layers in the pyramid
    """

    for current_layer in range(1, num_layers + 1):
        # Spaces is equal to total num of layers
        # minus the stars in the current layer
        spaces = " " * (num_layers - current_layer)

        print(spaces + stars(current_layer))

pyramid_mirror(2)
pyramid_mirror(3)
pyramid_mirror(20)


def linear_search(l: list, item: any) -> int:
    """Search through a list and if found,
    returns the index of the first occurence
    of the item.

    Params:
            l - list we're search through
            item - item we're looking for

    Returns:
            index if found, -1 if not found
    """
    counter = 0

    # search algorithm
    for thing in l:
        if thing == item:
            return counter
        counter += 1

    return -1

pockets = ["coins", "lint", "paperclip", "keys", "wallet"]

results = linear_search(pockets, "keys")

if results == -1:
    print("Your keys are not in your pockets")
else:
    print(f"Found your keys! They're in the {results}th index.")