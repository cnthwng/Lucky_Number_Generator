#!/usr/bin/env python
# coding: utf-8

# # Lucky Number Generator

# """
# This function returns a list of random numbers based on a range (x,y) and total numbers to generate (z) specified from the user.
# The total numbers to generate must be less then, or equal to the range inputted by the user.
# """

# In[2]:


import random


# In[3]:


def lucky_numbers(x,y,z):
    return random.sample(range(x,y+1), z)


# In[4]:


# Running test cases of the lucky_numbers function created above.


# In[5]:


# lucky_numbers(1,49,6) Example of Lotto 649 draw
# >>> [37, 9, 26, 12, 42, 24]


# In[6]:


# lucky_numbers(1,50,8) Example of Lotto Max Combination draw
# >>> [17, 50, 34, 38, 16, 8, 49, 45]

