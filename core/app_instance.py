import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = 'Forex Analyzer Ultimate'
server = app.server