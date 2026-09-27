# Chapter 5 - Problem 1
# Logistic Chaos Function

def chaos(k, x, n):
    for i in range(n):
        x = k * x * (1 - x)
        print(x)


def main():
    k = float(input("Enter k: "))
    x = float(input("Enter starting value for x: "))
    n = int(input("Enter number of iterations: "))

    chaos(k, x, n)


main()
