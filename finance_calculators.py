# Using import function to use certain math .
import math

# Declaring two placeholder variables for later use.
user_total = ""
user_calc = ""

# Asking user for input and declaring a variable for said input.
user_input = input("Choose either 'investment' or 'bond' from the menu below to proceed:\n\n"
                   "Investment      - to calculate the amount of interest you'll earn on interest.\n"
                   "Bond            - to calculate the amount you'll have to pay on a home loan.\n"
                   ": ").lower()

# Using 'if' statement to ask user for input if a certain condition is met.
if user_input == "investment":
    invest_amount = float(input("Please enter the amount of money you would like to invest.\n"
                                ": "))
    invest_rate = float(input("Please enter the interest rate of your investment.\n"
                              ": "))
    invest_year = float(input("How many years would you like to invest.\n"
                              ": "))
    interest = input("Would you prefer simple or compound interest.\n"
                     ": ").lower()

# Declaring a new value for a variable.
    invest_rate = invest_rate / 100

# Using 'if', 'elif' and 'else' statements to do calculations or print a response if certain conditions are met.
    if interest == "simple":
        user_calc = (invest_amount * (1 + (invest_rate * invest_year)))
        user_total = "R{:,.2f}".format(user_calc)
        print(f"The total amount of your investment will be {user_total}")

    elif interest == "compound":
        user_calc = (invest_amount * math.pow((1 + invest_rate), invest_year))
        user_total = "R{:,.2f}".format(user_calc)
        print(f"The total amount of your investment will be {user_total}")

    else:
        print("You have not chosen either of the above options.")

# Using 'if', 'elif' and 'else' statements to do calculations or print a response if certain conditions are met.
elif user_input == "bond":
    bond_amount = float(input("Please enter current value of property.\n"
                              ": "))
    bond_rate = float(input("Please enter the interest rate of your bond.\n"
                            ": "))
    bond_length = float(input("Please enter the number of months you play to repay your bond.\n"
                              ": "))

    bond_rate = (bond_rate / 100) / 12

    user_calc = bond_rate * bond_amount / (1 - math.pow((1 + bond_rate), - bond_length))
    user_total = "R{:,.2f}".format(user_calc)
    print(f"Your monthly installment will be {user_total}")

else:
    print("You have not chosen either of the above options.")
