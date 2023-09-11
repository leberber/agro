
from dash import Dash, dcc, html, Input, Output, ALL, Patch, callback, ctx, no_update, MATCH, State, clientside_callback
import dash_mantine_components as dmc
import json
from dash_iconify import DashIconify


app = Dash(__name__)

data= {
    'huile':{'1L':'140', '2L':'280', '5L':'500'},
    'sucre':{'1K':'40', '2K':'80', '5L':'150'},
   
}
# dmc.Paper(artile_type, style= {'border':'3px solid red'}) id={'type': 'articled','index': key},
article_card = []
for article, value in data.items():
    artile_type = []
    for article_type, value in value.items():
        artile_type.append(
            dmc.Grid(
                children=[
                    dmc.Col(dmc.Text(article_type,  id= f'name_{article}_{article_type}'), span=3,  className='item_type_column'),
                    dmc.Col(dmc.Text(value, id=f'price_{article}_{article_type}'), span=3,  className='item_type_column'),
                    dmc.Col(dmc.NumberInput( hideControls = True, value = 0, className='item_type_number_input', id=f'number_input_{article}_{article_type}'), span=3, className='item_type_column'),
                    
                    dmc.Col(dmc.Text(0, id=f'sum_{article}_{article_type}'), span=3,  className='item_type_column'),
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
                    dmc.Image(
                        src=f"assets/{article}.png",
                    )
                ),
                dmc.Group(
                    [
                        dmc.Text(f"{article}",id = f'{article}', weight=500),
                        dmc.Badge("On Sale", color="red", variant="light"),
                    ],
                    position="apart",
                    mt="md",
                    mb="xs",
                ),
                dmc.Paper(artile_type, ),

                dmc.Button(
                    "Add to Cart",
                    variant="light",
                    color="blue",
                    fullWidth=True,
                    mt="md",
                    radius="md",
                ),
            ],
            withBorder=True,
            shadow="sm",
            radius="md",
            style={"width": 396},
        )
    )


        
app.layout = html.Div(
    children=[
#             dmc.ActionIcon(
#             DashIconify(icon="material-symbols:garden-cart", width=20),
#             size="lg",
#             variant="filled",
#             id="chart-icon",
#             n_clicks=0,
#             mb=10,
#         ),
#        html.Div(article_card),
#        dcc.Store(id = 'items-in-chart', data = {}),
#     dmc.Modal(
#             title="Cart",
#             size="55%",
#             id="cart-modal",
#             zIndex=10000,
#             children=[
                
#                 dmc.Text("here all the items saved to cart"),
#                 dmc.Prism(
#     children =""" # """,
#     id = 'cart-items',
#     language="python",
#     colorScheme="dark",
# ),
#             ],
#         ),
        dmc.Button( 'button1', id = 'bt_1'), 
        dmc.Button( 'button2', id = 'bt_2'), 
        html.Div( 'div1',id = 'div_1'), 
        html.Div( 'div2',id = 'div_2'), 

    ]  
)

# for id in ['1','2']:
#     @callback(
#         Output(f"div_{id}", "children"),
#         Input(f"bt_{id}", "n_clicks"),
#         prevent_initial_call=True,
#     )
#     def view_cart(value):
#         return value


for id in ['1','2']:
    clientside_callback(
            """function (value) {
            return value
            }""",
            Output(f"div_{id}", "children"),
            Input(f"bt_{id}", "n_clicks"),
            prevent_initial_call=True,
        )

# clientside_callback(
#     """function (value) {
#     return value
#     }""",
#     Output(f"div_1", "children"),
#     Input(f"bt_1", "n_clicks"),
#     prevent_initial_call=True,
# )


# @callback(
#     Output("cart-items", "children"),
#     Input("items-in-chart", "data"),
#     prevent_initial_call=True,
# )
# def view_cart(value):
#     return json.dumps(value, indent=4)

# @callback(
#     Output("cart-modal", "opened"),
#     Input("chart-icon", "n_clicks"),
#     State("cart-modal", "opened"),
#     prevent_initial_call=True,
# )
# def modal_demo(nc3, opened):
#     return not opened

# def product_calls(article, article_type):
#     @callback(
#         Output('items-in-chart','data', allow_duplicate=True),
#         Output( f'sum_{article}_{article_type}', 'children'),
#         State( f'{article}', 'children'),
#         State( f'name_{article}_{article_type}', 'children'),
#         State( f'price_{article}_{article_type}', 'children'),
#         Input( f'number_input_{article}_{article_type}', 'value'),
#         State('items-in-chart', 'data'),
        
#         prevent_initial_call =True

#     )

#     def store_item_in_chart(artile, article_type, price, number_input, data):
#         if not number_input:
#             print('empy')
#             return no_update
#         # if number_input is None:
#         #     print('this is none')
#         #     return no_update

#         print(artile, article_type, price, 'input', str(number_input), type(number_input))
#         data[artile]={'article_type':article_type, 'article_price':price, 'item_quantity': number_input}
#         print('-----')
#         return data, int(price) * number_input
    
# def product_calls(article, article_type):
#     clientside_callback(
#         """function (n, data) {
#         var arr = [];

#         data.forEach((element) => arr.push(
#     {'props': {'children': element, 'color': element}, 'type': 'Badge', 'namespace': 'dash_mantine_components'}
#         ));

#             if (n) {
        
            
#                 return {'props': {'children': arr, 'position': 'center'}, 'type': 'Group', 'namespace': 'dash_mantine_components'}
#             }
            
#             return window.dash_clientside.no_update
#         }""",
#         Output("test", "children"), Input("testing", "n_clicks"), Input("store", "data"), 
#     )






# for article, value in data.items():
#     for article_type, value in value.items():
#         product_calls(article, article_type)


    


if __name__ == "__main__":
    app.run(app.run_server(debug=True, host='0.0.0.0', port=8050))

