#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range (1,6):
    for j in range (1,6):
        if j<=i:
         print ('*',end="")
        else:
         print("",end="")
    print()
for i in range (6,10):
    for j in range (10-i):
         print ("*", end="")
    print()  


# In[11]:


def reverse(string):
    reversed_string=""
    for i in string:
        reversed_string=i+reversed_string
    print("the reversed string is", reversed_string)
string=input("Enter a string")
reverse(string)


# In[ ]:




