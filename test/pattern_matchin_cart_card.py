

from dash import Dash, Input, html, Output, MATCH, no_update, State,ctx, callback

app = Dash(__name__)

import dash_mantine_components as dmc

app.layout = dmc.SimpleGrid(
    cols=2,
    children=[
        html.Div(id = 'containier'),
        html.Div(id = "cart"),
    ]
)



data = [
        {'category': 'alimentation', 'provider': 'cevital', 'product_code': 'Vinaigrettes', 'product_name': 'Vinaigrettes', 'price': 234.92, 'product_image': 'https://www.cevital-agro-industrie.com/storage/2023/03/Vinaigrettes-1-1.jpg'},
    {'category': 'alimentation', 'provider': 'cevital', 'product_code': 'Sauce_Harissa_Elio', 'product_name': 'Sauce Harissa Elio', 'price': 122.69, 'product_image': 'https://www.cevital-agro-industrie.com/storage/2023/08/harissa-elio-min.jpg'}, 
    {'category': 'alimentation', 'provider': 'cevital', 'product_code': 'Huile_Spciale_Friture_FLEURIAL', 'product_name': 'Huile Spéciale Friture FLEURIAL', 'price': 167.35, 'product_image': 'https://www.cevital-agro-industrie.com/storage/2023/06/huile-friture.jpg'}, 
 ]


    
@app.callback(
        Output('containier', 'children'),
        Output('cart', 'children'),
        Input('containier', 'children')
     )


def on_data_set_graph(void):
    card = []
    cart = []
    for item in data:
        card.append(

            dmc.Group(
                children = [ 
                    dmc.Text(item['product_name'][:20], miw = 150), 
                    dmc.Text(item['price'], id={"type": "card_item_price", "index": item['product_code']}), 
                    dmc.NumberInput(id={"type": "card_item_quantity", "index": item['product_code']}),
                  
                    dmc.Text(0, id={"type": "card_item_total", "index": item['product_code']}),
                ]
            )
        )
        cart.append(
            dmc.Group(
                children = [ 
                    dmc.Text(item['product_name'][:20], miw = 150), 
                    dmc.Text(item['price']), 
                    dmc.NumberInput(id={"type": "cart_item_quantity", "index": item['product_code']}),
                    dmc.Text(0, id={"type": "cart_item_total", "index": item['product_code']})
                ]
            )
        )
    return card, cart

@app.callback(
        Output({"type": "card_item_total", "index": MATCH}, "children"), 

        Input({"type": "card_item_quantity", "index": MATCH}, "value"),
        State({"type": "card_item_price", "index": MATCH}, "children"), prevent_initial_call=True,)

def item_card_add_item(item_quantity,item_price ):
    return item_quantity*item_price


@callback(
        Output({"type": "cart_item_quantity", "index": MATCH}, "value"), 
        Output({"type": "card_item_quantity", "index": MATCH}, "value"), 
        Output({"type": "cart_item_total", "index": MATCH}, "children"),  
         
        Input({"type": "card_item_quantity", "index": MATCH}, "value"),
        Input({"type": "cart_item_quantity", "index": MATCH}, "value"),

        State({"type": "card_item_price", "index": MATCH}, "children"),
        prevent_initial_call=True,
    )

def stored_items(card_item_quantity, cart_item_quantity, item_price):

    if ctx.triggered_id['type'] =='card_item_quantity':
        if card_item_quantity:
            print(card_item_quantity)
            return  card_item_quantity, card_item_quantity, card_item_quantity*item_price

    elif ctx.triggered_id['type'] =='cart_item_quantity':
        if cart_item_quantity:
            return  cart_item_quantity, cart_item_quantity, cart_item_quantity*item_price
        
    return cart_item_quantity, 0,0

    
if __name__ == '__main__':
    app.run_server(debug=True)