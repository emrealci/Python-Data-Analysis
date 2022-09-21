import numpy as np
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import itertools

df=pd.read_excel("Julian_iski_data_python.xlsx")

"""
searborn ve matplotlib kullanım farkına dikkat et, hangi şartlarda hangisi seçileceğine karar ver
"""

df = df[["prSM [db]", "Station", "yyyy-mm-dd hh:mm:ss.sss", "T(degC)"]] #belli columnları alır 
df = df.loc[df["prSM [db]"] == 1] # df=df [df["prSM [db]"] == 1] ile aynı şey. (db si 1 olan bütün sütunlar alır)
df = df.loc[df["Station"].isin(["B2", "K0", "M8", "M14", "M23", "MY2"])] #hangi istansyonları ayıklıyoruz..

# """ BELLİ BİR DEĞERİ ALMAK İÇİN """
#sadece m8 alıcaksak mesela şöyle yapabiliriz: (istasyonu m8 olan bütün columları alır)
#df = df.loc[df["Station"].isin(["M8"])] ,,,,,, df = df[ ( df["Station"] == "M8") ] ile yanı

fig = plt.figure(figsize=(10,10))
axes = fig.add_axes([0.04,0.06,0.95,0.91])

sns.scatterplot(data=df, x="yyyy-mm-dd hh:mm:ss.sss", y="T(degC)", hue="Station",style="Station")
axes.xaxis.set_major_locator(mdates.YearLocator(1)) #yılları 1 yıl farkla aldık
axes.xaxis.set_minor_locator(mdates.MonthLocator(interval=1)) #aylara çizgi ekler
axes.set_xlabel("Time")
axes.set_ylabel("Temperature")
axes.grid()
plt.show()
