
# coding: utf-8

# #Weather Analysis:
# The analysis is based on current weather obtained on june 20 and june 21. 
# The plot of latitude vs weather indicates that the temperature is highest near the tropic of cancer with latitude around 
# 23.5 deg N. T The maximum temperatures in the northern hemisphere falls considerably moving north of the 23.5 deg latitude 
# and moving south from the equator at 0 deg. There is also a wide variation in the maximum temperatures around the world 
# based on the latitude. The southern hemishphere experiences lower temperatures when it is  summer in  the northern hemisphere.
# 

# There does not seem to any correlation of latitude to cloudiness, windspeed or humidity. More historical analysis of weather data may be  needed to infer any correlations between latitude and cloudiness, windspeed or humidity. There does seem to be a concentration of data around 45-50 % humidity. This value is considered very conducive for humans. 

# In[15]:


#import required python libs.
import requests
import json
from pprint import pprint
from citipy import citipy
import random
import pandas as pd
import openweathermapy.core as owm
#import seaborn as sns
#config
from config import api_key
print(api_key)


# In[2]:


#urlw for openweather
#url = "http://api.openweathermap.org/data/2.5/weather?"
cnt=0
latlist=list()
longlist=list()

for k in range(-180,181,20):
    longlist.append(k)
#longlist=[-180,-160,-140,-120,-100,-8-75,-50,0,50,75,100,150,175]

#list of cities
cityset=set()

#list of countries corresponding to the city.
cnylist=list()
#create list of longitudes for use as a random choice

for i in range(-90,90,+2):
#use latitude choice from -90 to +90 and get a city closest to that latitude.
    for j in longlist:
        lat=i
        long=j
        city = citipy.nearest_city(lat, long)
        cityset.add(city.city_name)
        cnylist.append(city.country_code)
print(str(len(cityset)))
print(str(len(cnylist)))


# In[3]:


# Save config information.
url = "http://api.openweathermap.org/data/2.5/weather?"
units = "metric"

# Build partial query URL
query_url = f"{url}appid={api_key}&units={units}&q="
print(query_url)
#print(api_key)


# In[4]:


# Get current weather for all the cities using openweathermapy. 
#initialize count variables. 
cntcity=0
cntfail=0
     
# set up lists to hold reponse info
citylist=list()
cloudiness=list()
temp = list()
cnycode=list()
date=list()
humidity=list()
lat = list()
long=list()
tempmax=list()
windspeed=list()

# Loop through the list of cities and perform a request for weather data on each city.store results in lists. 
for city in cityset:
    #print(str(city))
    cntcity=cntcity+1
    print("Retrieving  data for record " + str(cntcity) + " " + city)
    try:
        weatherdetails = requests.get(query_url + city).json()
        #pprint(weatherdetails)
        citylist.append (weatherdetails["name"])
        cloudiness.append (weatherdetails["clouds"]["all"])
        cnycode.append (weatherdetails["sys"]["country"])
        #datetime=weatherdetails["dt"]
        date.append (weatherdetails["dt"])
        humidity.append (weatherdetails["main"]["humidity"])
        lat.append (weatherdetails["coord"]["lat"])
        long.append (weatherdetails["coord"]["lon"])
        tempmax.append (weatherdetails["main"]["temp_max"])
        windspeed.append (weatherdetails["wind"]["speed"])
    except:
        cntfail +=1
        print("Error in getting data for city " + city)
        print("error code: " + weatherdetails["cod"])
        print("message: " + weatherdetails["message"])

pprint(weatherdetails)        
print("Data Retrieval Complete....")
print("---------------------------------------------------------")
print("Number of cities weather data  not found: " + str(cntfail))


# In[5]:


print(len(citylist))
print(len(cloudiness))
print(len(tempmax))
print(len(humidity))
print(len(lat))


# In[6]:


#store results into a dictionary and convert to a dataframe. 
weatherdict=dict()
weatherdict={"City":citylist,"Cloudiness":cloudiness,"Country_code":cnycode,"Date":date,
             "Humidity":humidity,"Latitude":lat,"Longitude":long,"Max_temp":tempmax,
             "Wind_speed":windspeed}
