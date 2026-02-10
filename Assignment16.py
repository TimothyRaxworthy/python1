'''
Challenge: Optimize the function to handle large input numbers efficiently.



=====================================================

Description: Develop a function called is_prime that takes a positive integer as input and returns True if it is a prime number, and False otherwise.
'''

#Def function
def is_prime():
    #collect input from user
    n = int(input("Enter a positive integer: "))

    #check if the number is a prime number
    if n < 2:
        print("False")
    else:
        prime = True
        for i in range(2, int(n**1/2) + 1):
            if n % i == 0:
                prime = False
                break

        if prime:
            print("True")
        else:
            print("False")
is_prime()
