# -*- coding: utf-8 -*-
"""
Created on Sat May  19 13:18:49 2018

@author: Shiva
"""

# Module for reading CSV's
#import csv
import os
import re

linelist=list()

#dict to count words
countsdict=dict()


filepath = os.path.join("raw_data","paragraph_1.txt")

# Use paragraph_1.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = filepath
    print(fname)
try :
    fh = open(fname)
except:
    print ('invalid file name or path: ',fname)
    quit()
    
for line in fh:
    #print(line)
    linelist.append(line)
    linewords = line.split(" ")
    sentences = line.split(".")
#print(linelist)
print(linewords)
print(sentences)
wordcnt = len(linewords)
sentcnt = len(sentences)
#close file handle
fh.close()

#Print finval tallies
print(" ")
print ("Approximate Word Count     : " + str(wordcnt))
print ("Approximate sentence  Count: " + str(sentcnt))

