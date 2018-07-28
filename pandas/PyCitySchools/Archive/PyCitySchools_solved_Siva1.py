
# coding: utf-8

# # PyCity Schools Analysis
#  
# * Overall,smaller  schools seemed to peform better in math, reading and overall passing grades. School size seems to play an important role in the overall passing scores. 
# 
# * The data indicates that schools with higher budgets  and higher spending per student did not necessary  yield better test results. 
# 
# * Charter schools out-performed the public district schools across all metrics. More analysis may be required to required to determine if the effect is due to smaller school sizes or other factors. 
# 
# 

# In[1]:


# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:38:16 2018
@author: Shiva
"""
import os
#import csv
import pandas as pd
import numpy as np

#create path variable and assign relevant file names.
fp_students=os.path.join("raw_data","students_complete.csv")
fp_schools=os.path.join("raw_data","schools_complete.csv")

#read files into pandas data frames.
students_df = pd.read_csv(fp_students)

schools_df  = pd.read_csv(fp_schools)

print(students_df.head(3))
print(schools_df.head(3))
#students_df.columns


# In[2]:


#Determine district totals like total schools, total students, total budget, avg math score, avg reading score, % passing match, 
# % passing reading and overall passing rate. 
school_count= schools_df["name"].count()
student_count = students_df["Student ID"].count()
tot_budget = schools_df["budget"].sum()
mean_reading_score = students_df["reading_score"].mean()
mean_math_score = students_df["math_score"].mean()

#print values to verify 
print(student_count)
print(school_count)
print(tot_budget)
print(mean_reading_score)
print(mean_math_score)


# In[3]:


#Calulate number of students passing math and then use total student count to calculate % passing math. 
pass_math_df_cnt = students_df.loc[students_df["math_score"] > 70,:]["Student ID"].count()
#pass_math_df_cnt
pass_math_percent = (pass_math_df_cnt / student_count)*100
print(pass_math_percent)

#Calc % passing reading in a similar fashion. 
pass_reading_df_cnt = students_df.loc[students_df["reading_score"] > 70]["Student ID"].count()
pass_reading_df_cnt
pass_reading_percent = (pass_reading_df_cnt / student_count)*100
print(pass_reading_percent)

#calc overall pass percent as average of % passing math and % passing  reading.
overall_pass_percent = (pass_math_percent + pass_reading_percent) / 2 
print(overall_pass_percent)


# In[4]:


#Create a summary dict with all the values calculated above and covert to a dataframe. 
summary_dict={"Total Schools": [school_count], "Total Students": [student_count],"Total Budget":tot_budget,
              "Average Math Score":mean_math_score,"Average Reading Score":mean_reading_score,
              "% Passing Math":pass_math_percent,"% Passing Reading":pass_reading_percent,
              "Overall Passing Rate":overall_pass_percent
             }

summary_dist_df = pd.DataFrame(summary_dict,columns=["Total Schools","Total Students","Total Budget","Average Math Score",
                                                     "Average Reading Score","% Passing Math","% Passing Reading",
                                                     "Overall Passing Rate"
                                                    ])
summary_dist_df.head()


# ## District Summary

# In[5]:


#Final district summary and formatting based on above values. 
summary_dist_df["Total Students"] = summary_dist_df["Total Students"].map("{:,}".format)
summary_dist_df["Total Budget"]   = summary_dist_df["Total Budget"].map("${:,.2f}".format)
summary_dist_df.head()


# In[6]:


#Perform steps to determine values needed for school summary.
schools_ren_df = schools_df.rename(columns={"name": "school"})
#schools_ren_df = schools_ren_df.set_index("school")
del schools_ren_df["School ID"]
schools_ren_df.head(2)


# In[7]:


#mean of reading and math scores by school
students_df_groupsch_avg = students_df.groupby('school').mean()
del students_df_groupsch_avg["Student ID"]
students_df_groupsch_avg.reset_index(level=0, inplace=True)
students_df_groupsch_avg = students_df_groupsch_avg.rename(columns={"reading_score":"avg_reading_score",
                                                                    "math_score":"avg_math_score"})
#students_df_groupsch_avg["school"]=students_df_groupsch_avg.index
students_df_groupsch_avg.head(3)


# In[8]:


#total students by school.
students_df_groupsch_totstudents = students_df.groupby('school').count()
#students_df_groupsch_totstudents = students_df.groupby(['school'])["name"].count()

#students_df_groupsch_totstudents = pd.DataFrame(students_df_groupsch_totstudents,columns=["Total Student Count"])
students_df_groupsch_totstudents.reset_index(level=0,inplace=True)
#del students_df_groupsch_totstudents[["name","gender","grade","reading_score","math_score"]]
students_df_groupsch_totstudents= students_df_groupsch_totstudents[["school","name"]]
students_df_groupsch_totstudents = students_df_groupsch_totstudents.rename(columns={"name":"Total_student_count"})
students_df_groupsch_totstudents.head(3)


# In[9]:


## Count of students passing math by school
#students_df_groupsch.loc[students_df_groupsch["math_score" > 70]]
school_stu_math_df = students_df.loc[students_df["math_score"] > 70,:]
#school_stu_math_df_cnt= school_stu_math_df.groupby('school').count()
#school_stu_math_df_cnt= school_stu_math_df.groupby('school')["Student ID"].count()
school_stu_math_df_cnt= school_stu_math_df.groupby('school').count()

school_stu_math_df_cnt.reset_index(level=0,inplace=True)
school_stu_math_df_cnt=school_stu_math_df_cnt[["school","name"]]
school_stu_math_df_cnt = school_stu_math_df_cnt.rename(columns={"name":"pass_math_count"})
school_stu_math_df_cnt.head(3)


# In[10]:


#Count of students passing reading.
school_stu_read_df = students_df.loc[students_df["reading_score"] > 70,:]
#school_stu_read_df.head(10)
#school_stu_read_df_cnt= school_stu_read_df.groupby('school')["name"].count()
school_stu_read_df_cnt= school_stu_read_df.groupby('school').count()
school_stu_read_df_cnt.reset_index(level=0,inplace=True)
school_stu_read_df_cnt=school_stu_read_df_cnt[["school","name"]]
#rename column to pass reading count 
school_stu_read_df_cnt=school_stu_read_df_cnt.rename(columns={"name":"pass_reading_cnt"})
school_stu_read_df_cnt.head(3)


# In[11]:


#merge school info and average scores for new summary dataframe1
school_mrg1= pd.merge(schools_ren_df ,students_df_groupsch_avg, on="school")
school_mrg1.head(3)


# In[12]:


#merge the dataframe with total students into the above mrg1 dataframe
school_mrg2 = pd.merge(school_mrg1,students_df_groupsch_totstudents, on="school")
school_mrg2.head(3)


# In[13]:


school_readmath_cnt_mrg3 = pd.merge(school_stu_math_df_cnt,school_stu_read_df_cnt,on="school")
school_readmath_cnt_mrg3.head(3)


# In[14]:


# add math and student pass counts to the merge dataframe - result is mrg4.
school_mrg4 = pd.merge(school_mrg2 ,school_readmath_cnt_mrg3, on="school")

#Calculate % passing Math and percent passing reading. 
school_mrg4["percent passing math"] = (school_mrg4["pass_math_count"] * 100)/(school_mrg4["Total_student_count"])
school_mrg4["percent passing Reading"] = (school_mrg4["pass_reading_cnt"] * 100)/(school_mrg4["Total_student_count"])

#Calculate overall passing rate as average or percent passing for reading and math.
school_mrg4["overall passing rate"] = (school_mrg4["percent passing Reading"] + school_mrg4["percent passing math"]  ) / 2
school_mrg4.head(3)



# In[15]:


#Determine per student Budget based on total budget / Total student count(size)
school_mrg4["Per Student Budget"] = school_mrg4["budget"]/school_mrg4["Total_student_count"]
del school_mrg4["size"]
school_mrg4.head(3)


# In[16]:


#Rename columns to meaningful names 
school_mrg4 = school_mrg4.rename(columns={"school":"School Name","type":"School Type","budget":"Total School Budget",
                   "avg_reading_score":"Average Reading Score","avg_math_score":"Average Math Score",
                    "Total_student_count":"Total Students","percent passing math":"% Passing Math",
                   "percent passing Reading":"% Passing Reading","overall passing rate":"Overall Passing Rate",
                   "Per Student Budget":"Per Student Budget"}
                  )
school_mrg4.head(3)


# In[17]:


School_summary_df = school_mrg4[["School Name","School Type","Total Students","Total School Budget","Per Student Budget",
                                 "Average Math Score","Average Reading Score","% Passing Math","% Passing Reading",
                                 "Overall Passing Rate"]]
#convert budget amounts to numeric values before formatting. 
School_summary_df['Total School Budget'] = pd.to_numeric(School_summary_df["Total School Budget"])
School_summary_df['Per Student Budget'] = pd.to_numeric(School_summary_df["Per Student Budget"])
##School_summary_df.head(3)
##School_summary_df.dtypes
#Keep a dataframe with numeric values for relevant fields. 
School_summary_dfnum = School_summary_df.copy()
School_summary_dfnum.head(3)
#School_summary_dfnum.dtypes


# ## School Summary

# In[18]:


#Change formtting to numeric. CAN BE RUN ONLY ONCE. previous needs to re-run to run this code again.
School_summary_df["Total School Budget"] = School_summary_df["Total School Budget"].map("${:,.2f}".format)
School_summary_df["Per Student Budget"] = School_summary_df["Per Student Budget"].map("${:,.2f}".format)
#School_summary_dfnum.dtypes


# In[19]:


#Set index to school name for final school summary
School_summary_final_df = School_summary_df.set_index("School Name")
School_summary_final_df


# ## Top Performing Schools (By Passing Rate)

# In[20]:


#Determine top performing schools by overall passing rate.
schools_top_perform = School_summary_final_df.sort_values(["Overall Passing Rate"], ascending=False)
##schools_top_perform = schools_top_perform.rename(columns={"Total_student_count":"Total Students"})
schools_top_perform.iloc[0:5,:]


# ## Bottom Performing Schools (By Passing Rate)

# In[21]:


#Determine bottom performing schools by overall passing rate.
schools_bottom_perform = School_summary_final_df.sort_values(["Overall Passing Rate"], ascending=True)
##schools_bottom_perform = schools_bottom_perform.rename(columns={"Total_student_count":"Total Students"})
schools_bottom_perform.iloc[0:5,:]


# ## Math Scores by Grade

# In[22]:


#Math scores by passing grade.
#students_gr_grade_df = students_df.groupby(['school','grade']).reading_score.mean()
students_gr_grade_df = students_df.groupby(['school','grade']).reading_score.mean().unstack(level=1)
students_gr_grade_df 


# ## Reading Score by Grade 

# In[23]:


#Reading scores by passing grade.
#students_gr_avgreadgrade_df = students_df.groupby(['school','grade']).math_score.mean()
students_gr_avgreadgrade_df = students_df.groupby(['school','grade']).math_score.mean().unstack(level=1)


# In[24]:


students_gr_avgreadgrade_df


# In[25]:


#School_summary_dfnum.dtypes


# In[26]:


#select relevant columns and assign to new dataframe. This is to start steps for scores by school spending. 

School_summary_df2 = School_summary_dfnum[["Average Math Score", "Average Reading Score","% Passing Math",
                                         "% Passing Reading","Overall Passing Rate","Per Student Budget"]]
School_summary_df2.head(3)


# ## Scores by School Spending

# In[27]:


#scores by School spending
bins=[575,600,625,650,675]
binnames=["575 to 600","600 to 625","625 to 650","650 to 675"]
School_summary_df2["Spending ranges Per student"] = pd.cut(School_summary_df2["Per Student Budget"],bins,labels=binnames)
School_summary_df2.head(3)


# In[28]:


## create data frame with relevant columns, group by per student summary and calc mean.
##These are the Final scores by school spending. 
School_summary_df3 = School_summary_df2[["Average Math Score","Average Reading Score","% Passing Math","% Passing Reading",
                                       "Overall Passing Rate", "Spending ranges Per student"]]
School_summary_df3 = School_summary_df3.groupby('Spending ranges Per student')
School_spending_summary_final= School_summary_df3.mean()
School_spending_summary_final


# ## Scores by School Size

# In[29]:


#Get dataset to df1 to process bins based on school size and create table with avg math score, avg reading score, % passing
#math, % pass reading and overall passing rate.
School_size_df1 = School_summary_dfnum
School_size_df1.sort_values('Total Students').head(2) 


# In[30]:


#scores by School size.. define bins for school size. 
School_size_df2 = School_size_df1[["Average Math Score","Average Reading Score","% Passing Math","% Passing Reading",
                                       "Overall Passing Rate", "Total Students"]]
bins2=[0,1500,3000,5000]
binnames2=["Small<1500 students)","Medium-1500 to 3000 students","Large-3000 to 5000 students"]
School_size_df2["school size summary"] = pd.cut(School_size_df2["Total Students"],bins2,labels=binnames2)
School_size_df2.tail(2)


# In[31]:


#Group by school size summary and calculate mean of relevant columns.Final for school size summary
School_size_df3 = School_size_df2
del School_size_df3["Total Students"]
School_size_df3 = School_size_df3.groupby("school size summary")

School_size_summary_final= School_size_df3.mean()
School_size_summary_final


# ## Scores by School Type

# In[32]:


#Group schools based on school type - Charter, District
school_type_df1 = School_summary_dfnum[["Average Math Score","Average Reading Score","% Passing Math","% Passing Reading",
                                       "Overall Passing Rate", "School Type"]]
school_type_df2 =  school_type_df1.groupby('School Type')
school_type_df3_final = school_type_df2.mean()
school_type_df3_final

