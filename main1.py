from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import pandasql as ps

# Load the dataset
df = pd.read_csv('output2.csv')
query = ps.sqldf(
    "select district, loc_count, count(loc_count) as count_no_crimes_2016 from df group by loc_count, district")
print(query)
# Create the Dash app
app = Dash()

# Set up the app layout
geo_dropdown = dcc.Dropdown(options=query['district'].unique(),
                            value='UK')

app.layout = html.Div(children=[
    html.H1(children='Dashboard'),
    geo_dropdown,
    dcc.Graph(id='crime-graph 2')
])


# Set up the callback function
@app.callback(
    Output(component_id='crime-graph 2', component_property='figure'),
    Input(component_id=geo_dropdown, component_property='value')
)
def update_graph(selected_geography):

    df.loc[df['loc_count'] > 2.e6, 'district'] = 'Other district'
    fig = px.pie(df, values='loc_count', names='district', title='High risk districts')
    fig.show()
    return fig


# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)