import math
investment = """Investment - to calculate the amount of interest you'll 
earn on your investment"""

bond = """Bond - to calculate the amount 
you'll have to pay on a home loan"""

print(investment)
print(bond)

#collect user input on the type of calculation 
calculation_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

#collect user input and calculate interest based on interest types
if calculation_type == "investment":
    deposit = float(input("Enter the amount of money you are depositing: "))
    int_rate1 = float(input("Enter the interest rate: "))
    years = int(input("How many years do you plan to invest?: "))
    interest_type = input("Do you want 'simple' or 'compound' interest?: ").lower()
    if interest_type == "simple":
        simple_interest = deposit * (1 + int_rate1 / 100 * years)
        print(round(simple_interest, 2))
    elif interest_type == "compound":
        compound_interest = deposit * math.pow((1 + int_rate1/100), years)
        print(round(compound_interest, 2))
    else:
        print("Invalid entry, try again!")

elif calculation_type == "bond":
    house_value = float(input("Enter the present value of the house?: "))
    int_rate2 = float(input("Enter the interest rate: "))
    months = int(input("Enter the number of months you will pay on bond: "))

    monthly_rate = (int_rate2 / 100) / 12
    repayment = (monthly_rate * house_value) / (1 - (1 + monthly_rate) ** (-months))
    print(round(repayment, 2))
else:
    print("Invalid entry, try again!")



