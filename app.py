

from dash import Dash, dcc, html, Input, Output, State, ALL,  MATCH, callback, ctx, no_update,   clientside_callback, ClientsideFunction
from dash_iconify import DashIconify as icon
import dash_mantine_components as dmc

from appshell import  footer, header
from utils import id_dict
import pandas as pd
# from pages.shop import  shop

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
    ],
)

data = pd.read_csv('products.csv').tail(15)
data = data.to_dict('records')


def shop_card(product_name, product_code, product_price,  product_quantity, image_path):
    return dmc.Grid(
            className = 'card-grid',
            justify = 'center',
            children = [
                dmc.Col(
                className = 'card-image-column',
                p = 5,
                    span = 3,
                    children = [
                        dmc.ActionIcon(dmc.Image(src=image_path, className = 'card-image') , style = {'width':'100%', 'height':'100%'}, id={"type": "card_image_action", "index":product_code}) 
                    ]
                ),
                dmc.Col(
                    span = 'auto',
                    children = [
                        dmc.Grid(
                            children=[
                                dmc.Col(dmc.Text(product_name, size="lg", weight=500,), span=7, px = 0),
                                dmc.Col(dmc.Text(product_price, size="md", weight=900, align="right" , color = 'green',  id={"type": "card_item_price", "index":product_code}), span=5,  px = 0),
                            ],
                        ),
                        dmc.Grid(
                            justify = 'flex-end',
                            children=[
                                dmc.Col( 
                                span=4, px = 0,
                                    children =[
                                        dmc.Stack(
                                            align="center",
                                            children = [
                                                dmc.NumberInput(min=0, w = 50, h = 30, mih = 20, size = 'lg', hideControls =  True, className='card-quantity-input', value = product_quantity, id={"type": "card_item_quantity", "index": product_code}, placeholder=0),
                                                dmc.Text("Quantity", size="md", weight=600, align="right" ),

                                            ]
                                        ) 
                                    ]
                                ),
                                dmc.Col(    
                                    span=5, px = 0,
                                    children =[
                                        dmc.Stack(
                                            align="center",
                                            children = [
                                                dmc.Text(id={"type": "card_item_total", "index":product_code}, size="md", lh = '30px', weight='bolder'),
                                                dmc.Text("Total", size="md", weight=600, align="right" ),                                               

                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )


shop = dmc.Paper(
    id = id_dict('page_layout_id', 'shop'),
    style = {'display':'block'},
    className = 'page',

    children = [
        html.Div(id = 'filter_chips_container'),
        

        dmc.TextInput(
            id = 'search_item',
            size = 'md',
            placeholder="Search",
            rightSection=icon(icon="guidance:search"),
        ),
        dmc.Container(id = 'products_container'),




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
    m = 0,
    p = 0,
    id = id_dict('page_layout_id', 'cart'),
    style = {'display':'none'},
    className = 'page',
    children = [
            html.Div(id = 'cart-items')

    ]
)
content = dmc.Container(
    className = 'content',
    children = [
        shop,
        account,
        cart,
         dmc.Drawer(
            id="drawer-position",
            zIndex=10000,
            position = 'bottom',
            size="65%",
            withCloseButton=False
        ),
    ]
)
   
app.layout = html.Div(
    children=[  
        dmc.MantineProvider(
            id = 'theme',
            withGlobalStyles=True,
            children=[
                html.Div(
                    children = [
                        header,
                        content,
                        footer,
                dcc.Store(id = 'all_stored_products'),
                dcc.Store(id = 'items_pushed_to_cart', data = {}),
                dmc.Text(id='void'),
                    ]
                )
            ]
        ) 
    ]
)
@callback(
        Output('all_stored_products', 'data'),
        Output('filter_chips_container', 'children'),
        Input('void', 'children'))
def on_data_set_graph(void):

    filters = {
         "category": set(),
         "provider": set()
        }
    
    for item in data:
        filters["category"].add(item['category'])
        filters["provider"].add(item['provider'])
    filters["category"] =  list(filters["category"])
    filters["provider"] =  list(filters["provider"])

    chips_category  = dmc.ChipGroup(
                children = [
                     dmc.Chip(x, value=x, size = 'lg') for x in  filters["category"]
                ],
                multiple=True,
                value= filters["category"][0],
                id = 'product_category'
            )
    chips_provider  = dmc.ChipGroup(
                children = [
                     dmc.Chip(x, value=x, size = 'lg') for x in  filters["provider"]
                ],
                # multiple=True,
                id = 'product_povider',
                value= filters["provider"][0]
            )

    return data, html.Div([chips_category, chips_provider])


@app.callback(
        Output('products_container', 'children'),
        Input('product_povider', 'value'),
        State("items_pushed_to_cart", "data"),
        State("all_stored_products", "data"),
    )

def on_data_set_graph(product_povider, items_pushed_to_cart, _data):
    visible  = []
    hidden = []
    items_in_cart_and_filtered_data = []
    items_in_cart_not_in_filtered_data = []
    not_in_cart_and_filtered_data = []
    for item in _data:

        product_code = item['product_code']
        _product_provider = item['provider']
        if  product_code in items_pushed_to_cart and  _product_provider == product_povider:
            items_in_cart_and_filtered_data.append(item)
        elif product_code in items_pushed_to_cart and  _product_provider != product_povider:
            items_in_cart_not_in_filtered_data.append(item)
        elif product_code not in items_pushed_to_cart and  _product_provider == product_povider:
            not_in_cart_and_filtered_data.append(item)


    product_quantity = None
    for item in not_in_cart_and_filtered_data + items_in_cart_and_filtered_data:
        product_code = item['product_code']
        if item in items_in_cart_and_filtered_data:
            product_quantity = items_pushed_to_cart[item['product_code']]['item_quantity']

   
        visible.append(
                shop_card(
                    item['product_name'], 
                    product_code, 
                    item['price'],  
                    product_quantity, 
                    f'/assets/images/{product_code}.png',
                ),
            )
        
    for item in items_in_cart_not_in_filtered_data:
        product_quantity = items_pushed_to_cart[item['product_code']]['item_quantity']
        product_code = item['product_code']
        hidden.append(
                shop_card(
                    item['product_name'], 
                    product_code, 
                    item['price'],  
                    product_quantity, 
                    f'/assets/images/{product_code}.png',
                ),
            )

    return html.Div([html.Div(visible), html.Div(hidden,style = {'display':f'none'},)])

@app.callback(
        Output({"type": "card_item_total", "index": MATCH}, "children"), 
        Input({"type": "card_item_quantity", "index": MATCH}, "value"),
        State({"type": "card_item_price", "index": MATCH}, "children"))

def item_card_add_item(card_item_quantity, item_price):
    if  not card_item_quantity:
        card_item_quantity = 0

    return round(card_item_quantity*item_price, 2)
 

@app.callback(
        Output({"type": "cart_item_total", "index": MATCH}, "children"), 
        Input({"type": "card_item_quantity", "index": MATCH}, "value"),
        State({"type": "card_item_price", "index": MATCH}, "children"))

def item_card_add_item(card_item_quantity,item_price ):
    if  not card_item_quantity:
        card_item_quantity = 0
        
    return round(card_item_quantity*item_price, 2)

@app.callback(
        Output({"type": "cart_item_quantity", "index": MATCH}, "value"), 
        Output({"type": "card_item_quantity", "index": MATCH}, "value"), 
         
        Input({"type": "card_item_quantity", "index": MATCH}, "value"),
        Input({"type": "cart_item_quantity", "index": MATCH}, "value"),
        prevent_initial_call=True,
    )

def stored_items(card_item_quantity, cart_item_quantity):


    if ctx.triggered_id['type'] =='card_item_quantity':
        return  card_item_quantity, card_item_quantity

    elif ctx.triggered_id['type'] =='cart_item_quantity':
        return  cart_item_quantity, cart_item_quantity
        

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

clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='theme_switcher'
    ),
    Output("theme", "theme"),
    Output("theme_switcher", "children"),
    Input("theme_switcher", "n_clicks"),
)




@callback(
        Output("items_pushed_to_cart", "data"),
        Output('cart-items', 'children'),
        Input({"type": "card_item_quantity", "index": ALL}, "value"),
        Input({"type": "page_switcher_action", "index": ALL}, "n_clicks"),
        Input({"type": "x_out_from_cart", "index": ALL}, "n_clicks"),
        State("items_pushed_to_cart", "data"),
        prevent_initial_call=True,
)

def item_card_add_item(cart_click, x_click, card_item_quantity, items_pushed_to_cart):

    for item in ctx.inputs_list[0]:
        item_quantity = item.get("value")
        item_id = item['id']['index']
        if item_quantity: 
            items_pushed_to_cart[item_id] = {
                    'product_code':item_id,
                    'item_quantity': item_quantity,
                }
    if ctx.triggered_id['type'] == 'x_out_from_cart':
        items_pushed_to_cart[ctx.triggered_id['index']][ 'item_quantity'] = 0
    cart_items = []

    if ctx.triggered_id['type'] == 'card_item_quantity':
        return items_pushed_to_cart, no_update
    
    header =    dmc.Grid(
            m = 0,
            align ='center',
                children=[
                    dmc.Col(
                        span=2,
                        
                        children = [
                           dmc.Text('', className='cart-items-headers')
                        ]
                    ),
                    dmc.Col(
                        span=6,
                        children = [
                             dmc.Text('Produit', className='cart-items-headers')
                        ]
                    ),
                    dmc.Col(
                        span=2,
                        children = [
                             dmc.Text('Quantity', className='cart-items-headers')
                        ]
                    ),        
                    dmc.Col(
                        span=2,
                        children = [
                             dmc.Text('Total', className='cart-items-headers', ta = 'center')
                        ]
                    )

                ]
            )
    cart_items.append(header)
    for _, item in items_pushed_to_cart.items():
        product_code= item['product_code']
        product_quantity = item['item_quantity']
        if product_quantity ==0:
            style = {'display':'none'}
        else:
            style = {}
        cart_items.append(
            dmc.Grid(
              style=style,
            m = 0,
            align ='center',
                children=[
                    dmc.Col(
                        span=2,
                      
                        children = [
                            dmc.Image(src= f'/assets/images/{product_code}.png',  height = 30, fit = 'contain')  
                        ]
                    ),
                    dmc.Col(
                        span=6,
                        children = [
                            dmc.Text(product_code[:40], maw = 150, size = 'sm')
                        ]
                    ),
                    dmc.Col(
                        span=2,
                        children = [
                            dmc.NumberInput(id={"type": "cart_item_quantity", "index": item['product_code']}, value = product_quantity, hideControls =  True, className='cart-quantity-input'
                                            # min=0, w = 40, h = 30, mih = 20, size = 'sm',className='cart-quantity-input'
                                            )
                        ]
                    ),        
                    dmc.Col(
                        span=2,
                         pos = 'relative',
                        children = [
                            dmc.Text( 0, id={"type": "cart_item_total", "index":item['product_code']}, style = {'float':'right'}, 
                                     size = 'sm'),
                                   dmc.ActionIcon(
                                id={"type": "x_out_from_cart", "index":item['product_code']},
                                variant='transparent',  
                                pos = 'absolute',
                                top = '-10px',
                                right= '-10px',

                            
                                children = [
                                   icon(icon="ph:x-light", width=15),
                                ]
                            ),
                        ]
                    )

                ]
            )
        )

    print(items_pushed_to_cart)
    return items_pushed_to_cart, html.Div(cart_items)
    


@callback(
    Output("drawer-position", "opened"),
    Input({"type": "card_image_action", "index": ALL}, "n_clicks"),
    prevent_initial_call=True,
)
def toggle_drawer(n_clicks):
    if any(n_clicks):
        return True
    return False


if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8050 )

