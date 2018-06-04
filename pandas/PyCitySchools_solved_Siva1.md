
# PyCity Schools Analysis

* As a whole, schools with higher budgets, did not yield better test results. By contrast, schools with higher spending per student actually (\$645-675) underperformed compared to schools with smaller budgets (<\$585 per student).

* As a whole, smaller and medium sized schools dramatically out-performed large sized schools on passing math performances (89-91% passing vs 67%).

* As a whole, charter schools out-performed the public district schools across all metrics. However, more analysis will be required to glean if the effect is due to school practices or the fact that charter schools tend to serve smaller student populations per school. 
---


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
print(students_df.head(3))

schools_df  = pd.read_csv(fp_schools)
print(schools_df.head(3))


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

student_count = students_df["Student ID"].count()
student_count

```




    39170




```python
school_count= schools_df["name"].count()
school_count
```




    15




```python
students_df.columns

```




    Index(['Student ID', 'name', 'gender', 'grade', 'school', 'reading_score',
           'math_score'],
          dtype='object')




```python
tot_budget = schools_df["budget"].sum()
tot_budget
```




    24649428




```python
mean_reading_score = students_df["reading_score"].mean()
mean_reading_score
```




    81.87784018381414




```python
mean_math_score = students_df["math_score"].mean()
mean_math_score
```




    78.98537145774827




```python
pass_math_df_cnt = students_df.loc[students_df["math_score"] > 70,:]["Student ID"].count()
pass_math_df_cnt
```




    28356




```python
pass_math_percent = (pass_math_df_cnt / student_count)*100
pass_math_percent
```




    72.39213683941792




```python
pass_reading_df_cnt = students_df.loc[students_df["reading_score"] > 70]["Student ID"].count()
pass_reading_df_cnt
```




    32500




```python
pass_reading_percent = (pass_reading_df_cnt / student_count)*100
pass_reading_percent

```




    82.97166198621395




```python
overall_pass_percent = (pass_math_percent + pass_reading_percent) / 2 
overall_pass_percent
```




    77.68189941281594




```python
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




```python
summary_dist_df["Total Students"] = summary_dist_df["Total Students"].map("{:,}".format)

```

## District Summary


```python
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
schools_ren_df = schools_df.rename(columns={"name": "school"})
#schools_ren_df = schools_ren_df.set_index("school")
del schools_ren_df["School ID"]
schools_ren_df.head(20)

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
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
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
students_df_groupsch_avg

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
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>80.746258</td>
      <td>77.102592</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>83.816757</td>
      <td>83.351499</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>80.934412</td>
      <td>77.289752</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>83.814988</td>
      <td>83.803279</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>81.182722</td>
      <td>76.629414</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>80.966394</td>
      <td>77.072464</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>84.044699</td>
      <td>83.839917</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>80.744686</td>
      <td>76.842711</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>83.725724</td>
      <td>83.359455</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>83.848930</td>
      <td>83.418349</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>83.989488</td>
      <td>83.274201</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>83.955000</td>
      <td>83.682222</td>
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
students_df_groupsch_totstudents

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
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>2739</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>1468</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>4635</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>427</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>2917</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>4761</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>962</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>3999</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>1761</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>1635</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>2283</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>1800</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>1801</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>1317</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>3001</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>387</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>1847</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>3040</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>882</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>2562</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>1583</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>1475</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>2076</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>1625</td>
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
school_stu_read_df_cnt
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
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>2123</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>1371</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>3624</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>396</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>2299</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>3727</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>887</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>3109</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>1631</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>1519</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>2129</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>1682</td>
    </tr>
  </tbody>
</table>
</div>




```python
#merge school info and average scores for new summary dataframe1

school_mrg1= pd.merge(schools_ren_df ,students_df_groupsch_avg, on="school")
school_mrg1
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
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>80.934412</td>
      <td>77.289752</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>83.816757</td>
      <td>83.351499</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>83.989488</td>
      <td>83.274201</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>83.975780</td>
      <td>83.061895</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>81.033963</td>
      <td>77.048432</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>83.814988</td>
      <td>83.803279</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>84.044699</td>
      <td>83.839917</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>83.955000</td>
      <td>83.682222</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>80.744686</td>
      <td>76.842711</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>80.966394</td>
      <td>77.072464</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>80.746258</td>
      <td>77.102592</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>83.848930</td>
      <td>83.418349</td>
    </tr>
  </tbody>
</table>
</div>




```python
#merge the dataframe with total students into the above mrg1 dataframe
school_mrg2 = pd.merge(school_mrg1,students_df_groupsch_totstudents, on="school")
school_mrg2

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
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>80.934412</td>
      <td>77.289752</td>
      <td>4635</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>1468</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>2283</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>1858</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>81.033963</td>
      <td>77.048432</td>
      <td>4976</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>427</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>962</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>83.955000</td>
      <td>83.682222</td>
      <td>1800</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>80.744686</td>
      <td>76.842711</td>
      <td>3999</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>80.966394</td>
      <td>77.072464</td>
      <td>4761</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>80.746258</td>
      <td>77.102592</td>
      <td>2739</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>1635</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_readmath_cnt_mrg3 = pd.merge(school_stu_math_df_cnt,school_stu_read_df_cnt,on="school")
school_readmath_cnt_mrg3
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
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>1801</td>
      <td>2123</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>1317</td>
      <td>1371</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>3001</td>
      <td>3624</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>387</td>
      <td>396</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>1847</td>
      <td>2299</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>3040</td>
      <td>3727</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>882</td>
      <td>887</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>2562</td>
      <td>3109</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>1583</td>
      <td>1631</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>1475</td>
      <td>1519</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>2076</td>
      <td>2129</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>1625</td>
      <td>1682</td>
    </tr>
  </tbody>
</table>
</div>




```python
# add math and student pass counts to the merge dataframe - result is mrg4.
school_mrg4 = pd.merge(school_mrg2 ,school_readmath_cnt_mrg3, on="school")
school_mrg4
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
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>80.934412</td>
      <td>77.289752</td>
      <td>4635</td>
      <td>3001</td>
      <td>3624</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>1468</td>
      <td>1317</td>
      <td>1371</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>2283</td>
      <td>2076</td>
      <td>2129</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>1858</td>
      <td>1664</td>
      <td>1744</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>81.033963</td>
      <td>77.048432</td>
      <td>4976</td>
      <td>3216</td>
      <td>3946</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>427</td>
      <td>387</td>
      <td>396</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>962</td>
      <td>882</td>
      <td>887</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>83.955000</td>
      <td>83.682222</td>
      <td>1800</td>
      <td>1625</td>
      <td>1682</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>80.744686</td>
      <td>76.842711</td>
      <td>3999</td>
      <td>2562</td>
      <td>3109</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>80.966394</td>
      <td>77.072464</td>
      <td>4761</td>
      <td>3040</td>
      <td>3727</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>80.746258</td>
      <td>77.102592</td>
      <td>2739</td>
      <td>1801</td>
      <td>2123</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>1635</td>
      <td>1475</td>
      <td>1519</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_mrg4["percent passing math"] = (school_mrg4["pass_math_count"] * 100)/(school_mrg4["Total_student_count"])
school_mrg4
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
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>80.934412</td>
      <td>77.289752</td>
      <td>4635</td>
      <td>3001</td>
      <td>3624</td>
      <td>64.746494</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>1468</td>
      <td>1317</td>
      <td>1371</td>
      <td>89.713896</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>2283</td>
      <td>2076</td>
      <td>2129</td>
      <td>90.932983</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>1858</td>
      <td>1664</td>
      <td>1744</td>
      <td>89.558665</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>81.033963</td>
      <td>77.048432</td>
      <td>4976</td>
      <td>3216</td>
      <td>3946</td>
      <td>64.630225</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>427</td>
      <td>387</td>
      <td>396</td>
      <td>90.632319</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>962</td>
      <td>882</td>
      <td>887</td>
      <td>91.683992</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>83.955000</td>
      <td>83.682222</td>
      <td>1800</td>
      <td>1625</td>
      <td>1682</td>
      <td>90.277778</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>80.744686</td>
      <td>76.842711</td>
      <td>3999</td>
      <td>2562</td>
      <td>3109</td>
      <td>64.066017</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>80.966394</td>
      <td>77.072464</td>
      <td>4761</td>
      <td>3040</td>
      <td>3727</td>
      <td>63.852132</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>80.746258</td>
      <td>77.102592</td>
      <td>2739</td>
      <td>1801</td>
      <td>2123</td>
      <td>65.753925</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>1635</td>
      <td>1475</td>
      <td>1519</td>
      <td>90.214067</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_mrg4["percent passing Reading"] = (school_mrg4["pass_reading_cnt"] * 100)/(school_mrg4["Total_student_count"])
school_mrg4
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
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>80.934412</td>
      <td>77.289752</td>
      <td>4635</td>
      <td>3001</td>
      <td>3624</td>
      <td>64.746494</td>
      <td>78.187702</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>1468</td>
      <td>1317</td>
      <td>1371</td>
      <td>89.713896</td>
      <td>93.392371</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>2283</td>
      <td>2076</td>
      <td>2129</td>
      <td>90.932983</td>
      <td>93.254490</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>1858</td>
      <td>1664</td>
      <td>1744</td>
      <td>89.558665</td>
      <td>93.864370</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>81.033963</td>
      <td>77.048432</td>
      <td>4976</td>
      <td>3216</td>
      <td>3946</td>
      <td>64.630225</td>
      <td>79.300643</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>427</td>
      <td>387</td>
      <td>396</td>
      <td>90.632319</td>
      <td>92.740047</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>962</td>
      <td>882</td>
      <td>887</td>
      <td>91.683992</td>
      <td>92.203742</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>83.955000</td>
      <td>83.682222</td>
      <td>1800</td>
      <td>1625</td>
      <td>1682</td>
      <td>90.277778</td>
      <td>93.444444</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>80.744686</td>
      <td>76.842711</td>
      <td>3999</td>
      <td>2562</td>
      <td>3109</td>
      <td>64.066017</td>
      <td>77.744436</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>80.966394</td>
      <td>77.072464</td>
      <td>4761</td>
      <td>3040</td>
      <td>3727</td>
      <td>63.852132</td>
      <td>78.281874</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>80.746258</td>
      <td>77.102592</td>
      <td>2739</td>
      <td>1801</td>
      <td>2123</td>
      <td>65.753925</td>
      <td>77.510040</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>1635</td>
      <td>1475</td>
      <td>1519</td>
      <td>90.214067</td>
      <td>92.905199</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_mrg4["overall passing rate"] = (school_mrg4["percent passing Reading"] + school_mrg4["percent passing math"]  ) / 2
school_mrg4
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
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>80.934412</td>
      <td>77.289752</td>
      <td>4635</td>
      <td>3001</td>
      <td>3624</td>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>71.467098</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>1468</td>
      <td>1317</td>
      <td>1371</td>
      <td>89.713896</td>
      <td>93.392371</td>
      <td>91.553134</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>2283</td>
      <td>2076</td>
      <td>2129</td>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>92.093736</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>1858</td>
      <td>1664</td>
      <td>1744</td>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>91.711518</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>81.033963</td>
      <td>77.048432</td>
      <td>4976</td>
      <td>3216</td>
      <td>3946</td>
      <td>64.630225</td>
      <td>79.300643</td>
      <td>71.965434</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>427</td>
      <td>387</td>
      <td>396</td>
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
      <td>84.044699</td>
      <td>83.839917</td>
      <td>962</td>
      <td>882</td>
      <td>887</td>
      <td>91.683992</td>
      <td>92.203742</td>
      <td>91.943867</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>83.955000</td>
      <td>83.682222</td>
      <td>1800</td>
      <td>1625</td>
      <td>1682</td>
      <td>90.277778</td>
      <td>93.444444</td>
      <td>91.861111</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>80.744686</td>
      <td>76.842711</td>
      <td>3999</td>
      <td>2562</td>
      <td>3109</td>
      <td>64.066017</td>
      <td>77.744436</td>
      <td>70.905226</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>80.966394</td>
      <td>77.072464</td>
      <td>4761</td>
      <td>3040</td>
      <td>3727</td>
      <td>63.852132</td>
      <td>78.281874</td>
      <td>71.067003</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>80.746258</td>
      <td>77.102592</td>
      <td>2739</td>
      <td>1801</td>
      <td>2123</td>
      <td>65.753925</td>
      <td>77.510040</td>
      <td>71.631982</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>1635</td>
      <td>1475</td>
      <td>1519</td>
      <td>90.214067</td>
      <td>92.905199</td>
      <td>91.559633</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_mrg4["Per Student Budget"] = school_mrg4["budget"]/school_mrg4["Total_student_count"]
school_mrg4
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
      <th>Per Student Budget</th>
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
      <td>655.0</td>
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
      <td>639.0</td>
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
      <td>600.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>80.934412</td>
      <td>77.289752</td>
      <td>4635</td>
      <td>3001</td>
      <td>3624</td>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>71.467098</td>
      <td>652.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>1468</td>
      <td>1317</td>
      <td>1371</td>
      <td>89.713896</td>
      <td>93.392371</td>
      <td>91.553134</td>
      <td>625.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>2283</td>
      <td>2076</td>
      <td>2129</td>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>92.093736</td>
      <td>578.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>1858</td>
      <td>1664</td>
      <td>1744</td>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>91.711518</td>
      <td>582.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>81.033963</td>
      <td>77.048432</td>
      <td>4976</td>
      <td>3216</td>
      <td>3946</td>
      <td>64.630225</td>
      <td>79.300643</td>
      <td>71.965434</td>
      <td>628.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>427</td>
      <td>387</td>
      <td>396</td>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>91.686183</td>
      <td>581.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>962</td>
      <td>882</td>
      <td>887</td>
      <td>91.683992</td>
      <td>92.203742</td>
      <td>91.943867</td>
      <td>609.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>83.955000</td>
      <td>83.682222</td>
      <td>1800</td>
      <td>1625</td>
      <td>1682</td>
      <td>90.277778</td>
      <td>93.444444</td>
      <td>91.861111</td>
      <td>583.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>80.744686</td>
      <td>76.842711</td>
      <td>3999</td>
      <td>2562</td>
      <td>3109</td>
      <td>64.066017</td>
      <td>77.744436</td>
      <td>70.905226</td>
      <td>637.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>80.966394</td>
      <td>77.072464</td>
      <td>4761</td>
      <td>3040</td>
      <td>3727</td>
      <td>63.852132</td>
      <td>78.281874</td>
      <td>71.067003</td>
      <td>650.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>80.746258</td>
      <td>77.102592</td>
      <td>2739</td>
      <td>1801</td>
      <td>2123</td>
      <td>65.753925</td>
      <td>77.510040</td>
      <td>71.631982</td>
      <td>644.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>1635</td>
      <td>1475</td>
      <td>1519</td>
      <td>90.214067</td>
      <td>92.905199</td>
      <td>91.559633</td>
      <td>638.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
del school_mrg4["size"]

