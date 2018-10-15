# Debt Calculator

# This program will allow the user to input how many debts they have. Then it will take in the name and amount of the debt separated by a comma, without spaces.
# Next the user will input how much they will pay towards the debt every month. The program will then calculate how many months it will take to pay off the
# total_debt by breaking it down to years and months. It will collect the current month/year from the computer and add the time required to pay off the debt.



import datetime


# user_debt = dict() is slower than the below code
user_debt = {}


# Collecting the number of debts from the user
number_of_debt = int(input("Enter your number of debts as a number."))
total_debt = 0
x = 1

# Checking to see if user is debt free.
if number_of_debt == 0:
    print("CONGRATS! You have zero debts!")
    
else:
    # Loop to collect the name & debt amount of the number of debts the user defined.
    while x <= number_of_debt:
        user_input_debt = input("Enter your debt name and the amount of the debt separated by a comma (,):")
        debt_name, debt_value = user_input_debt.split(",")

        # Removing the whitespace and making sure debt_value is an interger. 
        debt_name = debt_name.strip()
        debt_value = int(debt_value.strip())

        user_debt[debt_name] = debt_value

        total_debt += debt_value
        x += 1
        
    else:
        income = int(input("How much are you putting towards your debt every month?"))

        months_paying = int(total_debt / income)

# Grabbing current month/year to be used later
current_year = datetime.date.today().year
current_month = datetime.date.today().month

# Checks to see how long the user has left to pay the debt down to zero.
if months_paying == 0:
    print("You will be debt free in less than a month!")
    years_to_pay = 0
    months_left_to_pay = months_paying
elif months_paying > 12:
    years_to_pay = months_paying / 12
    months_left_to_pay = months_paying % 12
else:
    months_left_to_pay = months_paying
    years_to_pay = 0
    
final_month = int(current_month + months_left_to_pay)

# Check to see if the year rolls over with current month + months to pay. ex: Aug + 6 months = Jan of the next year.
if final_month > 12:
    years_to_pay += 1
    final_month = final_month - 12

final_year = int(current_year + years_to_pay)
    
print("It will take you", months_paying, "months to pay off", total_debt, ". You started in", current_month, "/", current_year, ". And you will finish in", final_month, "/", final_year, ".")








    
