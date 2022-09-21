import numpy as np
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import itertools
from statistics import stdev

df = pd.read_excel("Julian_iski_data_python.xlsx")

liste_mean=[]
liste_sayi=[]
liste_standart_dev=[]

for i in range(1,13):
    df = df[["prSM [db]", "Station", "yyyy-mm-dd hh:mm:ss.sss","ChlA"]]
    df = df.loc[df["prSM [db]"] <= 1]
    df = df.loc[df["Station"].isin(["MY2"])] 

    a=pd.DatetimeIndex(df['yyyy-mm-dd hh:mm:ss.sss']).month==(i) #ayları aldık

    df2= df.loc[a==True]

    mean=df2["ChlA"].mean()
    sayi=df2["ChlA"].count()
    standart_dev=df2["ChlA"].std()
    liste_mean.append(mean) #ortalamaları ekle
    liste_sayi.append(sayi) #toplam sayı
    liste_standart_dev.append(standart_dev) #standart sapmaları ekle

df3 = pd.read_excel("B2_station.xlsx")
df3["MY2_mean"]=liste_mean
df3["MY2_count"]=liste_sayi
df3["MY2_Standart Deviation"]=liste_standart_dev
df3.to_excel("B2_station.xlsx")

