'''
Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.



==============================================

Input: Ask the user to enter an amount in one currency (e.g., USD).

Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.

Output: Display the converted amount in the target currency.
'''

USD = float(input("Enter amount of USD to convert:"))

EUR = USD*0.85

print("Amount of EUR:",EUR)
