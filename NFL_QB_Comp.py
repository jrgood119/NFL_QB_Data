#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[16]:


#Importing data
df = pd.read_excel('/Users/jtgood/Desktop/NFL_QB/Excel_Data/QB_Data.xlsx', sheet_name = 'QB')


# In[17]:


df.head()


# In[18]:


#Filtering out data that I do not need, using only points with over 250 passes thrown
needed_data = df[['Att', 'C_Att', 'Comp_Per', 'C_Comp_Per']]
over_250 = needed_data[needed_data['Att']>250]
over_250_c = over_250[over_250['C_Att']>250]


# In[19]:


#Verifying data shape is correct
over_250_c.shape


# In[20]:


#scatter test to make sure data can be plotted
over_250_c.plot(kind='scatter', x='C_Comp_Per', y='Comp_Per')


# In[21]:


#NFL completion percentage average
over_250_c["Comp_Per"].mean()


# In[22]:


#College completion percentage average
over_250_c["C_Comp_Per"].mean()


# In[23]:


#Plotting findings with quadrant analysis
plt.figure(figsize=(6,4))
sns.scatterplot(data=over_250_c, x='C_Comp_Per', y='Comp_Per')
plt.title(f"College and Pro Completion Percentage W/ > 250 Passes Thrown")
plt.xlabel('College Comp Percentage')
plt.ylabel('Pro Comp Percentage')
plt.axhline(y=over_250_c.Comp_Per.mean(), color='k', linestyle='--', linewidth=1)           
plt.axvline(x=over_250_c.C_Comp_Per.mean(), color='k',linestyle='--', linewidth=1) 

plt.show()


# In[24]:


#Observing r squared
x = over_250_c.C_Comp_Per
y = over_250_c.Comp_Per
correlation_matrix = np.corrcoef(x, y)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2
print(r_squared)


# In[25]:


#Running to find out number of players with above nfl above college comp per
over_250_c[(over_250_c.Comp_Per >= 0.596858653615332) & (over_250_c.C_Comp_Per >=0.6135248499937287)].count() 


# In[26]:


#above nfl below college
over_250_c[(over_250_c.Comp_Per >= 0.596858653615332) & (over_250_c.C_Comp_Per <0.6135248499937287)].count() 


# In[27]:


#below nfl above college
over_250_c[(over_250_c.Comp_Per < 0.596858653615332) & (over_250_c.C_Comp_Per >=0.6135248499937287)].count() 


# In[28]:


#below and below
over_250_c[(over_250_c.Comp_Per < 0.596858653615332) & (over_250_c.C_Comp_Per < 0.6135248499937287)].count() 

