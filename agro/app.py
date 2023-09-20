

from dash import Dash, dcc, html, Input, Output, State, ALL,  MATCH, callback, ctx, no_update,   clientside_callback, ClientsideFunction
from dash_iconify import DashIconify as icon
import dash_mantine_components as dmc

from simple_callbacks import paper, footer, header

app = Dash(
    __name__,
    external_stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
    ],
)

app.layout = html.Div(
    style={"height": 930, "width": 450, 'border': '2px solid red', 'overflow':'scroll'},
    children=[  
        html.Div(
            className = 'content',
            children = [
                dmc.MantineProvider(
                    theme={"primaryColor": "indigo"},
                    id = 'theme',
                    withGlobalStyles=True,
                    children=[
                        html.Div(
                            children = [
                                header,
                                paper,
                                footer
                            ]
                        )
                    ]
                ) 
            ]
        ),
    ]
)

# print(icon(icon="iconamoon:mode-light-light", width=20).to_plotly_json())

clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='switch_them_icon'
    ),
    Output("theme", "theme"),
    Output("theme_switcher", "children"),
    Input("theme_switcher", "n_clicks"),
    prevent_initial_call=True
)


if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8050 )

