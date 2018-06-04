
# coding: utf-8

# # PyCity Schools Analysis
# 
# * As a whole, schools with higher budgets, did not yield better test results. By contrast, schools with higher spending per student actually (\$645-675) underperformed compared to schools with smaller budgets (<\$585 per student).
# 
# * As a whole, smaller and medium sized schools dramatically out-performed large sized schools on passing math performances (89-91% passing vs 67%).
# 
# * As a whole, charter schools out-performed the public district schools across all metrics. However, more analysis will be required to glean if the effect is due to school practices or the fact that charter schools tend to serve smaller student populations per school. 
# ---

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
print(students_df.head(3))

schools_df  = pd.read_csv(fp_schools)
print(schools_df.head(3))



# In[2]:



student_count = students_df["Student ID"].count()
student_count


# In[3]:


school_count= schools_df["name"].count()
school_count


# In[4]:


students_df.columns


# In[5]:


tot_budget = schools_df["budget"].sum()
tot_budget


# In[6]:


mean_reading_score = students_df["reading_score"].mean()
mean_reading_score


# In[7]:


mean_math_score = students_df["math_score"].mean()
mean_math_score


# In[15]:


pass_math_df_cnt = students_df.loc[students_df["math_score"] > 70,:]["Student ID"].count()
pass_math_df_cnt


# In[16]:


pass_math_percent = (pass_math_df_cnt / student_count)*100
pass_math_percent


# In[17]:


pass_reading_df_cnt = students_df.loc[students_df["reading_score"] > 70]["Student ID"].count()
pass_reading_df_cnt


# In[18]:


pass_reading_percent = (pass_reading_df_cnt / student_count)*100
pass_reading_percent


# In[12]:


overall_pass_percent = (pass_math_percent + pass_reading_percent) / 2 
overall_pass_percent


# In[78]:


summary_dict={"Total Schools": [school_count], "Total Students": [student_count],"Total Budget":24649428,
              "Average Math Score":mean_math_score,"Average Reading Score":mean_reading_score,
              "% Passing Math":pass_math_percent,"% Passing Reading":pass_reading_percent,
              "Overall Passing Rate":overall_pass_percent
             }

summary_dist_df = pd.DataFrame(summary_dict,columns=["Total Schools","Total Students","Total Budget","Average Math Score",
                                                     "Average Reading Score","% Passing Math","% Passing Reading",
                                                     "Overall Passing Rate"
                                                    ])
summary_dist_df.head()


# In[79]:


summary_dist_df["Total Students"] = summary_dist_df["Total Students"].map("{:,}".format)


# ## District Summary

# In[80]:


summary_dist_df["Total Budget"]   = summary_dist_df["Total Budget"].map("${:,.2f}".format)
summary_dist_df.head()


# In[136]:


schools_ren_df = schools_df.rename(columns={"name": "school"})
#schools_ren_df = schools_ren_df.set_index("school")
del schools_ren_df["School ID"]
schools_ren_df.head(20)


# In[134]:


#mean of reading and math scores by school
students_df_groupsch_avg = students_df.groupby('school').mean()
del students_df_groupsch_avg["Student ID"]
students_df_groupsch_avg.reset_index(level=0, inplace=True)
students_df_groupsch_avg = students_df_groupsch_avg.rename(columns={"reading_score":"avg_reading_score",
                                                                    "math_score":"avg_math_score"})
#students_df_groupsch_avg["school"]=students_df_groupsch_avg.index
students_df_groupsch_avg


# In[160]:


#total students by school.
students_df_groupsch_totstudents = students_df.groupby('school').count()
#students_df_groupsch_totstudents = students_df.groupby(['school'])["name"].count()

#students_df_groupsch_totstudents = pd.DataFrame(students_df_groupsch_totstudents,columns=["Total Student Count"])
students_df_groupsch_totstudents.reset_index(level=0,inplace=True)
#del students_df_groupsch_totstudents[["name","gender","grade","reading_score","math_score"]]
students_df_groupsch_totstudents= students_df_groupsch_totstudents[["school","name"]]
students_df_groupsch_totstudents = students_df_groupsch_totstudents.rename(columns={"name":"Total_student_count"})
students_df_groupsch_totstudents


# In[173]:


## Count of students passing math by school
#students_df_groupsch.loc[students_df_groupsch["math_score" > 70]]
#??pass_math_df_cnt = students_df.loc[students_df["math_score"] > 70,:]["Student ID"].count()
school_stu_math_df = students_df.loc[students_df["math_score"] > 70,:]
#school_stu_math_df_cnt= school_stu_math_df.groupby('school').count()
#school_stu_math_df_cnt= school_stu_math_df.groupby('school')["Student ID"].count()
school_stu_math_df_cnt= school_stu_math_df.groupby('school').count()

school_stu_math_df_cnt.reset_index(level=0,inplace=True)
school_stu_math_df_cnt=school_stu_math_df_cnt[["school","name"]]
school_stu_math_df_cnt = school_stu_math_df_cnt.rename(columns={"name":"pass_math_count"})
school_stu_math_df_cnt


# In[171]:


#Count of students passing reading.
school_stu_read_df = students_df.loc[students_df["reading_score"] > 70,:]
#school_stu_read_df.head(10)
#school_stu_read_df_cnt= school_stu_read_df.groupby('school')["name"].count()
school_stu_read_df_cnt= school_stu_read_df.groupby('school').count()
school_stu_read_df_cnt.reset_index(level=0,inplace=True)
school_stu_read_df_cnt=school_stu_read_df_cnt[["school","name"]]
#rename column to pass reading count 
school_stu_read_df_cnt=school_stu_read_df_cnt.rename(columns={"name":"pass_reading_cnt"})
school_stu_read_df_cnt


# In[137]:


#merge school info and average scores for new summary dataframe1

school_mrg1= pd.merge(schools_ren_df ,students_df_groupsch_avg, on="school")
school_mrg1


# In[161]:


#merge the dataframe with total students into the above mrg1 dataframe
school_mrg2 = pd.merge(school_mrg1,students_df_groupsch_totstudents, on="school")
school_mrg2


# In[174]:


school_readmath_cnt_mrg3 = pd.merge(school_stu_math_df_cnt,school_stu_read_df_cnt,on="school")
school_readmath_cnt_mrg3


# In[176]:


# add math and student pass counts to the merge dataframe - result is mrg4.
school_mrg4 = pd.merge(school_mrg2 ,school_readmath_cnt_mrg3, on="school")
school_mrg4


# In[178]:


school_mrg4["percent passing math"] = (school_mrg4["pass_math_count"] * 100)/(school_mrg4["Total_student_count"])
school_mrg4


# In[180]:


school_mrg4["percent passing Reading"] = (school_mrg4["pass_reading_cnt"] * 100)/(school_mrg4["Total_student_count"])
school_mrg4


# In[181]:


school_mrg4["overall passing rate"] = (school_mrg4["percent passing Reading"] + school_mrg4["percent passing math"]  ) / 2
school_mrg4


# In[183]:


school_mrg4["Per Student Budget"] = school_mrg4["budget"]/school_mrg4["Total_student_count"]
school_mrg4


# In[184]:


del school_mrg4["size"]

school_mrg4


# In[192]:


school_mrg4 = school_mrg4.rename(columns={"school":"School Name","type":"School Type","budget":"Total School Budget",
                   "avg_reading_score":"Average Reading Score","avg_math_score":"Average Math Score",
                   "percent passing math":"% Passing Math","percent passing Reading":"% Passing Reading",
                   "overall passing rate":"Overall Passing Rate","Per Student Budget":"Per Student Budget"}
                  )
school_mrg4


# In[213]:


School_summary_df = school_mrg4[["School Name","School Type","Total_student_count","Total School Budget","Per Student Budget",
                                 "Average Math Score","Average Reading Score","% Passing Math","% Passing Reading",
                                 "Overall Passing Rate"]]
School_summary_df


# In[210]:


#convert budget amounts to numeric values for formatting. 
School_summary_df['Total School Budget'] = pd.to_numeric(School_summary_df["Total School Budget"])
School_summary_df['Per Student Budget'] = pd.to_numeric(School_summary_df["Per Student Budget"])
School_summary_df


# ## School Summary

# In[214]:


#Change formtting to numeric. CAN BE RUN ONLY ONCE. previous needs to re-run to run this code again.
School_summary_df["Total School Budget"] = School_summary_df["Total School Budget"].map("${:,.2f}".format)
School_summary_df["Per Student Budget"] = School_summary_df["Per Student Budget"].map("${:,.2f}".format)



# In[215]:


School_summary_final_df = School_summary_df.set_index("School Name")
School_summary_final_df


# ## Top Performing Schools (By Passing Rate)

# ## Bottom Performing Schools (By Passing Rate)

# ## Math Scores by Grade

# ## Reading Score by Grade 

# ## Scores by School Spending

# ## Scores by School Size

# ## Scores by School Type
