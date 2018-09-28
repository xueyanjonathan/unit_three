# Jonathan Lin
# Assignment Three
# Use turtle and functions to draw plus signs and fill color in them
# 9/28/2018

import turtle


def length_of_middle_plus_sign():
    """
    The function asks the user the side length of the plus sign and return it.
    :return:side length of a plus sign
    """
    side_length = input("What is the side length of the plus sign?")
    return float(side_length)


def color_of_plus_sign():
    """
    The functoin asks the user the color to fill in the plus signs and return it.
    :return:color of the plus sign
    """
    color = input("What is the color of the plus signs?")
    return color


def draw_a_plus_sign(color, length):
    """
    The function draws a plus sign based on the color and side length given,
    the parameters are color and side length of a plus sign,
    and the function returns nothing
    :param color: color obtained from the user's input to fill in the plus signs
    :param length: side length obtained from the user's input to draw the plus signs
    :return:none
    """
    turtle.color(color)
    turtle.begin_fill()
    for x in range(4):  # This loop draws a single plus sign with color filled in.
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(90)
    turtle.end_fill()


def draw_the_plus_sign_on_both_sides(color, length):
    """
    The function uses color and length given by the user and moves the turtle to draw plus signs on both sides of the middle plus sign.
    The parameters are color and side length of plus signs.
    The function returns nothing.
    :param color: color obtained from the user's input to fill in the plus signs
    :param length: side length obtained from the user's input to draw the plus signs
    :return: none
    """
    # These lines move the turtle to draw other plus signs.
    turtle.penup()
    turtle.forward(3 * length)
    turtle.pendown()
    # This line uses the other function to draw plus signs
    draw_a_plus_sign(color, length)
    # These lines move the turtle to draw another plus signs.
    turtle.left(180)
    turtle.penup()
    turtle.forward(6 * length)
    turtle.right(180)
    turtle.pendown()
    # This line uses the other function to draw plus signs
    draw_a_plus_sign(color, length)


def main():
    # These two lines store the color and side length obtained from the user.
    color = color_of_plus_sign()
    length = length_of_middle_plus_sign()
    turtle.speed(100)
    # Draw the middle plus sign.
    draw_a_plus_sign(color, length)
    # Draw the plus signs on the left and right sides.
    draw_the_plus_sign_on_both_sides(color, length)
    # Move the turtle to prepare it for drawing the top and bottom plus signs.
    turtle.penup()
    turtle.forward(5 * length)
    turtle.left(90)
    turtle.forward(length)
    turtle.pendown()
    # Draw the plus signs on top and bottom.
    draw_the_plus_sign_on_both_sides(color, length)
    turtle.exitonclick()


main()
