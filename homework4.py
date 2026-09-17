from graphics import *
import math


# Supplemental Chapter 4 - Homework 4


# Problem 1
def problem1():
    sides = int(input("Enter the number of sides: "))
    radius = float(input("Enter the radius: "))

    win = GraphWin("Problem 1 - Regular Polygon", 600, 600)

    center_x = 300
    center_y = 300
    angle = 360 / sides
    vertices = []

    for i in range(sides):
        theta = math.radians(i * angle)

        x = center_x + radius * math.cos(theta)
        y = center_y + radius * math.sin(theta)

        vertices.append(Point(x, y))

    polygon = Polygon(vertices)
    polygon.draw(win)

    win.getMouse()
    win.close()


# Problem 2
def problem2():
    sides = int(input("Enter the number of sides: "))
    radius = float(input("Enter the radius: "))

    win = GraphWin("Problem 2 - Rotated Polygon", 600, 600)

    center_x = 300
    center_y = 300
    angle = 360 / sides
    vertices = []

    rotation = 90 + (angle / 2)

    for i in range(sides):
        theta = math.radians((i * angle) + rotation)

        x = center_x + radius * math.cos(theta)
        y = center_y + radius * math.sin(theta)

        vertices.append(Point(x, y))

    polygon = Polygon(vertices)
    polygon.draw(win)

    win.getMouse()
    win.close()


# Problem 3
def problem3():
    k = float(input("Enter a value for k: "))
    value = float(input("Enter a starting value between 0 and 1: "))

    win = GraphWin("Problem 3 - Logistic Function", 800, 600)

    win.setCoords(-10, -0.1, 110, 1.1)

    # Draw x-axis
    x_axis = Line(Point(0, 0), Point(100, 0))
    x_axis.draw(win)

    # Draw y-axis
    y_axis = Line(Point(0, 0), Point(0, 1))
    y_axis.draw(win)

    # Plot 100 points
    for x in range(100):
        value = k * value * (1 - value)

        point = Point(x, value)
        point.draw(win)

    win.getMouse()
    win.close()


# Problem 4
def problem4():
    k = float(input("Enter a value for k: "))
    value = float(input("Enter a starting value between 0 and 1: "))

    win = GraphWin("Problem 4 - Logistic Function", 800, 600)

    win.setCoords(-10, -0.1, 110, 1.1)

    # Draw x-axis
    x_axis = Line(Point(0, 0), Point(100, 0))
    x_axis.draw(win)

    # Draw y-axis
    y_axis = Line(Point(0, 0), Point(0, 1))
    y_axis.draw(win)

    previous_point = None

    for x in range(100):
        value = k * value * (1 - value)

        current_point = Point(x, value)
        current_point.draw(win)

        if previous_point is not None:
            line = Line(previous_point, current_point)
            line.draw(win)

        previous_point = current_point

    win.getMouse()
    win.close()


# Problem 5
def problem5():
    win = GraphWin("Problem 5 - Logistic Function", 800, 650)

    # Input labels
    k_label = Text(Point(100, 30), "Enter k:")
    k_label.draw(win)

    value_label = Text(Point(100, 70), "Starting value:")
    value_label.draw(win)

    # k input
    k_entry = Entry(Point(220, 30), 10)
    k_entry.setText("3.9")
    k_entry.draw(win)

    # Starting value input
    value_entry = Entry(Point(220, 70), 10)
    value_entry.setText("0.5")
    value_entry.draw(win)

    # Graph button
    button = Rectangle(Point(300, 15), Point(400, 55))
    button.draw(win)

    button_text = Text(Point(350, 35), "Graph")
    button_text.draw(win)

    # Wait for Graph button
    while True:
        click = win.getMouse()

        if 300 <= click.getX() <= 400 and 15 <= click.getY() <= 55:
            break

    k = float(k_entry.getText())
    value = float(value_entry.getText())

    # Draw x-axis
    x_axis = Line(Point(50, 600), Point(750, 600))
    x_axis.draw(win)

    # Draw y-axis
    y_axis = Line(Point(50, 150), Point(50, 600))
    y_axis.draw(win)

    previous_point = None

    # Graph 100 values
    for x in range(100):
        value = k * value * (1 - value)

        screen_x = 50 + (x * 7)
        screen_y = 600 - (value * 450)

        current_point = Point(screen_x, screen_y)
        current_point.draw(win)

        if previous_point is not None:
            line = Line(previous_point, current_point)
            line.draw(win)

        previous_point = current_point

    # Change Graph button to Exit
    button_text.setText("Exit")

    # Wait for Exit button
    while True:
        click = win.getMouse()

        if 300 <= click.getX() <= 400 and 15 <= click.getY() <= 55:
            break

    win.close()
