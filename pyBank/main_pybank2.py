# Store the file path associated with the file (note the backslash may be OS specific)
#file = '../Resources/input.txt'
#import csv
#import os
import pandas as pd


#csvpath = os.path.join("raw_data",'budget_data_1.csv')
#file = 'budget_data_1.csv'
#totmonths=0
    
# set file path
filepath = "raw_data/budget_data_1.csv"

#read csv data file with the pandas lib
budgetcsv_df = pd.read_csv(filepath)

#print(budgetcsv_df.head())

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
#print(budgetcsv_df.head())
#print(budgetcsv_df.tail())

avgRevchange = budgetcsv_df["Revchange"].mean()
maxRevchange = budgetcsv_df["Revchange"].max()
minRevchange = budgetcsv_df["Revchange"].min()

avgrevdisp = str(avgRevchange)
maxrevdisp = str(maxRevchange)
#print(avgrevdisp)
print(maxRevchange)
print(str(minRevchange))

maxRevloc = budgetcsv_df.loc[budgetcsv_df["Revchange"] == maxRevchange]
minRevloc = budgetcsv_df.loc[budgetcsv_df["Revchange"] == minRevchange]
maxReviloc = budgetcsv_df.iloc[budgetcsv_df["Revchange"] == maxRevchange]
minReviloc = budgetcsv_df.iloc[budgetcsv_df["Revchange"] == minRevchange]
print(str(maxRevloc))
print(str(maxReviloc))
print(str(minRevloc))
print(str(minReviloc))

#print(maxRevloc)
#print(minRevloc)

print("Financial Analysis")
print("-"*30)
print("Total months             : "  + str(totmonths))
print("Total Revenue            : $" + str(sumrev))
print("Average Revenue Change   : $" + str(avgRevchange))
print(f"Greatest Increase in Revenue: "+str(maxRevloc["Date"])+" ($"+ str(maxRevchange) + ")")
print(f"Greatest Decrease in Revenue: "+str(minRevloc["Date"])+" ($"+ str(minRevchange) + ")")



