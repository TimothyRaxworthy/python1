'''
Challenge: Write the function using recursion.

===================================
Description: Create a function named is_palindrome that takes a string as input and returns True if it is a palindrome, and False otherwise.
'''

def is_palindrome():
    string = input("Enter a word: ")
    characters = [char for char in string]
    print(characters)

    # Reverse the order of the string and print it
    reversed_characters = characters[::-1]
    print(reversed_characters)

    # Check if they match
    if characters == reversed_characters:
        print("True")
    else:
        print("False")

    return

is_palindrome()