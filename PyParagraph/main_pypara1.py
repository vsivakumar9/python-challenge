# -*- coding: utf-8 -*-
"""
Created on Sat May  19 13:18:49 2018

@author: Shiva
""" 
#Program reads thru a text file to obtain statistics like approx word count, 
#sentence count, average letter count per word, average sentence length etc.

import os
import re

#filepath = os.path.join("raw_data","paragraph_1.txt")
#outfile = ("pypara_result.txt")

#filepath = os.path.join("raw_data","paragraph_2.txt")
filepath = os.path.join("raw_data","paragraph_1.txt")
outfile = ("pypara_result1.txt")


# Use paragraph_1.txt as the file name
#fname = input("Enter file name: ")
fname=filepath
if len(fname) < 1 :
    fname = filepath
    print(fname)
try :
    fh = open(fname)
except:
    print ('invalid file name or path: ',fname)
    quit()

linelist=list()
periods=list()
periodlist=list()
#dict to count word frequency
#countsdict=dict()
sentcnt = 0
#wordcnt = 0
linecnt=0
totwordcnt = 0
totletlength = 0
# average letter length.
avgletcnt = 0.0
#average sentence length.
avgsentlength = 0.0

#loop thru the lines in the paragraph being read. 
for line in fh:
    #print(line)
    linecnt += 1
    #print("linecnt : " + str(linecnt))
    # split line into words and store in array linewrods.
    line=line.strip('\n')
    linelist.append(line)
    #print(linelist)
    #Find words with periods using regex to determine number of sentences.
    #periods = re.findall('(\S*["."])',line)
    #periods = re.findall('[A-Z][^.]*(\S+?[.])',line)
    periods = re.findall('[A-Z].*\s(\S+[.])',line)
    #print(periods)
    #split sentence to words for other stats like letter cnt and word cnt.
    linewords = line.split(" ")
    #print(linewords)

    if len(linewords) >= 2 :
        #append word with the period to a list to determine # of sentences.
        periodlist.append(periods)
        #add number of sentences to total.
        sentcnt = sentcnt + len(periods)
        totwordcnt = totwordcnt + len(linewords)
        
        #count letters in each word.
        # loop thru word array to determine required counts. 
        for word in linewords :
            letlength = len(word)
            totletlength = totletlength + letlength
            
    #print(periodlist)
    #print("totwordcnt   : " + str(totwordcnt) )
    #print("sentcnt      : " + str(sentcnt) )
    #print("totletlength : " + str(totletlength))
#calc avg sentence length(total # of words / total # of sentences.
avgsentlength = totwordcnt / sentcnt

#average letter count in word(Total # of letters / Total # of words in para )
avgletcnt = totletlength / totwordcnt
    
        
    #sentences = line.split(".")
    #print(sentences)

#close file handle
fh.close()


#Print final tallies
print(" ")
print("Approximate Word Count     : " + str(totwordcnt) )
print("Approximate Sentence  Count: " + str(sentcnt) )
#print("Average Letter Count       : " + str(avgletcnt) )
print("Average Letter Count       : " + "%.2f" % avgletcnt)
print("Average Sentence Length    : " + "%.2f" % avgsentlength)

with  open(outfile,'w')  as fhout:
        print("Paragraph Analysis", file=fhout,end='\n')
        print("----------------------------------------", file=fhout,end='\n')
        print("Approximate Word Count     : " + str(totwordcnt), 
              file=fhout,end='\n')
        print("Approximate Sentence  Count: " + str(sentcnt), 
              file=fhout,end='\n')
        print("Average Letter Count       : " + "%.2f" % avgletcnt,
              file=fhout,end='\n')
        print("Average Sentence Length    : " + "%.2f" % avgsentlength,
              file=fhout,end='\n')
        