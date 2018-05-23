# -*- coding: utf-8 -*-
"""
Created on Sat May  19 13:18:49 2018

@author: Shiva
"""

# Module for reading CSV's
import csv
import os

csvpath = os.path.join('netflix_ratings.csv')

# Use words.txt as the file name
fname = input("Enter file name: ")
try :
    fh = open(fname)
except:
    print ('invalid file name',fname)
    quit()
    
for line in fh:
    lineup = line.upper()
    lineup1 = lineup.rstrip()
    print(lineup1)