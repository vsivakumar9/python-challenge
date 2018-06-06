# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:38:16 2018

@author: Shiva
"""
import os
#import csv
import pandas as pd

#create path variable and assign relevant file names.
fp_students=os.path.join("raw_data","students_complete.csv")
fp_schools=os.path.join("raw_data","schools_complete.csv")

#read files into pandas data frames.
students_df = pd.read_csv(fp_students)
print(students_df.head(10))

schools_df  = pd.read_csv(fp_schools)
print(schools_df.head(10))

