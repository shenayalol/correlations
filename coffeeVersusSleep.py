import pandas as pd
import plotly.express as px 
import numpy as np
df = pd.read_csv("coffeeVersusSleep.csv")
fig = px.scatter(df, x = 'Coffee in ml', y="sleep in hours")

fig.show()

x = df["Coffee in ml"].tolist()
y = df["sleep in hours"].tolist()
print(x)
print(y)
t = np.corrcoef(x,y)
print(t[0,1])