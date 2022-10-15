import pandas as pd
import plotly.express as px
import pandasql as ps

df = pd.read_csv('output3.csv')
#query = ps.sqldf(
 #   "select count, latitude, longitude "
#)

#print(query)
fig = px.density_mapbox(df, lat='latitude', lon='longitude', radius=10,
                        center=dict(lat=30.3, lon=-97.8), zoom=8.5, hover_name = 'count',
                        mapbox_style='stamen-terrain')
fig.show()