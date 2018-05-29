# Store the file path associated with the file (note the backslash may be OS specific)

import csv
import os


#csvpath = os.path.join('budget_data_1.csv')
csvpath = os.path.join("raw_data","budget_data_2.csv")
#file = 'budget_data_1.csv'
sum=0.00
sumrevchange = 0.00
cnt=0
revchngcnt=0
avgrevchange=0.00
revchange=0
maxrev_increase=0.00
maxrev_decrease=0.00
currev=0
prevrev=0

outfile="budget_out2.txt"



# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(csvpath, newline='')  as budgetcsv:
    # CSV reader specifies delimiter and variable that holds contents
    #csvreader = csv.csvreader(budgetcsv, delimiter=',')
    csvreader = csv.DictReader(budgetcsv, delimiter=',')
    ## Perform counts and totals for each row in the dict.
    for row in csvreader:
        #print(row["Revenue"])
        cnt=cnt+1
        currev=float(row["Revenue"])
        currdate=row["Date"]
        sum = sum + currev
        
        #calculate revenue change for each month and capture max, min values. 
        if cnt > 1: 
            revchange = currev - prevrev
            sumrevchange = sumrevchange + revchange
            revchngcnt =  revchngcnt + 1  
            #print(str(revchange))
        if revchange >= 0:
            if revchange > maxrev_increase :
                maxrev_increase = revchange
                maxrev_inc_date = currdate
                
        elif revchange < 0:
            if revchange < maxrev_decrease:
                maxrev_decrease = revchange
                maxrev_dec_date = currdate
                
        #print("max" + str(maxrev_increase)) 
        #print("min" + str(maxrev_decrease))  
        #store the current rev in to the hold area for use.
        prevrev=currev    
    
    #calculate average of revenuechange
    avgrevchange = sumrevchange / revchngcnt
    
    print(" ")
    print("Financial Analysis")
    print("-"*50)
    print("Total months  : " + str(cnt))
    print("Total Revenue : " + str(sum))
    print("Average Revenue Change $" + str(avgrevchange))
    print("Greatest Increase in Revenue: " + maxrev_inc_date + " ($" +
              str(maxrev_increase) +")" )
    print("Greatest Decrease in Revenue: " + maxrev_dec_date + " ($" +
              str(maxrev_decrease) +")" )
    print(" ")
    
    with  open(outfile,'w')  as fhout:
        print("Financial Analysis", file=fhout,end='\n')
        print("----------------------------------------", file=fhout,end='\n')
        print("Total months  : " + str(cnt), file=fhout,end='\n')
        print("Total Revenue : " + str(sum), file=fhout,end='\n')
        print("Average Revenue Change $" + str(avgrevchange),file=fhout,end='\n')
        print("Greatest Increase in Revenue: " + maxrev_inc_date + " ($" +
              str(maxrev_increase) +")", file=fhout,end='\n' )
        print("Greatest Decrease in Revenue: " + maxrev_dec_date + " ($" +
              str(maxrev_decrease) +")", file=fhout,end='\n' )
        
        #print("End of file ",file=fhout,end='\n')
        
        #fhout.write("Financial Analysis")
        #fhout.write("------------------------------------")
        #fhout.write("Total months  : " + str(cnt) + "\n")
        #fhout.write("Total Revenue : " + str(sum))
        #fhout.write("Average Revenue Change $" + str(avgrevchange))
        #fhout.write("Greatest Increase in Revenue: " + maxrev_inc_date + " ($" +
        #      str(maxrev_increase) +")")
        #fhout.write("Greatest Decrease in Revenue: " + maxrev_dec_date + " ($" +
        #      str(maxrev_decrease) +")" )
        
