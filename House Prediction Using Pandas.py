#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv("House Price Prediction - Test Data.csv")
data


# In[3]:


data=pd.read_csv("House Price Prediction - Test Data.csv",nrows=12)
data
print(type(data))


# In[4]:


data=pd.read_csv("House Price Prediction - Test Data.csv",usecols=['bedrooms'])
data


# In[5]:


data=pd.read_csv("House Price Prediction - Test Data.csv",usecols=['date'])
data


# In[6]:


data=pd.read_csv("House Price Prediction - Test Data.csv",usecols=['id'])
data


# In[7]:


data=pd.read_csv("House Price Prediction - Test Data.csv",usecols=['bedrooms','date','id','floors'])
data


# In[8]:


data=pd.read_csv("House Price Prediction - Test Data.csv",skiprows=[1])
data


# In[9]:


data=pd.read_csv("House Price Prediction - Test Data.csv",skiprows=[1,6])
data


# In[10]:


data=pd.read_csv("House Price Prediction - Test Data.csv",index_col=['date'])
data


# In[11]:


data=pd.read_csv("House Price Prediction - Test Data.csv",header=2)
data


# In[12]:


data=pd.read_csv("House Price Prediction - Test Data.csv",names=['col1','col2','col3','col4'])
data


# In[13]:


data=pd.read_csv("House Price Prediction - Test Data.csv",header=None, prefix=['col'])
data


# In[14]:


data=pd.read_csv("House Price Prediction - Test Data.csv",header=None, prefix=['col'],dtype={})
data


# In[15]:


data=pd.read_csv("House Price Prediction - Test Data.csv",dtype={"floors":"float"})
data


# In[16]:


data.index


# In[17]:


data.columns


# In[18]:


data.describe()


# In[19]:


data.head(3)


# In[20]:


data.tail(2)


# In[21]:


data.info(6)


# In[22]:


data.index.array


# In[23]:


data.to_numpy()


# In[24]:


print(type(data))


# In[25]:


import numpy as np
v=np.asarray(data)
print(v)


# In[26]:


data.sort_index(axis=0, ascending=False)


# In[27]:


data.loc[0,"id"]="Python Code"
data


# In[28]:


data.loc[[7,8],["bedrooms","bathrooms"]]


# In[29]:


data.loc[:,["bedrooms","bathrooms"]]


# In[30]:


import pandas as pd
data2=pd.read_csv("random.data.csv")
data2


# In[31]:


data2.isnull().sum()


# In[32]:


data2.isnull().any()


# In[33]:


data2.isnull().mean()


# In[34]:


df_clean=data2.dropna()
data2


# In[35]:


df_filled=data2.fillna(0)
df_filled


# In[36]:


df_clean


# In[37]:


data2


# In[38]:


data2.dropna(subset=["City"])


# In[39]:


data2.fillna({"Name":"Python","Age":"Mustafa"})


# In[40]:


data2.fillna(method="ffill") #forward filling


# In[41]:


data2.fillna(method="bfill") #backward filling


# In[42]:


x=[2,3,4,5,6]
var=pd.Series(x,index=['a','b','c','d','e'],dtype="float")
print(var)
print(type(var))


# In[43]:


dic={"Name":["Python","Java","C++","R"],"Rank":[1,2,4,3]}
var1=pd.Series(dic)
var1


# In[44]:


D={"A":[1,2,3,4,5],"B":[1,2,3,4,5],"C":[1,2,3,4,5]}
var1=pd.DataFrame(D, columns=["A"],index=['a','b','c','d','e'])
print(var1)


# In[45]:


sr={"S":pd.Series([1,2,3,4]),"P":pd.Series([1,2,3,4])}
var3=pd.DataFrame(sr)
var3
print(type(var3))
print(var3)


# In[46]:


var=pd.DataFrame({"A":[1,2,3,4,5],"B":[6,7,8,9,10]})
var
var["C"]=var["A"]+var["B"]
var


# In[47]:


data2.replace(to_replace="Delhi", value="Hamza")

