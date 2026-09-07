
# Problem 1
def problem1():
    initial_investment = float(input("Enter the initial investment: "))
    years = float(input("Enter the length of the investment in years: "))
    interest_rate = float(input("Enter the annual interest rate as a decimal: "))

    final_amount = initial_investment * math.exp(interest_rate * years)

    print("Final amount:", final_amount)


# Problem 2
def problem2():
    monthly_deposit = float(input("Enter the monthly deposit amount: "))
    interest_rate = float(input("Enter the annual interest rate as a decimal: "))

    k = 12
    months = 24

    final_balance = monthly_deposit * (
        ((1 + interest_rate / k) ** months - 1)
        / (interest_rate / k)
    )

    print("Final balance:", final_balance)


# Problem 3
def problem3():
    desired_amount = float(input("Enter the desired down payment amount: "))
    interest_rate = float(input("Enter the annual interest rate as a decimal: "))

    k = 12
    months = 24

    monthly_deposit = desired_amount * (interest_rate / k) / (
        (1 + interest_rate / k) ** months - 1
    )

    print("Monthly deposit needed:", monthly_deposit)


# Problem 4
def problem4():
    loan_amount = float(input("Enter the amount you want to borrow: "))
    interest_rate = float(input("Enter the annual interest rate as a decimal: "))
    years = int(input("Enter the loan term in years: "))

    k = 12

    monthly_payment = (
        loan_amount * (interest_rate / k)
        / (1 - (1 + interest_rate / k) ** (-years * k))
    )

    print("Monthly payment:", monthly_payment)


# Problem 5
def problem5():
    monthly_payment = float(input("Enter the monthly payment you can afford: "))
    interest_rate = float(input("Enter the annual interest rate as a decimal: "))

    k = 12

    loan_15_year = monthly_payment * (
        (1 - (1 + interest_rate / k) ** (-15 * k))
        / (interest_rate / k)
    )

    loan_30_year = monthly_payment * (
        (1 - (1 + interest_rate / k) ** (-30 * k))
        / (interest_rate / k)
    )

    print("Amount you can finance for 15 years:", loan_15_year)
    print("Amount you can finance for 30 years:", loan_30_year)


problem1()
problem2()
problem3()
problem4()
problem5()
