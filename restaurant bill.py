#!/usr/bin/env python
# coding: utf-8

# In[2]:


num=int(input('How much is the dinner?'))
taxrate=float(input('What is your state sale tax rate?'))
tiprate=float(input('What pecentile do you want to pay tax?'))
tax=num*taxrate/100
tip=num*tiprate/100
cost=int(num+tax+tip)
print('The total cost is',cost,'.')
head=int(input('How many people are going to share the bill?'))
share=cost/head
print('Every one has to pay',share,'.')


# In[ ]:




