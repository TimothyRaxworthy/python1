'''
Challenge: Ensure that the user enters only a single character and handle cases where the input is not a letter.

=====================================================
Input: Ask the user to enter a single character.
Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
Output: Display whether the entered character is a vowel or a consonant.
'''

char_input = input("Enter one character:")

# If the user entered exactly one character and that it is a letter
if len(char_input) == 1 and char_input.isalpha():
    char = char_input.lower()

    # check if the character is a vowel
    if char in 'aeiou':
        print("Its a vowel")
    else:
        print("Its a consonant")

else:

    if len(char_input) != 1:
        print("Error: Please enter one character")
    else:
        print("Error: the input is not a letter")
