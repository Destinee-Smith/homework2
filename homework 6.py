def chaos(k, x, n):
    for i in range(n):
        x = k * x * (1 - x)
        print(x)


def main():
    k = float(input("Enter the value for k: "))
    x = float(input("Enter a value for x between 0 and 1: "))
    n = int(input("Enter the number of iterations: "))

    if x < 0 or x > 1:
        print("Error: x must be between 0 and 1.")
        return

    chaos(k, x, n)


main()

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if side1 == side2 and side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age.")
elif age <= 12:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
elif age <= 64:
    print("You are an adult.")
elif age <= 99:
    print("You are a senior.")
else:
    print("Congratulations on reaching 100 or more years old!")

from graphics import *

def button_clicked(point):
    x = point.getX()
    y = point.getY()

    if 100 <= x <= 200 and 100 <= y <= 150:
        return True
    else:
        return False


win = GraphWin("Button Click", 300, 250)

button = Rectangle(Point(100, 100), Point(200, 150))
button.draw(win)

button_text = Text(Point(150, 125), "Button")
button_text.draw(win)

for i in range(10):
    mouse_click = win.getMouse()

    if button_clicked(mouse_click):
        message = Text(Point(150, 200), "The button was clicked.")
    else:
        message = Text(Point(150, 200), "The button was not clicked.")

    message.draw(win)
    win.getMouse()
    message.undraw()

win.close()

def check_prime(n):
    found = False

    for i in range(2, n):
        if n % i == 0:
            found = True

    return found


n = int(input("Enter an integer: "))

found = check_prime(n)

if n <= 1:
    print(n, "is not prime.")
elif found == False:
    print(n, "is prime.")
else:
    print(n, "is not prime.")
