# -*- coding: utf-8 -*-
"""
Created on Sat May  19 13:18:49 2018

@author: Shiva
""" 
#Program reads thru a text file to obtain statistics like approx word count, 
#sentence count, average letter count per word, average sentence length etc.

import os
import re

filepath = os.path.join("raw_data","paragraph_1.txt")
outfile = ("pypara_result.txt")

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
#dict to count words
countsdict=dict()
sentcnt = 0
wordcnt = 0
totwordcnt = 0
totletlength = 0
avgletcnt = 0.0
avgsentlength = 0.0

#loop thru the lines in the paragraph being read. 
for line in fh:
    #print(line)
    linelist.append(line)
    linewords = line.split(" ")
    ##sentences = line.split(".")
    
    #count letters in each word.
    #print(linewords)
    for word in linewords :
        letlength = len(word)
        totletlength = totletlength + letlength
        totwordcnt += 1
        
        #print("1: " + word + str(letlength))
        # print("2: " + str(totwordcnt))
    
    avgletcnt = totletlength / totwordcnt
    
    #Find words with periods using regex.
    periods = re.findall('(\S*["."])',line)
    #print(periods)
    #periodlist.append(periods)
    wordcnt = wordcnt + len(linewords)
    sentcnt = sentcnt + len(periods)

avgsentlength = totwordcnt / sentcnt

#print(linelist)
#print(linewords)
#print(sentences)
## assign counts to relevant variables for print.

#close file handle
fh.close()

#Print finval tallies
print(" ")
print("Approximate Word Count     : " + str(wordcnt) )
print("Approximate Sentence  Count: " + str(sentcnt) )
#print("Average Letter Count       : " + str(avgletcnt) )
print("Average Letter Count       : " + "%.2f" % avgletcnt)
print("Average Sentence Length    : " + "%.2f" % avgsentlength)

with  open(outfile,'w')  as fhout:
        print("Paragraph Analysis", file=fhout,end='\n')
        print("----------------------------------------", file=fhout,end='\n')
        print("Approximate Word Count     : " + str(wordcnt), 
              file=fhout,end='\n')
        print("Approximate Sentence  Count: " + str(sentcnt), 
              file=fhout,end='\n')
        print("Average Letter Count       : " + "%.2f" % avgletcnt,
              file=fhout,end='\n')
        print("Average Sentence Length    : " + "%.2f" % avgsentlength,
              file=fhout,end='\n')
        