#.to_plotly_json()
from dash import Dash, dcc, html, Input, Output, ALL, Patch, callback, ctx, no_update, MATCH, State, clientside_callback, ClientsideFunction
import dash_mantine_components as dmc
import json
from dash_iconify import DashIconify

import random


app = Dash(__name__, 
           suppress_callback_exceptions=True
           )

data= {
    'sucre':{'1K':'40', '2K':'80', '5L':'150'},
    'huile':{'1L':'140', '2L':'280', '5L':'500'},
    # 'sucre':{'1K':'40', '2K':'80', '5L':'150'},
    #  'tomate':{'1C':'40', '2C':'80'},
   
}

for i in range(0,50):
    s = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    data[str(s)+'huile'+str(i)] = {'1L':'140', '2L':'280', '5L':'500'}
print(json.dumps(data, indent=4))
# print(data.__sizeof__())

# print(dmc.TextInput(label="Your Email:", style={"width": 200}).to_plotly_json())
        
app.layout = html.Div(
    children=[
        dcc.Store(id = 'store_items_data'),
             dmc.ActionIcon(
            DashIconify(icon="material-symbols:garden-cart", width=20),
            size="lg",
            variant="filled",
            id="chart-icon",
            n_clicks=0,
            mb=10,
        ),
        dmc.Text(id='void'),
             dmc.TextInput(
                 id = 'search_item',
            style={"width": 380},
            placeholder="Search",
            rightSection=DashIconify(icon="guidance:search"),
        ),
   
        html.Div(id ='test_store'),
       dcc.Store(id = 'items-in-chart', data = {}),
        dmc.Modal(
            size="55%",
            id="cart-modal",
            zIndex=10000,
            children=[
                html.Div( id = 'cart-items'),
            ],
        ),
    ]  
)
@callback(
        Output('store_items_data', 'data'),
        Input('void', 'children'))
def on_data_set_graph(void):
    return data


app.clientside_callback(
     ClientsideFunction(
        namespace='clientside',
        function_name='show_dcc_stored_items'
    ),
    Output("test_store", "children"),
    Input("store_items_data", "data"),
    Input("search_item", "value"),
    

)
    
    
app.clientside_callback(
     ClientsideFunction(
        namespace='clientside',
        function_name='show_cart_items'
    ),
    Output("cart-items", "children"),
    Input("items-in-chart", "data"),
    prevent_initial_call=True,

)



@callback(
    Output("cart-modal", "opened"),
    Input("chart-icon", "n_clicks"),
    State("cart-modal", "opened"),
    prevent_initial_call=True,
)
def modal_demo(nc3, opened):
    return not opened

        
def product_calls(article, article_type):
    clientside_callback(
     ClientsideFunction(
        namespace='clientside',
        function_name='update_cart_itmes'
    ),
        Output('items-in-chart','data', allow_duplicate=True),
        Output( f'sum_{article}_{article_type}', 'children'),
       
        Input( f'number_input_{article}_{article_type}', 'value'),

        State( f'{article}', 'children'),
        State( f'name_{article}_{article_type}', 'children'),
        State( f'price_{article}_{article_type}', 'children'),
        State('items-in-chart', 'data'),
        prevent_initial_call =True
    )

for article, value in data.items():
    for article_type, value in value.items():
        product_calls(article, article_type)





def product_calls_nested(article, article_type):
    @callback(
        Output(f'number_input_{article}_{article_type}', 'value'),
        Input(f"{article}_{article_type}", "value"),
        prevent_initial_call=True,
    )
    def view_cart_(value):
        return value
    
for article, value in data.items():
    for article_type, value in value.items():
        product_calls_nested(article, article_type)

if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8050, 
                #    dev_tools_ui=False
                   )

