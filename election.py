import dash  # version 1.13.1
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, ALL, State, MATCH, ALLSMALLER
import plotly.express as px
import pandas as pd
import numpy as np
app = dash.Dash()

app.layout = html.Div([
    html.H1('Sam Analytics'),
    html.Iframe(id='map', srcDoc=open('Rani_Parties.html', 'r').read(), width='100%', height='600'),
    html.Button(id='map-submit-button', n_clicks=0, children='Submit')
])


@app.callback(
    dash.dependencies.Output('map', 'srcDoc'),
    [dash.dependencies.Input('map-submit-button', 'n_clicks')])
def update_map(n_clicks):
    if n_clicks is None:
        return dash.no_update
    else:
        return open('Rani_Parties.html', 'r').read()
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
