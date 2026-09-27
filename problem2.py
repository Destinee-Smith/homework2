# Chapter 5 - Problem 2
# Kelvin to Fahrenheit Conversion Table

def KToF(k):
    return (k - 273.15) * 9 / 5 + 32


def main():
    print("Kelvin\tFahrenheit")
    print("----------------------")

    for k in range(0, 301, 20):
        fahrenheit = KToF(k)
        print(f"{k}\t{fahrenheit:.2f}")


main()