#print(len(weatherdict))
weather_df = pd.DataFrame(weatherdict)
weather_df.tail(10)


# In[12]:


#Save weather data in a csv file for future reference and use. 
weather_df.to_csv("weatherdata.csv",index=False,header=True)
weather_df.info()


# In[16]:


#Import dependencies for plotting.
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
x_axis=weather_df["Latitude"]
y_axis_maxtemp=weather_df["Max_temp"]
y_axis_humidity=weather_df["Humidity"]
y_axis_cloudiness = weather_df["Cloudiness"]
y_axis_Windspeed = weather_df["Wind_speed"]


# In[13]:


#Review cities that have temperature greater than 28 deg C.
weather_df.loc[weather_df["Max_temp"] >= 38]
#weather_df_sortedbytemp = weather_df.sort("Max_temp",axis=1,ascending=False,inplace=False)
#weather_df_sortedbytemp.head(10)


# In[36]:


#Plot Latitude vs maximum temp(C)
sns.regplot(x_axis, y_axis_maxtemp, data=None, x_estimator=None, x_bins=None, x_ci='ci', 
            scatter=True, fit_reg=True, ci=95, n_boot=1000, units=None, order=1, 
            logistic=False, lowess=False, robust=False, logx=False, x_partial=None, y_partial=None, 
            truncate=False, dropna=True, x_jitter=None, y_jitter=None, label="Latitude vs Max temperature(C)", 
            color=None,marker='o', scatter_kws=None, line_kws=None, ax=None)
plt.title("Latitude vs Max temperature(C) Date: 06/21/2018 ")
plt.grid()
plt.xlim(-65,85)
plt.ylim(-10,50)
plt.ylabel("Maximum Temp in C")
plt.savefig("latvsMaxtemp.png")


# In[27]:


#Plot of latitude vs Humidity
sns.regplot(x_axis, y_axis_humidity, data=None, x_estimator=None, x_bins=None, x_ci='ci', 
            scatter=True, fit_reg=False, ci=95, n_boot=1000, units=None, order=1, 
            logistic=False, lowess=False, robust=False, logx=False, x_partial=None, y_partial=None, 
            truncate=False, dropna=True, x_jitter=None, y_jitter=None, label=None, color="g", 
            marker='o', scatter_kws=None, line_kws=None, ax=None)
plt.title("Latitude vs Humidity, Date: 06/21/2018 ")
plt.xlim(-65,85)
plt.ylim(-0,100)
plt.ylabel("Humidity % ")
plt.savefig("latvshumidity.png")


# In[31]:


#Plot of latitude vs Cloudiness
sns.regplot(x_axis, y_axis_cloudiness, data=None, x_estimator=None, x_bins=None, x_ci='ci', 
            scatter=True, fit_reg=False, ci=95, n_boot=1000, units=None, order=1, 
            logistic=False, lowess=False, robust=False, logx=False, x_partial=None, y_partial=None, 
            truncate=False, dropna=True, x_jitter=None, y_jitter=None, label=None, color="grey", 
            marker='o', scatter_kws=None, line_kws=None, ax=None)
plt.title("Latitude vs Cloudiness, Date: 06/21/2018 ")
plt.xlim(-65,85)
plt.ylim(-5,100)
plt.ylabel("Cloudiness ")
plt.savefig("latvscloudiness.png")


# In[35]:


#Latitude vs windspeed
sns.regplot(x_axis, y_axis_Windspeed, data=None, x_estimator=None, x_bins=None, x_ci='ci', 
            scatter=True, fit_reg=False, ci=95, n_boot=1000, units=None, order=1, 
            logistic=False, lowess=False, robust=False, logx=False, x_partial=None, y_partial=None, 
            truncate=False, dropna=True, x_jitter=None, y_jitter=None, label=None, color="cyan", 
            marker='+', scatter_kws=None, line_kws=None, ax=None)
plt.title("Latitude vs Wind speed, Date: 06/21/2018 ")
plt.grid()
plt.xlim(-65,85)
plt.ylim(-0,20)
plt.ylabel("Wind Speed ")
plt.savefig("latvswindspeed.png")

