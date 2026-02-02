'''
Challenge: Provide feedback to the user based on their BMI category (e.g., underweight, normal weight, overweight, obese).

===============================
Input: Prompt the user to enter their weight in kilograms and height in meters.
Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
Output: Display the calculated BMI.
'''

# The input section is being solved below
# We are creating two inputs to solve this assignment

weight = float(input("Enter the weight in kilograms: "))
height = float(input("Enter the height in meters: "))

# The processing section and calculations are being addressed below
bmi = weight / (height ** 2)

#This is the output below
print("The BMI is:", bmi)
