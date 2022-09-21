import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
df=pd.read_excel("Julian_iski_data_python.xlsx")

"""
df_time= df["yyyy-mm-dd hh:mm:ss.sss"] # access only years column

son_deger=[]
for i in range(0,68140):
    ts=pd.Timestamp(df_time[i])  #convert date to julian
    son_deger.append(ts.to_julian_date())

df["Julian"]=son_deger # create new column
df.to_excel("Julian_iski_daQta_python.xlsx")


"""

b2_station= df[ ( df["prSM [db]"] == 1) & ( df["Station"] == "B2" ) ]
k0_station= df[ ( df["prSM [db]"] == 1) & ( df["Station"] == "K0" ) ]
m8_station= df[ ( df["prSM [db]"] == 1) & ( df["Station"] == "M8" ) ]
m14_station= df[ ( df["prSM [db]"] == 1) & ( df["Station"] == "M14" ) ]
m23_station= df[ ( df["prSM [db]"] == 1) & ( df["Station"] == "M23" ) ]
my2_station= df[ ( df["prSM [db]"] == 1) & ( df["Station"] == "MY2" ) ]

b2_years= b2_station["yyyy-mm-dd hh:mm:ss.sss"]
b2_temperature= b2_station["T(degC)"]

k0_years= k0_station["yyyy-mm-dd hh:mm:ss.sss"]
k0_temperature= k0_station["T(degC)"]

m8_years = m8_station["yyyy-mm-dd hh:mm:ss.sss"]
m8_temperature= m8_station["T(degC)"]

m14_years = m14_station["yyyy-mm-dd hh:mm:ss.sss"]
m14_temperature= m14_station["T(degC)"]

m23_years = m23_station["yyyy-mm-dd hh:mm:ss.sss"]
m23_temperature= m23_station["T(degC)"]

my2_years = my2_station["yyyy-mm-dd hh:mm:ss.sss"]
my2_temperature= my2_station["T(degC)"]

fig = plt.figure(figsize=(10,10))
axes = fig.add_axes([0.04,0.06,0.95,0.91])


axes.plot(b2_years,b2_temperature,"ro",label="B2")
axes.plot(k0_years,k0_temperature,"b^",label="K0")
axes.plot(m8_years,m8_temperature,"gs",label="M8")
axes.plot(m14_years,m14_temperature,"y+",label="M14")
axes.plot(m23_years,m23_temperature,"md",label="M23")
axes.plot(my2_years,my2_temperature,"c*",label="MY2")

axes.xaxis.set_major_locator(mdates.YearLocator(base=1))  #makes the year frequency 1
axes.xaxis.set_minor_locator(mdates.MonthLocator(interval=1)) #adds lines to months

axes.set_xlabel("Time")
axes.set_ylabel("Temperature")
axes.legend()

axes.xaxis.grid()
plt.show()
