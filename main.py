from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly
import plotly.express as px
import pandasql as ps


# Load the dataset
df = pd.read_csv('output.csv')
query = ps.sqldf("select year, primary_type, count(primary_type) as count_major_crime from df group by year, primary_type")
print(query)
# Create the Dash app
app = Dash()

# Set up the app layout
geo_dropdown = dcc.Dropdown(options=query['year'].unique(),
                            value='2016')

app.layout = html.Div(children=[
    html.H1(children='Dashboard'),
    geo_dropdown,
    dcc.Graph(id='crime-graph')
])


# Set up the callback function
@app.callback(
    Output(component_id='crime-graph', component_property='figure'),
    Input(component_id=geo_dropdown, component_property='value')
)
def update_graph(selected_geography):
    filtered_crime = query[query['year'] == selected_geography]
    line_fig = px.bar(filtered_crime,
                       x='primary_type', y='year',
                       color='primary_type',
                       title=f'crimes in {selected_geography}')
    return line_fig


# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)