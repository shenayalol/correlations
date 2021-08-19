import pandas as pd
import plotly.express as px 
import numpy as np
df = pd.read_csv("sizeOfTvVersusWatching.csv")
fig = px.scatter(df, x = 'Size of TV', y="\tAverage time spent watching TV in a week (hours)")

fig.show()

df = pd.read_csv("sizeOfTvVersusWatching.csv")
x = df["Size of TV"].tolist()
y = df["\tAverage time spent watching TV in a week (hours)"].tolist()
print(x)
print(y)
t = np.corrcoef(x,y)
print(t[0,1])