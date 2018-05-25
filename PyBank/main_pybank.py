# Store the file path associated with the file (note the backslash may be OS specific)
#file = '../Resources/input.txt'
import csv
import os


csvpath = os.path.join('budget_data_1.csv')
#file = 'budget_data_1.csv'
sum=0.0
sumrevchange = 0.0
cnt=0
revchngcnt=0
avgrevchange=0
revchange=0
maxrev_increase=0
maxrev_decrease=0
currev=0
prevrev=0
newdict=dict()



# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(csvpath, newline='')  as budgetcsv:
    # CSV reader specifies delimiter and variable that holds contents
    #csvreader = csv.csvreader(budgetcsv, delimiter=',')
    csvreader = csv.DictReader(budgetcsv, delimiter=',')
    ## Perform counts and totals for each row in the dict.
    for row in csvreader:
        #print(row["Revenue"])
        
        currev=float(row["Revenue"])
        sum = sum + currev
        cnt=cnt+1
        if cnt > 1: 
            revchange = currev - prevrev
            sumrevchange = sumrevchange + 1
            revchngcnt =  revchngcnt + 1  
        print(str(revchange))
        #store the current rev in to the hold area for use.
        prevrev=currev    
    
    
    print("Financial Analysis")
    print("------------------------------------")
    print("Total months  : " + str(cnt))
    print("Total Revenue : " + str(sum))
    
## Create a dict that also contains the change in revenue for each mnth.