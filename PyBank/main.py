#!/usr/bin/env python
# coding: utf-8

# In[227]:


#Importing important modules
import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# In[228]:


#read the CSV using pandas
bank_data = pd.read_csv(r"C:\Users\Owner\HomeworkBankData.csv")


# In[229]:


#Turn Bank_Data into a DataFrame and objectify it.
PL_df = pd.DataFrame(data=bank_data)


# In[230]:


#Finding total months using len() function
#by calling the 'Date' column of the dataframe.

#Total_Months Function
Total_Months = len(PL_df['Date'])

#Total_Months Print Function
#print(f"Total Months: {Total_Months}")


# In[231]:


#Get the Total of Profit/Losses column from the PL_df (Profit/Losses DataFrame)

#Total_PL Function
Total_PL = PL_df['Profit/Losses'].sum()

#Total_PL Print Function
#print(f"Total: ${Total_PL}")


# In[232]:


#Isolating the Profit/Losses column by dropping the 'Date' column.
PL_alone = PL_df.drop(['Date'],axis=1)


# In[233]:


#Creating a dataframe of differentials from the Profit/Losses column
#and objectifying the column.
PL_differentials = PL_alone.diff(axis=0,periods=1)

#Dropping the NaN value from the beginning of the column
PL_differentials.dropna(subset=["Profit/Losses"], inplace=True)


# In[234]:


#Averaging the change by taking the mean of the Profit/Losses differential column
#and then objectifying it
Average_Change = round(float(PL_differentials.mean()), 2)

#Average Change Print Function
#print(f"Average Change: ${Average_Change}")


# In[235]:


#Finding the max value from the differentials dataframe.
#This represents the greatest increase in one day.
Greatest_Increase = max(PL_differentials['Profit/Losses'])


# In[236]:


#Finding the minimum value from the differentials dataframe
#This represents the greatest decrease in one day.
Greatest_Decrease = min(PL_differentials['Profit/Losses'])


# In[237]:


#Finding the index location of the greatest decrease
Index_Location_of_Greatest_Decrease = PL_differentials.idxmin()


# In[238]:


#Identifying and objectifying the month of the greatest decrease
Date_of_Greatest_Decrease = PL_df['Date'][44]

#Greatest Decrease Print Function
#print(f"Greatest Decrease in Profits: {Date_of_Greatest_Decrease} (${Greatest_Decrease})")


# In[239]:


#Finding the index location of the greatest increase
Index_Location_of_Greatest_Increase = PL_differentials.idxmax()


# In[240]:


#Identifying & objectifying the month of the greatest increase
Date_of_Greatest_Increase = PL_df['Date'][25]

#Greatest Increase Print Function
#print(f"Greatest Increase in Profits: {Date_of_Greatest_Increase} (${Greatest_Increase})")


# In[251]:


#Print Statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total_PL}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profits: {Date_of_Greatest_Increase} (${Greatest_Increase})")
print(f"Greatest Decrease in Profits: {Date_of_Greatest_Decrease} (${Greatest_Decrease})")


# In[268]:


#Writing the Financial Analysis onto a text file and exporting it.
text_file = open('Financial_AnalysisSRF.txt','w')
text_file.write(f"Financial Analysis\n----------------------------\nTotal Months: {Total_Months}\nTotal: ${Total_PL}\nAverage Change: ${Average_Change}\nGreatest Increase in Profits: {Date_of_Greatest_Increase} (${Greatest_Increase})\nGreatest Decrease in Profits: {Date_of_Greatest_Decrease} (${Greatest_Decrease})")
text_file.close()


# In[242]:


#Index of Objects/Variables 
#-----------------------------------------------------
#Total months = Total_Months
#Total Profit/Losses = Total_PL
#Average change = Average_Change
#Date of greatest increase = Date_of_Greatest_Increase
#Date of greatest decrease = Date_of_Greatest_Decrease
#Greatest increase in profits = Greatest_Increase
#Greatest decrease in profits = Greatest_Decrease


# In[ ]:




