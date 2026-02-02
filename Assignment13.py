'''
Challenge: Use a loop structure to compare characters from both ends of the string to determine whether it is a palindrome.

===================================
Description: Write a program that prompts the user to enter a string and then checks whether it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
'''

#Collect string input from user
string = input("Enter a word: ")
characters = [char for char in string]
print(characters)

#Reverse the order of the string and print it
reversed_characters = characters[::-1]
print(reversed_characters)

#Check if they match
if characters == reversed_characters:
    print("This is a palindrome!")
else:
    print("Not a palindrome!")


