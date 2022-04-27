from dash import Dash, dcc, html, Input, Output
from dash.html.Div import Div

app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(['NYC', 'MTL', 'SF'], 'NYC', id='select_project'),
    html.Div(id='dd-output-container')

])


@app.callback(
    Output('dd-output-container', 'children'),
    Input('select_project', 'value')
)
def update_output(value):
    if value == "SF":
        return html.Div("This shit!")
    if value == "MTL":
        return html.Div("That shit")
    if value == "NYC":
        return html.Div("Start shit")


if __name__ == '__main__':
    app.run_server(debug=True)