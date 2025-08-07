import pandas as pd
import dash
from dash import dcc, html, Output, Input
import plotly.express as px

# Load processed data
df = pd.read_csv("output.csv", parse_dates=["date"])
df.sort_values("date", inplace=True)

# Available regions
regions = ['all', 'north', 'east', 'south', 'west']

# Start Dash app
app = dash.Dash(__name__)
app.title = "Soul Foods Sales Visualiser"

# App layout
app.layout = html.Div(style={'fontFamily': 'Arial', 'backgroundColor': '#f9f9f9', 'padding': '20px'}, children=[
    html.H1("Soul Foods Sales Visualiser", style={
        'textAlign': 'center',
        'color': '#003366',
        'paddingBottom': '20px'
    }),

    html.Div([
        html.Label("Select Region:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
        dcc.RadioItems(
            id='region-selector',
            options=[{'label': region.capitalize(), 'value': region} for region in regions],
            value='all',
            inline=True,
            style={'marginBottom': '20px'}
        ),
    ], style={'textAlign': 'center'}),

    dcc.Graph(id='sales-line-chart')
])

# Callback to update chart based on region selection
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(selected_region):
    filtered_df = df.copy()
    if selected_region != 'all':
        filtered_df = filtered_df[filtered_df['region'] == selected_region]

    fig = px.line(
        filtered_df,
        x='date',
        y='quantity',
        color='product',
        title=f"Sales Over Time - Region: {selected_region.capitalize()}",
        labels={'quantity': 'Units Sold', 'date': 'Date'}
    )

    fig.add_vline(
        x='2021-01-15',
        line_dash='dash',
        line_color='red',
        annotation_text='Price Increase',
        annotation_position='top left'
    )

    fig.update_layout({
        'plot_bgcolor': '#ffffff',
        'paper_bgcolor': '#ffffff',
        'font': {'color': '#333'},
    })

    return fig

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
