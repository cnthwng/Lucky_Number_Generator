# Lucky Number Generator

"""
This program will generate a list of six random lucky numbers ranging from 1 to 49, to simulate the weekly draw of numbers for Lotto 649.
The user will run the program by calling the function defined below in order to generate the six random values. 
"""


import random #Random library imported as its functions are required to generate a list of random numbers.



def six_lucky_numbers(): # Defined a function to return a list of six random numbers.
    return random.sample(range(1, 50), 6) # The function will return six numbers from numbers 1-49.


print(six_lucky_numbers()) # Prints a list of 6 numbers when the user runs this script. 



