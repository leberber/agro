#.to_plotly_json()
from dash import Dash, dcc, html, Input, Output, ALL, Patch, callback, ctx, no_update, MATCH, State, clientside_callback, ClientsideFunction
import dash_mantine_components as dmc
import json
from dash_iconify import DashIconify


app = Dash(__name__, 
           suppress_callback_exceptions=True
           )

data= {
    'huile':{'1L':'140', '2L':'280', '5L':'500'},
    'sucre':{'1K':'40', '2K':'80', '5L':'150'},
     'tomate':{'1C':'40', '2C':'80'},
   
}

for i in range(0,10):
    data['huile'+str(i)] = {'1L':'140', '2L':'280', '5L':'500'}
print(data.__sizeof__())

article_card = []
for article, value in data.items():
    artile_type = []
    for article_type, value in value.items():
        artile_type.append(
            dmc.Grid(
                children=[
                    dmc.Col(dmc.Text(article_type,  id= f'name_{article}_{article_type}'), span=2,  className='item_type_column'),
                    dmc.Col(dmc.Text(f"{value} DA", id=f'price_{article}_{article_type}', className='price_test'), span=4,  className='item_type_column'),
                    dmc.Col(dmc.NumberInput( hideControls = True, value = 0, className='item_type_number_input', id=f'number_input_{article}_{article_type}'), span=2, className='item_type_column'),
                    dmc.Col(dmc.Text(f"{0} DA", id=f'sum_{article}_{article_type}', className='price_test'), span=4,  className='item_type_column'),
                ],
                justify="center",
                align="center",
                gutter="xl",
                className='item_type_grid'

            ),
    )
    article_card.append(
        dmc.Card(
            children=[
                dmc.CardSection(
                    dmc.Center(  dmc.Image(src=f"assets/huile.png", width = 200))
                  ,p = 30,
                ),
                dmc.Text(
                    [
                        dmc.Text(f"{article}",id = f'{article}', className='article_name'),
                    ],
                 
                ),
                dmc.Paper(artile_type),

            ],
            withBorder=True,
            shadow="sm",
            radius="md",
            style={"width": 396},
        )
    )

        
app.layout = html.Div(
    children=[
        dmc.ActionIcon(
            DashIconify(icon="material-symbols:garden-cart", width=20),
            size="lg",
            variant="filled",
            id="chart-icon",
            n_clicks=0,
            mb=10,
        ),
        html.Div(article_card),
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
    app.run_server(debug=True, host='0.0.0.0', port=8050, dev_tools_ui=False)

