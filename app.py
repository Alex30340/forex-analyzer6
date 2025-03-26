from core.app_instance import app
from pages import analyse, dashboard, education, backtest
from dash import html, dcc
from dash.dependencies import Input, Output

app.layout = html.Div([
    dcc.Location(id='url'),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/dashboard':
        return dashboard.layout
    elif pathname == '/backtest':
        return backtest.layout
    elif pathname == '/education':
        return education.layout
    else:
        return analyse.layout

if __name__ == '__main__':
    app.run_server(debug=False, host="0.0.0.0", port=8080)
