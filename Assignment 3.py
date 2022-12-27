#!/usr/bin/env python
# coding: utf-8

#  Write a Python function to sum all the numbers in a list.
# 
# 
# 
# Sample List : (8, 2, 3, 0, 7)
# 
# Expected Output : 20

# In[10]:


def sum(numbers):

   total = 0

   for x in numbers:

       total += x

   return total

print(sum((8, 2, 3, 0, 7)))


# In[11]:


def add(a,b,c,d,e):
 return a+b+c+d+e
print(add(8,2,3,0,7))


# Write a Python program to reverse a string.
# 
# 
# 
# ﻿Sample String : "1234abcd"
# 
# Expected Output : "dcba4321"

# In[12]:


def my_function(x):
  return x[::-1]

str = my_function("1234abcd")

print(str)


# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# 
# 
# 
# ﻿Sample String : 'The quick Brow Fox'
# 
# Expected Output :
# 
# No. of Upper case characters : 3
# 
# No. of Lower case Characters : 12

# In[13]:


def up_low(s):      
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print( "No. of Upper case characters : %s         No. of Lower case characters : %s" % (u,l))

up_low("The quick Brow Fox")


# In[ ]:





# In[ ]:




