import numpy as np
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import itertools
from matplotlib.ticker import MultipleLocator

df=pd.read_excel("Julian_iski_data_python.xlsx")

lodos_list = df["lodos"].head(n=13) #lodos_list sütunundaki ilk 13 index değerini listeye attık
poyraz_list = df["poyraz"].head(n=14)
tuna_list = df["tuna"].head(n=4)

#df = df[["prSM [db]", "İstasyon", "year", "ChlA","S(psu)","NO3+NO2(µM)","Si(µM)","PO4(µM)","lodos"]] #belli columnları alır
df = df.loc[( df["prSM [db]"] <=1)] # df=df [df["prSM [db]"] <= 1] ile aynı şey... (db si 1 eşit ve kücük olan bütün sütunlar alır)
df = df.loc[df["İstasyon"].isin(["B2","K0"])] #hangi istansyonları ayıklıyoruz..

# """ BELLİ BİR DEĞERİ ALMAK İÇİN """
#sadece m8 alıcaksak mesela şöyle yapabiliriz: (istasyonu m8 olan bütün columları alır)
#df = df.loc[df["Station"].isin(["M8"])] ,,,,,, df = df[ ( df["Station"] == "M8") ] ile yanı

#sns.set_style("whitegrid", {'grid.linestyle': '--'})

fig, axes = plt.subplots(nrows=2,ncols=1,dpi=250,gridspec_kw={'height_ratios': [3.5,1]})
#dpi=250 --> ekrana yakıslastırdı (büyülttü) ,,, gridspec_kw={'height_ratios': [4,1]}) --> üstteki axes , alttakinin 4 katı

sns.set(font_scale=0.75) #legend ' te yazan b2,k0 gibi istasyon yazılarının boyutunu ayarlar

sns.lineplot(data=df, x="new_years", y="NO3+NO2(µM)", hue="İstasyon",lw=0.65,legend=False,ax=axes[0])
sns.scatterplot(data=df, x="new_years", y="NO3+NO2(µM)", hue="İstasyon",style="İstasyon",ax=axes[0])

sns.lineplot(data=df, x="new_years", y="S(psu)", hue="İstasyon",lw=0.65,legend=False,ax=axes[1])
sns.scatterplot(data=df, x="new_years", y="S(psu)", hue="İstasyon",style="İstasyon",legend=False,ax=axes[1],s=5)

axes[0].xaxis.set_major_locator(mdates.YearLocator(1)) #yılları 1 yıl farkla aldık
axes[0].xaxis.set_minor_locator(mdates.MonthLocator(interval=1)) #yılların arasına ayları gösteren çizgiler ekler
axes[0].tick_params(which='minor', width=0.4) # minor'un genisligi
axes[0].set_xlabel("Yıllar (Year)",size=8.5)
axes[0].set_ylabel("NO3+NO2(µM)")
axes[0].yaxis.set_major_locator(MultipleLocator(2)) # from matplotlib.ticker import MultipleLocator ettikten sonra bunu yaparsan y eksenindeki değerleri 2 aralıklarla alır
axes[0].legend().set_title(None)

axes[1].xaxis.set_major_locator(mdates.YearLocator(1))
axes[1].xaxis.set_minor_locator(mdates.MonthLocator(interval=1))

max_value=df["S(psu)"].max() #S(psu) sütunundaki max değeri aldık, aşağıda kullanacağız

axes[1].vlines(x=lodos_list,ymin=0,ymax=max_value, colors='black', linestyles="--",linewidth=0.5) #x eksenindeki değerler ile , lodos_listte aynı değer varsa vertical line atar
axes[1].vlines(x=poyraz_list,ymin=0,ymax=max_value, colors='red', linestyles="--",linewidth=0.5)
axes[1].vlines(x=tuna_list,ymin=0,ymax=max_value, colors='green', linestyles="--",linewidth=0.5)

axes[1].yaxis.set_major_locator(MultipleLocator(5))

axes[1].set_xlabel("Yıllar (Year)",size=8.5)
axes[1].set_ylabel("S(psu)")

axes[0].set_ylim([-0.3,12]) #limitleme
axes[1].set_ylim([14.3,25])

axes[0].grid(linewidth=0.1,linestyle="--")
axes[1].grid(linewidth=0.1,linestyle="--")

plt.show()


