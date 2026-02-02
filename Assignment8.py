'''
Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.


=================================================

Input: Ask the user to enter their marks for three subjects.

Processing: Calculate the average of the marks. Determine the grade based on the average:

90 and above: A
80-89: B
70-79: C
60-69: D
Below 60: F
Output: Display the calculated grade.
'''

#Ask the user to enter each grade

mark1 = int(input("Please enter your first mark: "))
if mark1 >= 0 and mark1 < 101:
        mark2 = int(input("Please enter your second mark: "))
else:
        print("Please enter a number between 0 and 100")
if mark2 >= 0 and mark2 < 101:
    mark3 = int(input("Please enter your third mark: "))
else:
                print("Please enter a valid value")
if mark3 >= 0 and mark3 < 101:
    average = (mark1 + mark2 + mark3) / 3
    print("The average is:", average)
else:
    print("Please enter a number between 0 and 100")

if average >= 90:
    print("A")
elif average >= 80:
    print("B")
elif average >= 70:
    print("C")
elif average >= 60:
    print("D")
else:
    print("F")

