# Jonathan Lin
# Assignment Three
# Use turtle and functions to draw plus signs and fill color in them

import turtle


def length_of_middle_plus_sign():
    """
    Ask the user the side length of the plus sign and return it.
    :return:
    """
    side_length = input("What is the side length of the plus sign?")
    return float(side_length)


def color_of_plus_sign():
    """
    Ask the user the color to fill in the plus signs and return it.
    :return:
    """
    color = input("What is the color of the plus signs?")
    return color


def draw_a_plus_sign(color, length):
    """
    draw a plus sign based on the color and side length given
    :param color:
    :param length:
    :return:
    """
    turtle.color(color)
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(90)
    turtle.end_fill()

 
def main():
    """
    Run all the functions
    :return:
    """
    color = color_of_plus_sign()
    length = length_of_middle_plus_sign()
    turtle.speed(100)
    draw_a_plus_sign(color, length)
    turtle.exitonclick()


main()
