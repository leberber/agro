

from dash import Dash, dcc, html, Input, Output, State, ALL,  MATCH, callback, ctx, no_update,   clientside_callback, ClientsideFunction
from dash_iconify import DashIconify as icon
import dash_mantine_components as dmc

from appshell import  footer, header
from utils import id_dict
# from pages.shop import  shop

app = Dash(
    __name__,
    external_stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
    ],
)
shop = dmc.Paper(
    id = id_dict('page_layout_id', 'shop'),
    style = {'display':'block'},
    className = 'page',
    children = [
        dmc.Text("shop_page", size="md", color ='red'),
        dmc.Text("shop_page", size="md"),
        dmc.Text("Dshop_page", size="md"),
        dmc.Text("Default text", size="md"),
        dmc.Text("Default text", size="md"),
    ]
)

account = dmc.Paper(
    id = id_dict('page_layout_id', 'account'),
    className = 'page',
    style = {'display':'none'},
    children = [
        dmc.Text("account_page", size="md", color ='yellow'),
        dmc.Text("account_page", size="md"),
        dmc.Text("account_page", size="md"),
        dmc.Text("Default text", size="md"),
        dmc.Text("Default text", size="md"),
    ]
)

cart = dmc.Paper(
    id = id_dict('page_layout_id', 'cart'),
    style = {'display':'none'},
    className = 'page',
    children = [
        dmc.Text("cart_page", size="md", color ='blue'),
        dmc.Text("cart_page", size="md"),
        dmc.Text("cart_page", size="md"),
        dmc.Text("Default text", size="md"),
        dmc.Text("Default text", size="md"),

    ]
)
content = dmc.Container(
    className = 'content',
    children = [
        shop,
        account,
        cart,
    ]
)
   
app.layout = html.Div(
    style={"height": 930, "width": 450, 'border': '2px solid red', 'overflow':'scroll'},
    children=[  
        dmc.MantineProvider(
            theme={"primaryColor": "indigo"},
            id = 'theme',
            withGlobalStyles=True,
            children=[
                html.Div(
                    children = [
                        header,
                        content,
                        footer
                    ]
                )
            ]
        ) 
    ]
)


clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='page_switcher'
    ),
    Output({"type": "page_layout_id", "index": ALL}, "style"), 
    Output({"type": "page_switcher_action", "index": ALL}, "style"),
    Output({"type": "page_switcher_action_text", "index": ALL}, "style"),
    Input({"type": "page_switcher_action", "index": ALL}, "n_clicks"),
    prevent_initial_call=True
)


# print(icon(icon="iconamoon:mode-light-light", width=20).to_plotly_json())

clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='theme_switcher'
    ),
    Output("theme", "theme"),
    Output("theme_switcher", "children"),
    # Output("papertest", "className"),
    Input("theme_switcher", "n_clicks"),
    prevent_initial_call=True
)

# clientside_callback(
#     ClientsideFunction(
#         namespace='clientside',
#         function_name='page_switcher'
#     ),
#     Output("shop_page", "style"),
#     Output("account_page", "style"),
#     Output("cart_page", "style"),
#     Input("theme_switcher", "n_clicks"),
#     prevent_initial_call=True
# )


if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8050 )

