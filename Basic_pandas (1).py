#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Importing pandas and creating dataframe 

import pandas as pd

# Column A consists of String elements and column B is filled with integers
df=pd.DataFrame({'A':['One','Two','Three','Four','Five'],
               'B':[1,2,3,4,5]})


# In[36]:


# Converting all elements in column B from Int type to String (updating, NOT creating a new column)

df['B']=df['B'].astype(str)


# In[38]:


# Checking whether we got it right by picking an arbitrary element from cloumn B

type(df['B'][1])


# In[41]:


# Creating a new column called 'Joined', which includes the elements from both columns 

df['joined'] = df['A'].str.cat(df['B'], sep = ' , ')


# In[42]:


# Next step would be to remove columns A and B

df


# In[ ]:




