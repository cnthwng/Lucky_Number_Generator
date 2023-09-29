# Lucky Number Generator

# """
# This function returns a list of random numbers based on a range (x,y) and total numbers to generate (z) specified from the user.
# The total numbers to generate must be less then, or equal to the range inputted by the user.
# """


import random

def lucky_numbers(x,y,z):
    # Examples 
    # lucky_numbers(1,49,6) example of Lotto 649 draw
    # [37, 9, 26, 12, 42, 24]
    
    # lucky_numbers(1,50,8) Example of Lotto Max Combination draw
    # [17, 50, 34, 38, 16, 8, 49, 45]
    
    return random.sample(range(x,y+1), z)


first_num = int(input("Please provide the 1st number of your range: "))
last_num = int(input("Please provide the last number of your range: "))
total_num = int(input("Please provide the amount of numbers you'd like: "))

print(first_num, last_num, total_num))