school_mrg4
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
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>3022020</td>
      <td>80.934412</td>
      <td>77.289752</td>
      <td>4635</td>
      <td>3001</td>
      <td>3624</td>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>71.467098</td>
      <td>652.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>917500</td>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>1468</td>
      <td>1317</td>
      <td>1371</td>
      <td>89.713896</td>
      <td>93.392371</td>
      <td>91.553134</td>
      <td>625.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>1319574</td>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>2283</td>
      <td>2076</td>
      <td>2129</td>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>92.093736</td>
      <td>578.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1081356</td>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>1858</td>
      <td>1664</td>
      <td>1744</td>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>91.711518</td>
      <td>582.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>3124928</td>
      <td>81.033963</td>
      <td>77.048432</td>
      <td>4976</td>
      <td>3216</td>
      <td>3946</td>
      <td>64.630225</td>
      <td>79.300643</td>
      <td>71.965434</td>
      <td>628.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>248087</td>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>427</td>
      <td>387</td>
      <td>396</td>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>91.686183</td>
      <td>581.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>585858</td>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>962</td>
      <td>882</td>
      <td>887</td>
      <td>91.683992</td>
      <td>92.203742</td>
      <td>91.943867</td>
      <td>609.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1049400</td>
      <td>83.955000</td>
      <td>83.682222</td>
      <td>1800</td>
      <td>1625</td>
      <td>1682</td>
      <td>90.277778</td>
      <td>93.444444</td>
      <td>91.861111</td>
      <td>583.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>2547363</td>
      <td>80.744686</td>
      <td>76.842711</td>
      <td>3999</td>
      <td>2562</td>
      <td>3109</td>
      <td>64.066017</td>
      <td>77.744436</td>
      <td>70.905226</td>
      <td>637.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>3094650</td>
      <td>80.966394</td>
      <td>77.072464</td>
      <td>4761</td>
      <td>3040</td>
      <td>3727</td>
      <td>63.852132</td>
      <td>78.281874</td>
      <td>71.067003</td>
      <td>650.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>1763916</td>
      <td>80.746258</td>
      <td>77.102592</td>
      <td>2739</td>
      <td>1801</td>
      <td>2123</td>
      <td>65.753925</td>
      <td>77.510040</td>
      <td>71.631982</td>
      <td>644.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1043130</td>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>1635</td>
      <td>1475</td>
      <td>1519</td>
      <td>90.214067</td>
      <td>92.905199</td>
      <td>91.559633</td>
      <td>638.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_mrg4 = school_mrg4.rename(columns={"school":"School Name","type":"School Type","budget":"Total School Budget",
                   "avg_reading_score":"Average Reading Score","avg_math_score":"Average Math Score",
                   "percent passing math":"% Passing Math","percent passing Reading":"% Passing Reading",
                   "overall passing rate":"Overall Passing Rate","Per Student Budget":"Per Student Budget"}
                  )
school_mrg4
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
      <th>Total_student_count</th>
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
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>3022020</td>
      <td>80.934412</td>
      <td>77.289752</td>
      <td>4635</td>
      <td>3001</td>
      <td>3624</td>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>71.467098</td>
      <td>652.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>917500</td>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>1468</td>
      <td>1317</td>
      <td>1371</td>
      <td>89.713896</td>
      <td>93.392371</td>
      <td>91.553134</td>
      <td>625.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>1319574</td>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>2283</td>
      <td>2076</td>
      <td>2129</td>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>92.093736</td>
      <td>578.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1081356</td>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>1858</td>
      <td>1664</td>
      <td>1744</td>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>91.711518</td>
      <td>582.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>3124928</td>
      <td>81.033963</td>
      <td>77.048432</td>
      <td>4976</td>
      <td>3216</td>
      <td>3946</td>
      <td>64.630225</td>
      <td>79.300643</td>
      <td>71.965434</td>
      <td>628.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>248087</td>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>427</td>
      <td>387</td>
      <td>396</td>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>91.686183</td>
      <td>581.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>585858</td>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>962</td>
      <td>882</td>
      <td>887</td>
      <td>91.683992</td>
      <td>92.203742</td>
      <td>91.943867</td>
      <td>609.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1049400</td>
      <td>83.955000</td>
      <td>83.682222</td>
      <td>1800</td>
      <td>1625</td>
      <td>1682</td>
      <td>90.277778</td>
      <td>93.444444</td>
      <td>91.861111</td>
      <td>583.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>2547363</td>
      <td>80.744686</td>
      <td>76.842711</td>
      <td>3999</td>
      <td>2562</td>
      <td>3109</td>
      <td>64.066017</td>
      <td>77.744436</td>
      <td>70.905226</td>
      <td>637.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>3094650</td>
      <td>80.966394</td>
      <td>77.072464</td>
      <td>4761</td>
      <td>3040</td>
      <td>3727</td>
      <td>63.852132</td>
      <td>78.281874</td>
      <td>71.067003</td>
      <td>650.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>1763916</td>
      <td>80.746258</td>
      <td>77.102592</td>
      <td>2739</td>
      <td>1801</td>
      <td>2123</td>
      <td>65.753925</td>
      <td>77.510040</td>
      <td>71.631982</td>
      <td>644.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1043130</td>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>1635</td>
      <td>1475</td>
      <td>1519</td>
      <td>90.214067</td>
      <td>92.905199</td>
      <td>91.559633</td>
      <td>638.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
School_summary_df = school_mrg4[["School Name","School Type","Total_student_count","Total School Budget","Per Student Budget",
                                 "Average Math Score","Average Reading Score","% Passing Math","% Passing Reading",
                                 "Overall Passing Rate"]]
School_summary_df
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
      <th>Total_student_count</th>
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
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>71.467098</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>89.713896</td>
      <td>93.392371</td>
      <td>91.553134</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>92.093736</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>91.711518</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>628.0</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>64.630225</td>
      <td>79.300643</td>
      <td>71.965434</td>
    </tr>
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
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>583.0</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>90.277778</td>
      <td>93.444444</td>
      <td>91.861111</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>64.066017</td>
      <td>77.744436</td>
      <td>70.905226</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>63.852132</td>
      <td>78.281874</td>
      <td>71.067003</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>65.753925</td>
      <td>77.510040</td>
      <td>71.631982</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>90.214067</td>
      <td>92.905199</td>
      <td>91.559633</td>
    </tr>
  </tbody>
</table>
</div>




```python
#convert budget amounts to numeric values for formatting. 
School_summary_df['Total School Budget'] = pd.to_numeric(School_summary_df["Total School Budget"])
School_summary_df['Per Student Budget'] = pd.to_numeric(School_summary_df["Per Student Budget"])
School_summary_df

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
      <th>Total_student_count</th>
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
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>71.467098</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>89.713896</td>
      <td>93.392371</td>
      <td>91.553134</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>92.093736</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>91.711518</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>628.0</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>64.630225</td>
      <td>79.300643</td>
      <td>71.965434</td>
    </tr>
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
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>583.0</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>90.277778</td>
      <td>93.444444</td>
      <td>91.861111</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>64.066017</td>
      <td>77.744436</td>
      <td>70.905226</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>63.852132</td>
      <td>78.281874</td>
      <td>71.067003</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>65.753925</td>
      <td>77.510040</td>
      <td>71.631982</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>90.214067</td>
      <td>92.905199</td>
      <td>91.559633</td>
    </tr>
  </tbody>
</table>
</div>



## School Summary


```python
#Change formtting to numeric. CAN BE RUN ONLY ONCE. previous needs to re-run to run this code again.
School_summary_df["Total School Budget"] = School_summary_df["Total School Budget"].map("${:,.2f}".format)
School_summary_df["Per Student Budget"] = School_summary_df["Per Student Budget"].map("${:,.2f}".format)


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
      <th>Total_student_count</th>
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

## Bottom Performing Schools (By Passing Rate)

## Math Scores by Grade

## Reading Score by Grade 

## Scores by School Spending

## Scores by School Size

## Scores by School Type
