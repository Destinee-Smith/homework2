# Chapter 5 - Problem 4
# N-Sided Polygon
# Requires Zelle graphics.py

from graphics import *
import math


def ngon(n, center, radius):
    angle = 360 / n
    vertices = []

    for i in range(n):
        theta = math.radians(i * angle)

        x = center.getX() + radius * math.cos(theta)
        y = center.getY() + radius * math.sin(theta)

        vertices.append(Point(x, y))

    polygon = Polygon(vertices)

    return polygon


def drawGraph(win, entry, button):
    win.getMouse()

    n = int(entry.getText())

    polygon = ngon(n, Point(250, 250), 150)
    polygon.draw(win)

    button.setText("Exit")


def main():
    win = GraphWin("N-Sided Polygon", 500, 500)

    label = Text(Point(150, 40), "Number of Sides:")
    label.draw(win)

    entry = Entry(Point(300, 40), 5)
    entry.setText("5")
    entry.draw(win)

    button = Text(Point(250, 460), "Graph")
    button.draw(win)

    drawGraph(win, entry, button)

    win.getMouse()
    win.close()


main()
