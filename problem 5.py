# Chapter 5 - Problem 5
# Logistic Function Graph
# Modified from Supplemental Chapter 4 Problem 3

from graphics import *


def logistic(k, x):
    return k * x * (1 - x)


def main():
    k = float(input("Enter k: "))
    x = float(input("Enter starting value for x: "))

    win = GraphWin("Logistic Function", 700, 500)

    # Set graph coordinates
    win.setCoords(-10, -0.1, 110, 1.1)

    # Draw x-axis
    x_axis = Line(Point(0, 0), Point(100, 0))
    x_axis.draw(win)

    # Draw y-axis
    y_axis = Line(Point(0, 0), Point(0, 1))
    y_axis.draw(win)

    # Calculate and graph 100 logistic values
    for i in range(1, 101):
        x = logistic(k, x)

        point = Point(i, x)
        point.draw(win)

    # Wait for mouse click before exiting
    win.getMouse()
    win.close()


main()
