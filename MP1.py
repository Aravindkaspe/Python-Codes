#
# Machine Problem 1
#
# Aravind Kumar Kaspe
#
# Description: This script prompts the user for their name, the year they were
#              born, and the balance in their savings account. A greeting is output
#              along with the projected year of retirement, and an estimate
#              of what their savings account will be worth at that time. Three
#              assumptions are made. (1) the current year is 2023, (2) retirement
#              age is 65, and (3) the annual rate of growth for the savings
#              account will be 7%.
#
print("Let's see how much money you will have when you retire.\n")

user_name = input("What is your name? ")
year_of_birth = int(input("What year were you born? "))
account_balance = float(input("What is the balance of your savings account? "))

user_age = 2023 - year_of_birth
retirement_year = year_of_birth + 65
pending_retirement_years = retirement_year - 2023
estimated_savings = account_balance*((1.07)**pending_retirement_years)

print("\nHello,", user_name + "!")
print("You turn", user_age, "this year.")
print("You will retire in", str(retirement_year),end=".\n")
print("That will be", pending_retirement_years, "years from now.")
print("Congratulations! You will have $", estimated_savings, " by that time.", sep='')

