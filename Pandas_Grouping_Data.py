#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi',  
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'],  
        'Age':[27, 24, 22, 32,  
               33, 36, 27, 32],  
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj', 
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],  
        'Qualification':['Msc', 'MA', 'MCA', 'Phd', 
                         'B.Tech', 'B.com', 'Msc', 'MA'], 
        'Score': [23, 34, 35, 45, 47, 50, 52, 53]}


# In[3]:


df = pd.DataFrame(data1)


# In[4]:


df


# In[5]:


df.groupby('Name').groups


# In[6]:


gk = df.groupby('Name')
gk.first()


# In[7]:


df.groupby(['Name','Qualification']).groups


# In[8]:


df.groupby('Name').sum()


# In[9]:


df.groupby(['Name'] , sort=False).sum()


# In[10]:


gp = df.groupby('Name')

for name,group in gp:
    print(name)
    print(group)


# In[11]:


grp = df.groupby(['Name','Qualification'])

for name,group in grp:
    print(name)
    print(group)
    print()


# In[12]:


grp = df.groupby('Name')

grp.get_group('Princi')


# In[13]:


grp = df.groupby(['Name','Qualification'])
grp.get_group(('Abhi','MA'))


# In[14]:


grp = df.groupby('Name')
grp.aggregate(np.sum)


# In[15]:


grp = df.groupby(['Name','Qualification'])
grp.aggregate(np.sum)


# In[16]:


grp = df.groupby('Name')
grp['Age'].agg([np.sum, np.mean, np.std])


# In[17]:


grp = df.groupby('Name')
grp.agg({'Age':"sum",'Score':"std"})


# In[18]:


grp = df.groupby('Name')

sc = lambda x : (x - x.sum())/x.std()*10
grp.transform(sc)


# In[19]:


grp = df.groupby('Name')

grp.filter(lambda x : len(x)>=2)


# In[20]:


data2 = {'Team':['Arsenal', 'Manchester United', 'Arsenal', 
                   'Arsenal', 'Chelsea', 'Manchester United', 
                   'Manchester United', 'Chelsea', 'Chelsea', 'Chelsea'], 
                     
           'Player':['Ozil', 'Pogba', 'Lucas', 'Aubameyang', 
                       'Hazard', 'Mata', 'Lukaku', 'Morata',  
                                         'Giroud', 'Kante'], 
                                           
           'Goals':[5, 3, 6, 4, 9, 2, 0, 5, 2, 3] } 


# In[21]:


df2 = pd.DataFrame(data2)


# In[22]:


df2


# In[23]:


total_goals = df2['Goals'].groupby(df2['Team'])
print(total_goals.sum())


# In[24]:


Cricket= {'Team':['Australia', 'England', 'South Africa', 
                   'Australia', 'England', 'India', 'India', 
                        'South Africa', 'England', 'India'], 
                          
           'Player':['Ricky Ponting', 'Joe Root', 'Hashim Amla', 
                     'David Warner', 'Jos Buttler', 'Virat Kohli', 
                     'Rohit Sharma', 'David Miller', 'Eoin Morgan', 
                                                 'Dinesh Karthik'], 
                                                   
          'Runs':[345, 336, 689, 490, 989, 672, 560, 455, 342, 376], 
            
          'Salary':[34500, 33600, 68900, 49000, 98899, 
                    67562, 56760, 45675, 34542, 31176] }


# In[25]:


df3 = pd.DataFrame(Cricket)


# In[26]:


df3


# In[27]:


#Total_Salary = df3['Salary'].groupby(df3['Team'])
Total_Salary = df3['Runs'].groupby(df3['Team'])


# In[28]:


Total_Salary.sum()


# In[29]:


d = { 'id':['1','2','3'],
     'columns 1.1':[1,2,3],
     'columns 1.2': ['10','20','30'],
     'columns 2.1': ['5','6','7'],
     'columns 2.2': ['50','60','70']}


# In[30]:


df4=pd.DataFrame(d)
df4


# In[31]:


grp = { 'columns 1.1':'columns1',
         'columns 1.2':'columns1',
         'columns 2.1':'columns2',
         'columns 2.2':'columns2'}


# In[32]:


df4 = df4.set_index('id')


# In[33]:


df4 = df4.groupby(grp, axis=1).max()
print(df4)


# In[36]:


dict = { 
    "ID":[1, 2, 3], 
    "Movies":["The Godfather", "Fight Club", "Casablanca"], 
    "Week_1_Viewers":[30, 30, 40], 
    "Week_2_Viewers":[60, 40, 80], 
    "Week_3_Viewers":[40, 20, 20] }


# In[37]:


# Convert dictionary to dataframe 
df = pd.DataFrame(dict)
print(df)


# In[38]:


# Create the groupby_dict  
groupby_dict = {"Week_1_Viewers":"Total_Viewers", 
           "Week_2_Viewers":"Total_Viewers", 
           "Week_3_Viewers":"Total_Viewers", 
           "Movies":"Movies" } 
  
df = df.set_index('ID') 
df = df.groupby(groupby_dict, axis = 1).sum() 
print(df)


# In[ ]:




