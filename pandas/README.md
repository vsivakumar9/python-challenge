
# PyCity Schools Analysis
 
* Overall,smaller  schools seemed to peform better in math, reading and overall passing grades. School size seems to play an important role in the overall passing scores. 

* The data indicates that schools with higher budgets  and higher spending per student did not necessary  yield better test results. 

* Charter schools out-performed the public district schools across all metrics. More analysis may be required to required to determine if the effect is due to smaller school sizes or other factors. 




```python
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

```

       Student ID             name gender grade             school  reading_score  \
    0           0     Paul Bradley      M   9th  Huang High School             66   
    1           1     Victor Smith      M  12th  Huang High School             94   
    2           2  Kevin Rodriguez      M  12th  Huang High School             90   
    
       math_score  
    0          79  
    1          61  
    2          60  
       School ID                  name      type  size   budget
    0          0     Huang High School  District  2917  1910635
    1          1  Figueroa High School  District  2949  1884411
    2          2   Shelton High School   Charter  1761  1056600
    


```python
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
```

    39170
    15
    24649428
    81.87784018381414
    78.98537145774827
    


```python
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
```

    72.39213683941792
    82.97166198621395
    77.68189941281594
    


```python
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
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39170</td>
      <td>24649428</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>72.392137</td>
      <td>82.971662</td>
      <td>77.681899</td>
    </tr>
  </tbody>
</table>
</div>



## District Summary


```python
#Final district summary and formatting based on above values. 
summary_dist_df["Total Students"] = summary_dist_df["Total Students"].map("{:,}".format)
summary_dist_df["Total Budget"]   = summary_dist_df["Total Budget"].map("${:,.2f}".format)
summary_dist_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39,170</td>
      <td>$24,649,428.00</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>72.392137</td>
      <td>82.971662</td>
      <td>77.681899</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Perform steps to determine values needed for school summary.
schools_ren_df = schools_df.rename(columns={"name": "school"})
#schools_ren_df = schools_ren_df.set_index("school")
del schools_ren_df["School ID"]
schools_ren_df.head(2)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
  </tbody>
</table>
</div>




```python
#mean of reading and math scores by school
students_df_groupsch_avg = students_df.groupby('school').mean()
del students_df_groupsch_avg["Student ID"]
students_df_groupsch_avg.reset_index(level=0, inplace=True)
students_df_groupsch_avg = students_df_groupsch_avg.rename(columns={"reading_score":"avg_reading_score",
                                                                    "math_score":"avg_math_score"})
#students_df_groupsch_avg["school"]=students_df_groupsch_avg.index
students_df_groupsch_avg.head(3)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>avg_reading_score</th>
      <th>avg_math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>81.033963</td>
      <td>77.048432</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>83.975780</td>
      <td>83.061895</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>81.158020</td>
      <td>76.711767</td>
    </tr>
  </tbody>
</table>
</div>




```python
#total students by school.
students_df_groupsch_totstudents = students_df.groupby('school').count()
#students_df_groupsch_totstudents = students_df.groupby(['school'])["name"].count()

#students_df_groupsch_totstudents = pd.DataFrame(students_df_groupsch_totstudents,columns=["Total Student Count"])
students_df_groupsch_totstudents.reset_index(level=0,inplace=True)
#del students_df_groupsch_totstudents[["name","gender","grade","reading_score","math_score"]]
students_df_groupsch_totstudents= students_df_groupsch_totstudents[["school","name"]]
students_df_groupsch_totstudents = students_df_groupsch_totstudents.rename(columns={"name":"Total_student_count"})
students_df_groupsch_totstudents.head(3)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>Total_student_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>4976</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>1858</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>2949</td>
    </tr>
  </tbody>
</table>
</div>




```python
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

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>pass_math_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>3216</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>1664</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>1880</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>pass_reading_cnt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>3946</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>1744</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>2313</td>
    </tr>
  </tbody>
</table>
</div>




```python
#merge school info and average scores for new summary dataframe1
school_mrg1= pd.merge(schools_ren_df ,students_df_groupsch_avg, on="school")
school_mrg1.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>avg_reading_score</th>
      <th>avg_math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>81.182722</td>
      <td>76.629414</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>81.158020</td>
      <td>76.711767</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>83.725724</td>
      <td>83.359455</td>
    </tr>
  </tbody>
</table>
</div>




```python
#merge the dataframe with total students into the above mrg1 dataframe
school_mrg2 = pd.merge(school_mrg1,students_df_groupsch_totstudents, on="school")
school_mrg2.head(3)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>avg_reading_score</th>
      <th>avg_math_score</th>
      <th>Total_student_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>81.182722</td>
      <td>76.629414</td>
      <td>2917</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>81.158020</td>
      <td>76.711767</td>
      <td>2949</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>83.725724</td>
      <td>83.359455</td>
      <td>1761</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_readmath_cnt_mrg3 = pd.merge(school_stu_math_df_cnt,school_stu_read_df_cnt,on="school")
school_readmath_cnt_mrg3.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>pass_math_count</th>
      <th>pass_reading_cnt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>3216</td>
      <td>3946</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>1664</td>
      <td>1744</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>1880</td>
      <td>2313</td>
    </tr>
  </tbody>
</table>
</div>




```python
# add math and student pass counts to the merge dataframe - result is mrg4.
school_mrg4 = pd.merge(school_mrg2 ,school_readmath_cnt_mrg3, on="school")

#Calculate % passing Math and percent passing reading. 
school_mrg4["percent passing math"] = (school_mrg4["pass_math_count"] * 100)/(school_mrg4["Total_student_count"])
school_mrg4["percent passing Reading"] = (school_mrg4["pass_reading_cnt"] * 100)/(school_mrg4["Total_student_count"])

#Calculate overall passing rate as average or percent passing for reading and math.
school_mrg4["overall passing rate"] = (school_mrg4["percent passing Reading"] + school_mrg4["percent passing math"]  ) / 2
school_mrg4.head(3)


```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>avg_reading_score</th>
      <th>avg_math_score</th>
      <th>Total_student_count</th>
      <th>pass_math_count</th>
      <th>pass_reading_cnt</th>
      <th>percent passing math</th>
      <th>percent passing Reading</th>
      <th>overall passing rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>81.182722</td>
      <td>76.629414</td>
      <td>2917</td>
      <td>1847</td>
      <td>2299</td>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>71.066164</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>81.158020</td>
      <td>76.711767</td>
      <td>2949</td>
      <td>1880</td>
      <td>2313</td>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>71.091896</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>83.725724</td>
      <td>83.359455</td>
      <td>1761</td>
      <td>1583</td>
      <td>1631</td>
      <td>89.892107</td>
      <td>92.617831</td>
      <td>91.254969</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Determine per student Budget based on total budget / Total student count(size)
school_mrg4["Per Student Budget"] = school_mrg4["budget"]/school_mrg4["Total_student_count"]
del school_mrg4["size"]
school_mrg4.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>school</th>
      <th>type</th>
      <th>budget</th>
      <th>avg_reading_score</th>
      <th>avg_math_score</th>
      <th>Total_student_count</th>
      <th>pass_math_count</th>
      <th>pass_reading_cnt</th>
      <th>percent passing math</th>
      <th>percent passing Reading</th>
      <th>overall passing rate</th>
      <th>Per Student Budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>1910635</td>
      <td>81.182722</td>
      <td>76.629414</td>
      <td>2917</td>
      <td>1847</td>
      <td>2299</td>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>71.066164</td>
      <td>655.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>1884411</td>
      <td>81.158020</td>
      <td>76.711767</td>
      <td>2949</td>
      <td>1880</td>
      <td>2313</td>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>71.091896</td>
      <td>639.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1056600</td>
      <td>83.725724</td>
      <td>83.359455</td>
      <td>1761</td>
      <td>1583</td>
      <td>1631</td>
      <td>89.892107</td>
      <td>92.617831</td>
      <td>91.254969</td>
      <td>600.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Rename columns to meaningful names 
school_mrg4 = school_mrg4.rename(columns={"school":"School Name","type":"School Type","budget":"Total School Budget",
                   "avg_reading_score":"Average Reading Score","avg_math_score":"Average Math Score",
                    "Total_student_count":"Total Students","percent passing math":"% Passing Math",
                   "percent passing Reading":"% Passing Reading","overall passing rate":"Overall Passing Rate",
                   "Per Student Budget":"Per Student Budget"}
                  )
school_mrg4.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total School Budget</th>
      <th>Average Reading Score</th>
      <th>Average Math Score</th>
      <th>Total Students</th>
      <th>pass_math_count</th>
      <th>pass_reading_cnt</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
      <th>Per Student Budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>1910635</td>
      <td>81.182722</td>
      <td>76.629414</td>
      <td>2917</td>
      <td>1847</td>
      <td>2299</td>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>71.066164</td>
      <td>655.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>1884411</td>
      <td>81.158020</td>
      <td>76.711767</td>
      <td>2949</td>
      <td>1880</td>
      <td>2313</td>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>71.091896</td>
      <td>639.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1056600</td>
      <td>83.725724</td>
      <td>83.359455</td>
      <td>1761</td>
      <td>1583</td>
      <td>1631</td>
      <td>89.892107</td>
      <td>92.617831</td>
      <td>91.254969</td>
      <td>600.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```

    C:\Users\Sivakumar\AppData\Local\conda\conda\envs\PythonData\lib\site-packages\ipykernel_launcher.py:5: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """
    C:\Users\Sivakumar\AppData\Local\conda\conda\envs\PythonData\lib\site-packages\ipykernel_launcher.py:6: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>71.066164</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>71.091896</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>89.892107</td>
      <td>92.617831</td>
      <td>91.254969</td>
    </tr>
  </tbody>
</table>
</div>



## School Summary


```python
#Change formtting to numeric. CAN BE RUN ONLY ONCE. previous needs to re-run to run this code again.
School_summary_df["Total School Budget"] = School_summary_df["Total School Budget"].map("${:,.2f}".format)
School_summary_df["Per Student Budget"] = School_summary_df["Per Student Budget"].map("${:,.2f}".format)
#School_summary_dfnum.dtypes

```

    C:\Users\Sivakumar\AppData\Local\conda\conda\envs\PythonData\lib\site-packages\ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    C:\Users\Sivakumar\AppData\Local\conda\conda\envs\PythonData\lib\site-packages\ipykernel_launcher.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      This is separate from the ipykernel package so we can avoid doing imports until
    


```python
#Set index to school name for final school summary
School_summary_final_df = School_summary_df.set_index("School Name")
School_summary_final_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2917</td>
      <td>$1,910,635.00</td>
      <td>$655.00</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>71.066164</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2949</td>
      <td>$1,884,411.00</td>
      <td>$639.00</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>71.091896</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>Charter</td>
      <td>1761</td>
      <td>$1,056,600.00</td>
      <td>$600.00</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>89.892107</td>
      <td>92.617831</td>
      <td>91.254969</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>District</td>
      <td>4635</td>
      <td>$3,022,020.00</td>
      <td>$652.00</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>71.467098</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Charter</td>
      <td>1468</td>
      <td>$917,500.00</td>
      <td>$625.00</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>89.713896</td>
      <td>93.392371</td>
      <td>91.553134</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>Charter</td>
      <td>2283</td>
      <td>$1,319,574.00</td>
      <td>$578.00</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>92.093736</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>Charter</td>
      <td>1858</td>
      <td>$1,081,356.00</td>
      <td>$582.00</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>91.711518</td>
    </tr>
    <tr>
      <th>Bailey High School</th>
      <td>District</td>
      <td>4976</td>
      <td>$3,124,928.00</td>
      <td>$628.00</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>64.630225</td>
      <td>79.300643</td>
      <td>71.965434</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Charter</td>
      <td>427</td>
      <td>$248,087.00</td>
      <td>$581.00</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>91.686183</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>$585,858.00</td>
      <td>$609.00</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>91.683992</td>
      <td>92.203742</td>
      <td>91.943867</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>Charter</td>
      <td>1800</td>
      <td>$1,049,400.00</td>
      <td>$583.00</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>90.277778</td>
      <td>93.444444</td>
      <td>91.861111</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>District</td>
      <td>3999</td>
      <td>$2,547,363.00</td>
      <td>$637.00</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>64.066017</td>
      <td>77.744436</td>
      <td>70.905226</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>District</td>
      <td>4761</td>
      <td>$3,094,650.00</td>
      <td>$650.00</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>63.852132</td>
      <td>78.281874</td>
      <td>71.067003</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>District</td>
      <td>2739</td>
      <td>$1,763,916.00</td>
      <td>$644.00</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>65.753925</td>
      <td>77.510040</td>
      <td>71.631982</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>Charter</td>
      <td>1635</td>
      <td>$1,043,130.00</td>
      <td>$638.00</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>90.214067</td>
      <td>92.905199</td>
      <td>91.559633</td>
    </tr>
  </tbody>
</table>
</div>



## Top Performing Schools (By Passing Rate)


```python
#Determine top performing schools by overall passing rate.
schools_top_perform = School_summary_final_df.sort_values(["Overall Passing Rate"], ascending=False)
##schools_top_perform = schools_top_perform.rename(columns={"Total_student_count":"Total Students"})
schools_top_perform.iloc[0:5,:]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Wilson High School</th>
      <td>Charter</td>
      <td>2283</td>
      <td>$1,319,574.00</td>
      <td>$578.00</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>92.093736</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>$585,858.00</td>
      <td>$609.00</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>91.683992</td>
      <td>92.203742</td>
      <td>91.943867</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>Charter</td>
      <td>1800</td>
      <td>$1,049,400.00</td>
      <td>$583.00</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>90.277778</td>
      <td>93.444444</td>
      <td>91.861111</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>Charter</td>
      <td>1858</td>
      <td>$1,081,356.00</td>
      <td>$582.00</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>91.711518</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Charter</td>
      <td>427</td>
      <td>$248,087.00</td>
      <td>$581.00</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>91.686183</td>
    </tr>
  </tbody>
</table>
</div>



## Bottom Performing Schools (By Passing Rate)


```python
#Determine bottom performing schools by overall passing rate.
schools_bottom_perform = School_summary_final_df.sort_values(["Overall Passing Rate"], ascending=True)
##schools_bottom_perform = schools_bottom_perform.rename(columns={"Total_student_count":"Total Students"})
schools_bottom_perform.iloc[0:5,:]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rodriguez High School</th>
      <td>District</td>
      <td>3999</td>
      <td>$2,547,363.00</td>
      <td>$637.00</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>64.066017</td>
      <td>77.744436</td>
      <td>70.905226</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2917</td>
      <td>$1,910,635.00</td>
      <td>$655.00</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>71.066164</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>District</td>
      <td>4761</td>
      <td>$3,094,650.00</td>
      <td>$650.00</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>63.852132</td>
      <td>78.281874</td>
      <td>71.067003</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2949</td>
      <td>$1,884,411.00</td>
      <td>$639.00</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>71.091896</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>District</td>
      <td>4635</td>
      <td>$3,022,020.00</td>
      <td>$652.00</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>71.467098</td>
    </tr>
  </tbody>
</table>
</div>



## Math Scores by Grade


```python
#Math scores by passing grade.
#students_gr_grade_df = students_df.groupby(['school','grade']).reading_score.mean()
students_gr_grade_df = students_df.groupby(['school','grade']).reading_score.mean().unstack(level=1)
students_gr_grade_df 

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>grade</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
      <th>9th</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>80.907183</td>
      <td>80.945643</td>
      <td>80.912451</td>
      <td>81.303155</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>84.253219</td>
      <td>83.788382</td>
      <td>84.287958</td>
      <td>83.676136</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.408912</td>
      <td>80.640339</td>
      <td>81.384863</td>
      <td>81.198598</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>81.262712</td>
      <td>80.403642</td>
      <td>80.662338</td>
      <td>80.632653</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.706897</td>
      <td>84.288089</td>
      <td>84.013699</td>
      <td>83.369193</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.660147</td>
      <td>81.396140</td>
      <td>80.857143</td>
      <td>80.866860</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.324561</td>
      <td>83.815534</td>
      <td>84.698795</td>
      <td>83.677165</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.512386</td>
      <td>81.417476</td>
      <td>80.305983</td>
      <td>81.290284</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>80.773431</td>
      <td>80.616027</td>
      <td>81.227564</td>
      <td>81.260714</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.612000</td>
      <td>84.335938</td>
      <td>84.591160</td>
      <td>83.807273</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.629808</td>
      <td>80.864811</td>
      <td>80.376426</td>
      <td>80.993127</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.441964</td>
      <td>84.373786</td>
      <td>82.781671</td>
      <td>84.122642</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>84.254157</td>
      <td>83.585542</td>
      <td>83.831361</td>
      <td>83.728850</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>84.021452</td>
      <td>83.764608</td>
      <td>84.317673</td>
      <td>83.939778</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.812757</td>
      <td>84.156322</td>
      <td>84.073171</td>
      <td>83.833333</td>
    </tr>
  </tbody>
</table>
</div>



## Reading Score by Grade 


```python
#Reading scores by passing grade.
#students_gr_avgreadgrade_df = students_df.groupby(['school','grade']).math_score.mean()
students_gr_avgreadgrade_df = students_df.groupby(['school','grade']).math_score.mean().unstack(level=1)
```


```python
students_gr_avgreadgrade_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>grade</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
      <th>9th</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>76.996772</td>
      <td>77.515588</td>
      <td>76.492218</td>
      <td>77.083676</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.154506</td>
      <td>82.765560</td>
      <td>83.277487</td>
      <td>83.094697</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.539974</td>
      <td>76.884344</td>
      <td>77.151369</td>
      <td>76.403037</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.672316</td>
      <td>76.918058</td>
      <td>76.179963</td>
      <td>77.361345</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>84.229064</td>
      <td>83.842105</td>
      <td>83.356164</td>
      <td>82.044010</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.337408</td>
      <td>77.136029</td>
      <td>77.186567</td>
      <td>77.438495</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.429825</td>
      <td>85.000000</td>
      <td>82.855422</td>
      <td>83.787402</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>75.908735</td>
      <td>76.446602</td>
      <td>77.225641</td>
      <td>77.027251</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>76.691117</td>
      <td>77.491653</td>
      <td>76.863248</td>
      <td>77.187857</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.372000</td>
      <td>84.328125</td>
      <td>84.121547</td>
      <td>83.625455</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.612500</td>
      <td>76.395626</td>
      <td>77.690748</td>
      <td>76.859966</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>82.917411</td>
      <td>83.383495</td>
      <td>83.778976</td>
      <td>83.420755</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.087886</td>
      <td>83.498795</td>
      <td>83.497041</td>
      <td>83.590022</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.724422</td>
      <td>83.195326</td>
      <td>83.035794</td>
      <td>83.085578</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>84.010288</td>
      <td>83.836782</td>
      <td>83.644986</td>
      <td>83.264706</td>
    </tr>
  </tbody>
</table>
</div>




```python
#School_summary_dfnum.dtypes
```


```python
#select relevant columns and assign to new dataframe. This is to start steps for scores by school spending. 

School_summary_df2 = School_summary_dfnum[["Average Math Score", "Average Reading Score","% Passing Math",
                                         "% Passing Reading","Overall Passing Rate","Per Student Budget"]]
School_summary_df2.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
      <th>Per Student Budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>71.066164</td>
      <td>655.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>71.091896</td>
      <td>639.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>89.892107</td>
      <td>92.617831</td>
      <td>91.254969</td>
      <td>600.0</td>
    </tr>
  </tbody>
</table>
</div>



## Scores by School Spending


```python
#scores by School spending
bins=[575,600,625,650,675]
binnames=["575 to 600","600 to 625","625 to 650","650 to 675"]
School_summary_df2["Spending ranges Per student"] = pd.cut(School_summary_df2["Per Student Budget"],bins,labels=binnames)
School_summary_df2.head(3)

```

    C:\Users\Sivakumar\AppData\Local\conda\conda\envs\PythonData\lib\site-packages\ipykernel_launcher.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      after removing the cwd from sys.path.
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
      <th>Per Student Budget</th>
      <th>Spending ranges Per student</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>71.066164</td>
      <td>655.0</td>
      <td>650 to 675</td>
    </tr>
    <tr>
      <th>1</th>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>71.091896</td>
      <td>639.0</td>
      <td>625 to 650</td>
    </tr>
    <tr>
      <th>2</th>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>89.892107</td>
      <td>92.617831</td>
      <td>91.254969</td>
      <td>600.0</td>
      <td>575 to 600</td>
    </tr>
  </tbody>
</table>
</div>




```python
## create data frame with relevant columns, group by per student summary and calc mean.
##These are the Final scores by school spending. 
School_summary_df3 = School_summary_df2[["Average Math Score","Average Reading Score","% Passing Math","% Passing Reading",
                                       "Overall Passing Rate", "Spending ranges Per student"]]
School_summary_df3 = School_summary_df3.groupby('Spending ranges Per student')
School_spending_summary_final= School_summary_df3.mean()
School_spending_summary_final
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>Spending ranges Per student</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>575 to 600</th>
      <td>83.436210</td>
      <td>83.892196</td>
      <td>90.258770</td>
      <td>93.184236</td>
      <td>91.721503</td>
    </tr>
    <tr>
      <th>600 to 625</th>
      <td>83.595708</td>
      <td>83.930728</td>
      <td>90.698944</td>
      <td>92.798056</td>
      <td>91.748500</td>
    </tr>
    <tr>
      <th>625 to 650</th>
      <td>78.032719</td>
      <td>81.416375</td>
      <td>68.711132</td>
      <td>80.695926</td>
      <td>74.703529</td>
    </tr>
    <tr>
      <th>650 to 675</th>
      <td>76.959583</td>
      <td>81.058567</td>
      <td>64.032486</td>
      <td>78.500776</td>
      <td>71.266631</td>
    </tr>
  </tbody>
</table>
</div>



## Scores by School Size


```python
#Get dataset to df1 to process bins based on school size and create table with avg math score, avg reading score, % passing
#math, % pass reading and overall passing rate.
School_size_df1 = School_summary_dfnum
School_size_df1.sort_values('Total Students').head(2) 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>581.0</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>91.686183</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>91.683992</td>
      <td>92.203742</td>
      <td>91.943867</td>
    </tr>
  </tbody>
</table>
</div>




```python
#scores by School size.. define bins for school size. 
School_size_df2 = School_size_df1[["Average Math Score","Average Reading Score","% Passing Math","% Passing Reading",
                                       "Overall Passing Rate", "Total Students"]]
bins2=[0,1500,3000,5000]
binnames2=["Small<1500 students)","Medium-1500 to 3000 students","Large-3000 to 5000 students"]
School_size_df2["school size summary"] = pd.cut(School_size_df2["Total Students"],bins2,labels=binnames2)
School_size_df2.tail(2)

```

    C:\Users\Sivakumar\AppData\Local\conda\conda\envs\PythonData\lib\site-packages\ipykernel_launcher.py:6: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
      <th>Total Students</th>
      <th>school size summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13</th>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>65.753925</td>
      <td>77.510040</td>
      <td>71.631982</td>
      <td>2739</td>
      <td>Medium-1500 to 3000 students</td>
    </tr>
    <tr>
      <th>14</th>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>90.214067</td>
      <td>92.905199</td>
      <td>91.559633</td>
      <td>1635</td>
      <td>Medium-1500 to 3000 students</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Group by school size summary and calculate mean of relevant columns.Final for school size summary
School_size_df3 = School_size_df2
del School_size_df3["Total Students"]
School_size_df3 = School_size_df3.groupby("school size summary")

School_size_summary_final= School_size_df3.mean()
School_size_summary_final
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>school size summary</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Small&lt;1500 students)</th>
      <td>83.664898</td>
      <td>83.892148</td>
      <td>90.676736</td>
      <td>92.778720</td>
      <td>91.727728</td>
    </tr>
    <tr>
      <th>Medium-1500 to 3000 students</th>
      <td>80.904987</td>
      <td>82.822740</td>
      <td>80.462303</td>
      <td>87.605449</td>
      <td>84.033876</td>
    </tr>
    <tr>
      <th>Large-3000 to 5000 students</th>
      <td>77.063340</td>
      <td>80.919864</td>
      <td>64.323717</td>
      <td>78.378664</td>
      <td>71.351190</td>
    </tr>
  </tbody>
</table>
</div>



## Scores by School Type


```python
#Group schools based on school type - Charter, District
school_type_df1 = School_summary_dfnum[["Average Math Score","Average Reading Score","% Passing Math","% Passing Reading",
                                       "Overall Passing Rate", "School Type"]]
school_type_df2 =  school_type_df1.groupby('School Type')
school_type_df3_final = school_type_df2.mean()
school_type_df3_final
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>83.473852</td>
      <td>83.896421</td>
      <td>90.363226</td>
      <td>93.052812</td>
      <td>91.708019</td>
    </tr>
    <tr>
      <th>District</th>
      <td>76.956733</td>
      <td>80.966636</td>
      <td>64.302528</td>
      <td>78.324559</td>
      <td>71.313543</td>
    </tr>
  </tbody>
</table>
</div>


