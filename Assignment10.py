'''
Challenge: Implement error handling to ensure that the user enters a positive integer for the age.

==================================
Input: Prompt the user to enter their age.
Processing: Classify the age into different categories:
Under 18: Minor
18-65: Adult
Above 65: Senior citizen
Output: Display the category based on the entered age.
'''

#Ask the user to input their age
age_int = input("Enter your age: ")


#Check if the input is a number and not an empty string
if age_int.isdigit():
    age = int(age_int)
    if age > 0:

        if age < 18:
            print("Minor")

        elif age >= 18 and age <= 65:
            print("Adult")

        else:
            print("Senior Citizen")
    else:
        print("Error: Age must be positive integer")

else:
    print("Age must be positive integer")