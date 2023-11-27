# jonathan feng
# nov

# Function

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


def stars(num_stars: int) -> str:
    """"""
    stars = "*" * num_stars
    return stars

def biggest_of_three(num1, num2, num3):
    biggest = 0
    if num3 > num2:
        biggest = num3
    elif num1 > num3:
        biggest = num1
    elif num2 > num1:
        biggest = num2
    return biggest

def pyramid(num):
    for i in range(num):
        print("*" * int(i+1))

def pyramid_mirror(num):
    stored_pyrimid = []
    for i in range(num):
        line = "*" * int(i+1)
        stored_pyrimid.append(line)
    

        
    




print(stars(2))  #   **
print(stars(10))  #   **********
print("\n")

print_area_of_a_square(12.2)
print_area_of_a_square(13)
 #sum_areas = area_of_a_square(12.2) + area_of_a_square(13)
print(area_of_a_square(2))

print(print_area_of_a_square(2))
print("\n")

print(biggest_of_three(100,43,3))
print("\n")

pyramid(5)
pyramid_mirror(4)