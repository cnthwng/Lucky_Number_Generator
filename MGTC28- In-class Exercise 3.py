#!/usr/bin/env python
# coding: utf-8

# # Lucky Number Generator

# """
# This program will generate a list of six different random lucky numbers ranging from 1 to 49, to simulate the weekly draw of numbers for Lotto 649.
# User will run the program by calling the function defined below in order to generate the six random values. 
# """

# In[1]:


import random # Random library imported as its functions are required to generate a list of random numbers.


# In[9]:


def six_lucky_numbers(): # Defined a function to return a list of 6 random numbers.
    return random.sample(range(1, 50), 6) # The function will return 6 numbers from numbers 1-49.


# In[ ]:


# Examples of output when program is run.


# In[10]:


six_lucky_numbers() # To generate the list of 6 numbers, user will call the function six_lucky_numbers(). No input required.


# In[11]:


six_lucky_numbers()


# In[14]:


six_lucky_numbers()


# In[15]:


six_lucky_numbers()

