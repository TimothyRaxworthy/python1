
'''
Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.

=======================================================
Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds.
'''

hours = float(input("Enter the number of hours: "))
minutes = hours*60
seconds = minutes*60

print(minutes, seconds)