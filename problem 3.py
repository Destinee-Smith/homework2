# Chapter 5 - Problem 3
# Loan Payment Calculator

def calcPmt(P0, r, k, N):
    rate = r / k
    periods = N * k

    if rate == 0:
        return P0 / periods

    d = (P0 * rate) / (1 - (1 + rate) ** (-periods))

    return d


def main():
    P0 = float(input("Enter amount to finance: "))
    r = float(input("Enter annual interest rate (%): ")) / 100
    k = int(input("Enter number of times interest is compounded per year: "))
    N = int(input("Enter number of years: "))

    payment = calcPmt(P0, r, k, N)

    print(f"Monthly payment: ${payment:.2f}")


main()
