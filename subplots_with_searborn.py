import numpy as np
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import itertools

df=pd.read_excel("Julian_iski_data_python.xlsx")

new_year_list = df["new_year"].head(n=10) #new year sütunundaki ilk 10 index değerini listeye attık

"""
print(new_year_list) 
output:
0   1996-09-24
1   1996-11-28
2   1999-11-15
3   1999-12-15
4   2000-01-19
5   2002-10-23
6   2003-10-22
7   2004-01-21
8   2006-03-03
9   2007-10-24

"""

df = df[["prSM [db]", "Station", "yyyy-mm-dd hh:mm:ss.sss", "ChlA","S(psu)","NO3+NO2(µM)","Si(µM)","PO4(µM)","new_year"]] #belli columnları alır
df = df.loc[( df["prSM [db]"] ==1)] # df=df [df["prSM [db]"] == 1] ile aynı şey. (db si 1 olan bütün sütunlar alır)
df = df.loc[df["Station"].isin(["M8", "M14", "M23", "MY2"])] #hangi istansyonları ayıklıyoruz..

# """ BELLİ BİR DEĞERİ ALMAK İÇİN """
#sadece m8 alıcaksak mesela şöyle yapabiliriz: (istasyonu m8 olan bütün columları alır)
#df = df.loc[df["Station"].isin(["M8"])] ,,,,,, df = df[ ( df["Station"] == "M8") ] ile yanı

sns.set_style("whitegrid", {'grid.linestyle': '--'})
fig, axes = plt.subplots(nrows=2,ncols=1,dpi=250,gridspec_kw={'height_ratios': [3.5,1]}) #bu sefer subplots ile aldık çünkü birden fazla graph basacağız
#dpi=250 --> ekrana yakıslastırdı (büyülttü) ,,, gridspec_kw={'height_ratios': [4,1]}) --> üstteki axes , alttakinin 4 katı
sns.set(font_scale=0.75) #legendlerin yazı boyutunu ayarlar

sns.lineplot(data=df, x="yyyy-mm-dd hh:mm:ss.sss", y="NO3+NO2(µM)", hue="Station",lw=0.65,legend=False,ax=axes[0]) #subplots yapınca ax= diye hangisi oldugunu belirt
sns.scatterplot(data=df, x="yyyy-mm-dd hh:mm:ss.sss", y="NO3+NO2(µM)", hue="Station",style="Station",ax=axes[0])

axes[0].xaxis.set_major_locator(mdates.YearLocator(1)) #yılları 1 yıl farkla aldık
axes[0].xaxis.set_minor_locator(mdates.MonthLocator(interval=1)) #aylara  ekler
axes[0].set_xlabel("Yıllar (Year)",size=8.5)
axes[0].set_ylabel("NO3+NO2(µM)")


sns.lineplot(data=df, x="yyyy-mm-dd hh:mm:ss.sss", y="Station", hue="Station",lw=0.65,legend=False,ax=axes[1])
sns.scatterplot(data=df, x="yyyy-mm-dd hh:mm:ss.sss", y="Station", hue="Station",style="Station",legend=False,ax=axes[1],s=5) # s= yaparak scatterların boyutunu belirle

axes[1].xaxis.set_major_locator(mdates.YearLocator(1)) #yılları 1 yıl farkla aldık
axes[1].xaxis.set_minor_locator(mdates.MonthLocator(interval=1)) #aylara çizgi ekler
axes[1].set_xlabel("Yıllar (Year)",size=8.5)
axes[1].set_ylabel("S(psu)")

max_value=df["S(psu)"].max() #S(psu) sütunundaki max değeri aldık, aşağıda kullanacağız
axes[1].vlines(x=new_year_list,ymin=0,ymax=max_value, colors='black', linestyles="--",linewidth=0.5)
#vlines ile , x= kısmındaki datalar ile sns.lineplot daki x="year" datalarını karşılaştırıyoruz, eğer aynı varsa çizgi atar

plt.show()
