#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
print('Hello User!!!..')
n=True
while n:
    length=input('Enter Your Password Length to continue or type stop to hold this program :')
    if length!='stop':
        length=int(length)
        upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower= upper.casefold()
        numbers='1234567890'
        symbols='!@#%^&(){}[]:;""''<>,.?\|~`+-*/'
        P=upper+lower+numbers+symbols
        temp=random.sample(P,length)
        Password="".join(temp)
        print(Password)
    else:
        n=False
        break
        



# In[ ]:




