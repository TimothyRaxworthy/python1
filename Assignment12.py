'''
Challenge: Use nested loop structures to print the pattern efficiently and neatly. Allow the user to specify the character used for the pattern.

=========================================
Description: Develop a program that prompts the user to enter the number of rows for a pattern and then prints a pattern of asterisks (*) in the form of a right triangle.
'''

#Collect the inputs from user
char = input("Enter a character: ")
rows = int(input("Enter the number of rows for a pattern: "))

#Nested loop structure for printing pattern
while True:
    if rows > 0:
        print(char*rows)
        rows = rows - 1
    else:
        break
