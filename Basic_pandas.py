#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd

A=pd.DataFrame({'A':[1,2,3,4,5]})
B=pd.DataFrame({'B':[6,8,9,7,12]})


# In[37]:


A_new = A['A'].apply(str)


# In[38]:


B_new = B['B'].apply(str)


# In[39]:


df = pd.concat([A_new,B_new],1)


# In[41]:


df


# In[32]:





# In[ ]:





# In[ ]:





# In[ ]:




