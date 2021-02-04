#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


import warnings
warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_excel(r'C:\Users\rajes\OneDrive\Desktop\Task 2 eda\data.xlsx')


# In[3]:


df.head(2)


# In[4]:


df.drop(columns=(['Unnamed: 0','ID']),axis=1,inplace=True)


# In[5]:


df.head(2)


# In[6]:


df.info()


# In[7]:


df.DOL.unique()


# In[8]:


df["DOL"].replace({"present": "2021"}, inplace=True)
df['DOL']=pd.to_datetime(df['DOL'])


# In[9]:


df.info()


# In[10]:


categorical_col = []
numarical_cols = []
date_time = []
for x in df.columns:
    if df[x].dtype == 'object':
        categorical_col.append(x)
    elif df[x].dtype == 'datetime64[ns]':
        date_time.append(x)
    else:
        numarical_cols.append(x)


# # Uni Variate Analysys

# ### Categorical Variables

# In[11]:


categorical_col


# In[12]:


a = 3  # number of rows
b = 3  # number of columns
c = 1  # initialize plot counter

fig = plt.figure(figsize=(40,30))

for i in categorical_col:
    plt.subplot(a, b, c)
    plt.title('countplot :'+'{}'.format(i))
    plt.xlabel(i)
    sns.countplot(df[i].dropna(), order = df[i].value_counts().iloc[:10].index)
    c = c + 1

plt.show()


# ## DateTIme

# In[13]:


date_time


# In[14]:


a = 3  # number of rows
b = 1 # number of columns
c = 1  # initialize plot counter

fig = plt.figure(figsize=(20,20))

for i in date_time:
    plt.subplot(a, b, c)
    plt.title('countplot :'+'{}'.format(i))
    plt.xlabel(i)
    sns.countplot(df[i].dropna(), order = df[i].value_counts().iloc[:10].index)
    c = c + 1

plt.show()


# ### Numaic Variables

# In[15]:


numarical_cols


# ### Histogram

# In[16]:


a = 13  # number of rows
b = 2 # number of columns
c = 1  # initialize plot counter


fig = plt.figure(figsize=(50,30))

for i in numarical_cols:
    
    plt.subplot(a, b, c)
    plt.title('Histogram :'+'{}'.format(i))
    plt.xlabel(i)
    plt.ylabel('count')
    plt.hist(df[i].dropna(),bins=50,color = 'green')
    c += 1
plt.tight_layout(pad=4.0)    
plt.show()


# ### boxplot

# In[17]:


a = 13  # number of rows
b = 2 # number of columns
c = 1  # initialize plot counter

fig = plt.figure(figsize=(50,30))

for i in numarical_cols:
    plt.subplot(a, b, c)
    df[[i]].boxplot()
    plt.title('BoxPlot :'+'{}'.format(i))
    plt.ylabel('count')
    c += 1
plt.tight_layout(pad=4.0)
plt.show()


# In[ ]:





# # Bi-Variate Analysis

# ## Numerical vs Numerical variables

# In[18]:


for i in numarical_cols:
    for j in numarical_cols:
        df.plot.scatter(i,j)
        df[i].corr(df[j])
        


# In[ ]:





# ### Categorical vs Categorical

# In[19]:


# Using catplot to compare categorical data with numerical data
sns.catplot(x="Gender",y="Salary",kind="point",data=df)
plt.show()

sns.catplot(x="Gender",y="Salary",kind="swarm",data=df)
plt.show()

sns.catplot(x="Gender",y="Salary",kind="strip",data=df)
plt.show()

sns.catplot(x="Gender",y="Salary",kind="box",data=df)
plt.show()


# ### Categorical vs Numerical 

# In[23]:


sns.pairplot(df)
plt.show()


# In[22]:


df.columns


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




