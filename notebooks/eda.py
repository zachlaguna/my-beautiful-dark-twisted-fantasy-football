#!/usr/bin/env python
# coding: utf-8

# # Explore & Clean the Data

# In[1]:


import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


pd.options.display.max_columns = None


# In[3]:


df = pd.read_csv('../data/raw/pbp-2018.csv')


# In[4]:


display(df.head())


# In[5]:


df.dtypes


# In[6]:


df.describe()


# Remove non-plays

# In[7]:


df = df[df['IsNoPlay']==0]
df.drop(columns=['IsNoPlay'], inplace=True)


# In[8]:


df.describe()


# Check out the distribution of Yards To-Go on 2nd down by team.

# In[9]:


df2 = df[df['Down']==2]


# In[10]:


fig, ax = plt.subplots(figsize=(20,10))
# sns.boxplot(x='OffenseTeam',y='ToGo',data=df2,ax=ax)
sns.violinplot(x='OffenseTeam',y='ToGo',data=df2.sort_values(by=['OffenseTeam']),ax=ax)
plt.show()


# In[ ]:




