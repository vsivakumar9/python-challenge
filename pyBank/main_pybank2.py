# Store the file path associated with the file (note the backslash may be OS specific)
#file = '../Resources/input.txt'
#import csv
#import os
import pandas as pd


#csvpath = os.path.join("raw_data",'budget_data_1.csv')
#file = 'budget_data_1.csv'
#totmonths=0
sumrev=0
cnt=0
avgrevchange=0
revchange=0
maxrev_increase=0
maxrev_decrease=0
currev=0
prevrev=0
newdict=dict()

    
# set file path
filepath = "raw_data/budget_data_1.csv"

#read csv data file with the pandas lib
budgetcsv_df = pd.read_csv(filepath)

print(budgetcsv_df.head())

#print(str(len(budgetcsv_df)))

#Number of months = length of the dataframe for a column.
totmonths = len(budgetcsv_df["Date"])

#Calc sum of Revenue.
sumrev = budgetcsv_df["Revenue"].sum()

#create another column with each of the Revenue rows shifted by 1.
budgetcsv_df["Revshift"] = budgetcsv_df["Revenue"].shift(1)

#change in rev is the diff between orig Revenue and shifted Revenue.
budgetcsv_df["Revchange"] = budgetcsv_df["Revenue"] - budgetcsv_df["Revshift"]
#print(str(totmonths))
#print(str(sumrev))
print(budgetcsv_df.head())
#print(budgetcsv_df.tail())

avgRevchange = budgetcsv_df["Revchange"].mean()
maxRevchange = budgetcsv_df["Revchange"].max()
minRevchange = budgetcsv_df["Revchange"].min()
print(str(avgRevchange))
print(str(maxRevchange))
print(str(minRevchange))

maxRevloc = budgetcsv_df.loc[budgetcsv_df["Revchange"] == maxRevchange]
minRevloc = budgetcsv_df.loc[budgetcsv_df["Revchange"] == minRevchange]
print(maxRevloc["Date"])
print(minRevloc["Date"])

print(maxRevloc)
print(minRevloc)


## Create a dict that also contains the change in revenue for each mnth.