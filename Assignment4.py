'''
Challenge: Implement error handling to ensure that the user enters numeric values for the coordinates.

============================================
Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
Processing: Calculate the distance between the two points using the distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
Output: Display the calculated distance between the two points.
'''
# Libraries
import math

# Submit the coordinates for the 2d plane
x1 = float(input("Enter x coordinate: "))
y1 = float(input("Enter y coordinate: "))
x2 = float(input("Enter x coordinate: "))
y2 = float(input("Enter y coordinate: "))

# Calculate the distance
#distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

distance_squared = (x2 - x1)**2 + (y2 - y1)**2
distance = distance_squared ** 0.5

# Display the calculated distance
print("The distance is:", distance)