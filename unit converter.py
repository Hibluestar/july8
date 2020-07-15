#!/usr/bin/env python
# coding: utf-8

# In[15]:


def convert(I):
    C=2.54*I
    print(I,'inches=',C,'cm')


# In[16]:


convert(64)


# In[17]:


convert(34)


# In[28]:


def weightconvert(p):
    k=float(p/(2.205))
    print(p,'pounds=',k,'kgs')


# In[29]:


weightconvert(9)


# In[30]:


weightconvert(290)


# In[33]:


def tempconvert(c):
    f=(c*9/5)+32
    print(c,'Celsius=',f,'Fahrenheit')


# In[34]:


tempconvert(90)


# In[35]:


tempconvert(199)


# In[ ]:




