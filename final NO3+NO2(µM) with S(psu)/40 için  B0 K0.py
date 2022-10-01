import numpy as np
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import itertools
from matplotlib.ticker import MultipleLocator

df=pd.read_excel("Julian_iski_data_python.xlsx")

lodos_list = df["lodos"].head(n=13)
poyraz_list = df["poyraz"].head(n=14)
tuna_list = df["tuna"].head(n=4)

df1=df # df1 b2 için olsun
       # df ise k0 için
df1 = df.loc[df["İstasyon"].isin(["B2"])]
df1 = df1.loc[( ( df["prSM [db]"] <40) & (df["prSM [db]"] >=35) ) ]

df = df.loc[df["İstasyon"].isin(["K0"])]
df = df.loc[ ( ( df["prSM [db]"] <=71 ) & ( df["prSM [db]"] >=65 ) ) ]


fig, axes = plt.subplots(nrows=2,ncols=1,dpi=250,gridspec_kw={'height_ratios': [3.5,1]})


sns.set(font_scale=0.75)
sns.lineplot(data=df1, x="new_years", y="NO3+NO2(µM)", hue="İstasyon",lw=0.65,legend=False,ax=axes[0],palette=["#e69138"])
sns.scatterplot(data=df1, x="new_years", y="NO3+NO2(µM)", hue="İstasyon",ax=axes[0],palette=["#e69138"])
sns.lineplot(data=df, x="new_years", y="NO3+NO2(µM)", hue="İstasyon",lw=0.65,legend=False,ax=axes[0])
sns.scatterplot(data=df, x="new_years", y="NO3+NO2(µM)", hue="İstasyon",style="İstasyon",ax=axes[0])


sns.lineplot(data=df1, x="new_years", y="S(psu)", hue="İstasyon",lw=0.65,legend=False,ax=axes[1],palette=["#e69138"])
sns.scatterplot(data=df1, x="new_years", y="S(psu)", hue="İstasyon",style="İstasyon",legend=False,ax=axes[1],s=5,palette=["#e69138"])
sns.lineplot(data=df, x="new_years", y="S(psu)", hue="İstasyon",lw=0.65,legend=False,ax=axes[1])
sns.scatterplot(data=df, x="new_years", y="S(psu)", hue="İstasyon",style="İstasyon",legend=False,ax=axes[1],s=5)

axes[0].xaxis.set_major_locator(mdates.YearLocator(1))
axes[0].xaxis.set_minor_locator(mdates.MonthLocator(interval=1))
axes[0].tick_params(which='minor', width=0.4)
axes[0].set_xlabel("Yıllar (Year)",size=8.5)
axes[0].set_ylabel("NO3+NO2(µM)")
axes[0].yaxis.set_major_locator(MultipleLocator(2))
axes[0].legend().set_title(None)

axes[1].xaxis.set_major_locator(mdates.YearLocator(1))
axes[1].xaxis.set_minor_locator(mdates.MonthLocator(interval=1))
max_value=df["S(psu)"].max()

axes[1].vlines(x=lodos_list,ymin=0,ymax=max_value, colors='black', linestyles="--",linewidth=0.5)
axes[1].vlines(x=poyraz_list,ymin=0,ymax=max_value, colors='red', linestyles="--",linewidth=0.5)
axes[1].vlines(x=tuna_list,ymin=0,ymax=max_value, colors='green', linestyles="--",linewidth=0.5)

axes[1].yaxis.set_major_locator(MultipleLocator(10))

axes[1].set_xlabel("Yıllar (Year)",size=8.5)
axes[1].set_ylabel("S(psu)")

axes[0].set_ylim([-0.3,17.5])
axes[1].set_ylim([16.5,40])


axes[0].grid(linewidth=0.1,linestyle="--")
axes[1].grid(linewidth=0.1,linestyle="--")

plt.show()
