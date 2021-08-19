import pandas as pd
import plotly.express as px 
import numpy as np
df = pd.read_csv("marksVersusPresenties.csv")
fig = px.scatter(df, x = 'Days Present', y="Marks In Percentage")

fig.show()

x = df["Days Present"].tolist()
y = df["Marks In Percentage"].tolist()
print(x)
print(y)
t = np.corrcoef(x,y)
print(t[0,1])