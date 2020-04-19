#!/usr/bin/env python
# coding: utf-8

# 
# # **Assignment - 2: Basic Data Understanding**
# 
# ---
# 
# This assignment will get you familiarized with Python libraries and  functions required for data visualization.

# ---
# ## Part 1 - Loading data 
# ---

# ###Import the following libraries:  
# 
# * ```numpy``` with an alias name ```np```, 
# * ```pandas``` with an alias name ```pd```, 
# * ```matplotlib.pyplot``` with an alias name ```plt```, and 
# * ```seaborn``` with an alias name ```sns```. 

# In[ ]:


# Load the four libraries with their aliases 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


### Using the files ```train.csv``` and ```moviesData.csv```,  peform the following:

#* Load these file as ```pandas``` dataframes and store it in variables named ```df``` and ```movies``` respectively. 
#* Print the first ten rows of ```df```. 


# In[39]:


# Load the file as a dataframe 
df = pd.read_csv('train.csv')
movies= pd.read_csv('moviesData.csv')
df.head()


# In[57]:


# Print the first ten rows of df
df.iloc[0:5,0:9]



# ### Using the dataframe ```df```, perform the following: 
# 
# * Print the first five rows of the column ```MonthlyRate```. 
# * Find out the details of the column ```MonthlyRate``` like mean, maximum value, minimum value, etc. 

# In[70]:


# Print the first five rows of MonthlyRate
df["MonthlyRate"]
df.columns.get_loc("MonthlyRate")
df.iloc[0:5,18:19]
#df.describe()
#df.info


# In[75]:


# Find the details of MonthlyRate 
df.describe()


# ---
# ## Part 2 - Cleaning and manipulating data 
# ---

# ### Using the dataframe ```df```, peform the following:
# 
# * Check whether there are any missing values in ```df```. 
# * If yes, drop those values and print the size of ```df``` after dropping these. 

# In[ ]:


# Check for missing values 
df

# Drop the missing values 


# Print the size of df after dropping 


# ### Using the dataframe ```df```, peform the following:
# 
# * Add another column named ```MonthRateNew``` in ```df``` by subtracting the mean from ```MonthlyRate``` and dividing it by standard deviation. 

# In[ ]:


# Add a column named MonthRateNew 



# ### Using the dataframe ```movies```, perform the following: 
# 
# * Check whether there are any missing values in ```movies```. 
# * Find out the number of observations/rows having any of their features/columns missing. 
# * Drop the missing values and print the size of ```movies``` after dropping these. 
# * Instead of dropping the missing values, replace the missing values by their mean (or some suitable value). 
# 

# In[ ]:


# Check for missing values 

# Drop the missing values 

# Replace the missing values 
# You can use SimpleImputer of sklearn for this


# ---
# ## Part 3 - Visualizing data 
# ---

# ### Visualize the ```df``` by drawing the following plots:
# 
# * Plot a histogram of ```Age``` and find the range in which most people are there. 
# * Modify the histogram of ```Age``` by adding 30 bins. 
# * Draw a scatter plot between ```Age``` and ```Attrition``` and suitable labels to the axes. Find out whether people more than 50 years are more likely to leave the company. (```Attrition``` = 1 means people have left the company). 

# In[86]:


# Plot and modify the histogram of Age
plt.hist(df.Age)
df.Age.describe()
plt.hist(df.Age, bins = 30, color='green', orientation='vertical')
#plt.title("Distribution of movies' length")
#plt.xlabel("Run time of movies")
#plt.xlim(0,300)


# In[88]:


# Draw a scatter plot between Age and Attrition
plt.scatter(df.Age, df.Attrition, c='red')
plt.xlim(25,50) # Age varies from 25 to 50
plt.ylim(0,3) # audience varies from 0 to 100
plt.title('Scatter plot of Age and Attrition')
plt.show()


# In[89]:


# Print the first five rows of MonthlyRate
df["MonthlyRate"]
df.columns.get_loc("MonthlyRate")
df.iloc[0:5,18:19]
#df.describe()
#df.info


# ### Visualize the ```df``` by following the steps given below:
# 
# * Get a series containing counts of unique values of ```Attrition```.
# * Draw a countplot for ```Attrition``` using ```sns.countplot()```. 

# In[ ]:


# Get a series of counts of values of Attrition


# Draw a countplot for Attrition 
# You may use countplot of seaborn for this 


# ### Visualize the ```df``` by following the steps given below:
# 
# * Draw a cross tabulation of ```Attrition``` and ```BusinessTravel``` as bar charts. Find which value of ```BusinessTravel``` has highest number of people.

# In[ ]:


# Draw a cross tab of Attritiona and BusinessTravel 
# You may use crosstab of pandas for this 


# ### Visualize the ```df``` by drawing the following plot:
# 
# * Draw a stacked bar chart between ```Attrition``` and ```Gender``` columns. 

# In[ ]:


# Draw a stacked bar chart between Attrition and Gender 


# ### Visualize the ```df``` by drawing the following histogram:
# 
# * Draw a histogram of ```TotalWorkingYears``` with 30 bins. 
# * Draw a histogram of ```YearsAtCompany``` with 30 bins and find whether the values in ```YearsAtCompany``` are skewed. 

# In[90]:


# Draw a histogram of TotalWorkingYears with 30 bins
plt.hist(df.TotalWorkingYears, bins = 30, color='green', orientation='vertical')

# Draw a histogram of YearsAtCompany
plt.hist(df.YearsAtCompany, bins = 30, color='red', orientation='vertical')


# ### Visualize the ```df``` by drawing the following boxplot:
# 
# * Draw a boxplot of ```MonthlyIncome``` for each ```Department``` and report whether there is/are outlier(s). 
# 

# In[97]:


# Draw a boxplot of MonthlyIncome for each Department and report outliers 
plt.figure(figsize=(8,10))
#df['MonthlyIncome'] = movies['audience_score'] - movies['critics_score']
chart = sns.boxplot('MonthlyIncome', 'Department', data=df)
chart.set_xticklabels(
  chart.get_xticklabels(), 
    #rotation=90, 
    #horizontalalignment='right',
    #fontweight='light',
    #fontsize='x-large'
)


# ### Visualize the ```df``` by drawing the following piechart:
# 
# * Create a pie chart of the values in ```JobRole``` with suitable label and report which role has highest number of persons. 

# In[102]:


# You will need to find the counts of unique values in JobRole. 
JobRole = df.JobRole.value_counts()
print(JobRole)


# In[106]:


# Create a piechart of JobRole
plt.pie(JobRole, labels= JobRole.index.tolist())
plt.show()


# In[ ]:




