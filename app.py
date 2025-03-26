import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dcc.Location(id='url'),
    dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8080)
