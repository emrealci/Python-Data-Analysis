import numpy as np
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import itertools
from statistics import stdev
liste=[]
df = pd.read_excel("Julian_iski_data_python.xlsx")
df = df[["Station", "Julian", "ChlA","Cruise","prSM [db]","yyyy-mm-dd hh:mm:ss.sss"]]
df = df.loc[df["Station"].isin(["B2"])]

df= df[df['ChlA'] == df.groupby(['Cruise'])['ChlA'].transform(max)]
#aynı değerdeki "Cruise" değerlerinden max Klorofil - a değerini bulduk
#daha sonra bu max Klorofil -a değerlerinin olduğu diğer sütunları da depoladık.

print(df)

fig = plt.figure(figsize=(10,10))
axes = fig.add_axes([0.04,0.06,0.95,0.91])

sns.scatterplot(data=df, x="yyyy-mm-dd hh:mm:ss.sss", y="ChlA", hue="prSM [db]",style="Cruise")
plt.show()
