# chaos5.py
# This program demonstrates chaotic behavior.

def main():
    print("This program illustrates a chaotic function.")

    x = float(input("Enter a number between 0 and 1: "))
    k = float(input("Enter a value for k: "))

    for i in range(30):
        x = k * x * (1 - x)
        print(x)

main()
