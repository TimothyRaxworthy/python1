'''
Challenge: Handle cases where the user enters non-numeric input for the year and provide appropriate error messages.



===============================================

Input: Prompt the user to enter a year.

Processing: Determine whether the entered year is a leap year or not. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.

Output: Display whether the entered year is a leap year or not.
'''

year_int = input("Enter a year: ")

if year_int.isdigit():
    year = int(year_int)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Leap year")

    else:
        print("Not a leap year")

else:
    print("Not numeric, please enter a valid year")

