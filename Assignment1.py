'''
Challenge: Handle cases where the user enters non-numeric input for the principal amount, interest rate, or time period, and provide appropriate error messages.

=============================
Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
Output: Display the calculated simple interest.
'''

#we will be handling the input section below

principal = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period: "))

#This is the processing phase below
simple_interest = (principal * interest_rate * time) / 100

#The output section is below
print("Simple Interest: ", simple_interest)

