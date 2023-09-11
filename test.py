


from dash import html, Output, Input, Dash, no_update, dcc
import json
import time
import dash_mantine_components as dmc

app = Dash(__name__)
app.layout = html.Div(
    [
        html.Button('testing', 'testing'),
        html.Div(id='test'),
        dcc.Store(id = 'store', data=[
    "gray",
    "red",
    "pink",
    "grape",
    "violet",
    "indigo",
    "blue",
    "lime",
    "yellow",
    "orange",
])
    ]
)

sample = dmc.SimpleGrid(
    cols=3,
    className = 'test',
    children=[
        html.Div("1").to_plotly_json(),
        html.Div("2").to_plotly_json(),

    ]
).to_plotly_json()


b =     dmc.Group(
            position="center",
        ).to_plotly_json()
print(b)


d = html.Div("test").to_plotly_json()

app.clientside_callback(
    """function (n, data) {
    var arr = [];

    data.forEach((element) => arr.push(
{'props': {'children': element, 'color': element}, 'type': 'Badge', 'namespace': 'dash_mantine_components'}
    ));

        if (n) {
       
        
            return {'props': {'children': arr, 'position': 'center'}, 'type': 'Group', 'namespace': 'dash_mantine_components'}
        }
        
        return window.dash_clientside.no_update
    }""",
    Output("test", "children"), Input("testing", "n_clicks"), Input("store", "data"), 
)



if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8010)


