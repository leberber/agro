from dash import Dash, Input, html, Output, MATCH, no_update, State, dcc, ALL, ctx, callback

app = Dash(__name__)
import dash_mantine_components as dmc

app.layout = html.Div(
    children = [
        dmc.ChipGroup(
    [dmc.Chip(x, value=x) for x in ["leBerber",'cevital']],
    value="leBerber",
    id = 'product_povider'
),
         dcc.Store(id='items_pushed_to_cart', data = {}),

             html.Div(  id = 'datastored'),



             dmc.SimpleGrid(
    cols=2,
    children=[
        html.Div(id = 'containier'),
        html.Div(id = "cart"),
    ]
)
    ]

      )



def item_card(product_code, product_name, product_price, product_quantity, visibility ):


    return dmc.Group(
            children=[
               dmc.Text(product_name, miw = 150),
            dmc.Text(product_price, id={"type": "card_item_price", "index":product_code}),
             dmc.NumberInput(id={"type": "card_item_quantity", "index": product_code}, value = product_quantity, min=0,),
              dmc.Text( id={"type": "card_item_total", "index":product_code}) 
            
            ],
            style = {'visibility':f'{visibility}'}
         

)


data = [
    {'category': 'alimentation', 'provider': 'cevital', 'product_code': 'Huile_Speciale_Friture_FLEURIAL', 'product_name': 'Huile Spéciale Friture FLEURIAL', 'price': 167.35, 'product_image': 'https://www.cevital-agro-industrie.com/storage/2023/06/huile-friture.jpg'}, 
    {'category': 'alimentation', 'provider': 'cevital', 'product_code': 'Vinaigrettes', 'product_name': 'Vinaigrettes', 'price': 234.92, 'product_image': 'https://www.cevital-agro-industrie.com/storage/2023/03/Vinaigrettes-1-1.jpg'},
    {'category': 'alimentation', 'provider': 'cevital', 'product_code': 'Sauce_Harissa_Elio', 'product_name': 'Sauce Harissa Elio', 'price': 122.69, 'product_image': 'https://www.cevital-agro-industrie.com/storage/2023/08/harissa-elio-min.jpg'}, 
    {'category': 'laitage', 'provider': 'leBerber', 'product_code': 'Fromage_fondu_portion', 'product_name': 'Fromage fondu portion', 'price': 186.68, 'product_image': 'http://www.promasidor.dz/media/3413/boite-16-portions-plus-une-portion.png'}, 
    {'category': 'laitage', 'provider': 'leBerber', 'product_code': 'Fromage_fondu_barre', 'product_name': 'Fromage fondu barre', 'price': 249.55, 'product_image': 'http://www.promasidor.dz/media/3414/product_lb_croissance_square.png'}, 
    {'category': 'laitage', 'provider': 'leBerber', 'product_code': 'Fromage_cuisine', 'product_name': 'Fromage cuisine', 'price': 222.45, 'product_image': 'http://www.promasidor.dz/media/3415/product_lb_cuisiner_barre-300gr.png'}, 
    {'category': 'laitage', 'provider': 'leBerber', 'product_code': 'Fromage_olive_noir', 'product_name': 'Fromage olive noir', 'price': 104.47, 'product_image': 'http://www.promasidor.dz/media/3249/barre-150gr-olive-noire-copy.png'}, 
    {'category': 'laitage', 'provider': 'leBerber', 'product_code': 'Ail_&_finesherbes', 'product_name': 'Ail & fines-herbes', 'price': 200.07, 'product_image': 'http://www.promasidor.dz/media/3247/barre-150gr-ail-et-fines-herbes-copy.png'}

    
 ]




    
@app.callback(
        Output('containier', 'children'),
        Input('product_povider', 'value'),
        State("items_pushed_to_cart", "data"),
    )

def on_data_set_graph(product_povider, items_pushed_to_cart):

    visible  = []
    hidden = []
    items_in_cart_and_filtered_data = []
    items_in_cart_not_in_filtered_data = []
    not_in_cart_and_filtered_data = []
    for item in data:
        product_code = item['product_code']
        _product_provider = item['provider']
        if  product_code in items_pushed_to_cart and  _product_provider == product_povider:
            items_in_cart_and_filtered_data.append(item)
        elif product_code in items_pushed_to_cart and  _product_provider != product_povider:
            items_in_cart_not_in_filtered_data.append(item)
        elif product_code not in items_pushed_to_cart and  _product_provider == product_povider:
            not_in_cart_and_filtered_data.append(item)


    product_quantity = 0
    for item in not_in_cart_and_filtered_data + items_in_cart_and_filtered_data:
        visibility = 'visible'
        if item in items_in_cart_and_filtered_data:
            product_quantity = items_pushed_to_cart[item['product_code']]['item_quantity']
   
        visible.append(
                    item_card(
                        item['product_code'],  
                        item['product_name'][:20],
                        item['price'],
                        product_quantity,
                        visibility
                   )
            )
        
    for item in items_in_cart_not_in_filtered_data:
              product_quantity = items_pushed_to_cart[item['product_code']]['item_quantity']
              visibility = 'visible'
              hidden.append(
                        item_card(
                        item['product_code'],  
                        item['product_name'][:20],
                        item['price'],
                        product_quantity,
                        visibility
                       )
                )
   

    return html.Div([html.Div(visible), html.Div(hidden)])


@app.callback(
        Output({"type": "card_item_total", "index": MATCH}, "children"), 
        Input({"type": "card_item_quantity", "index": MATCH}, "value"),
        State({"type": "card_item_price", "index": MATCH}, "children"))

def item_card_add_item(card_item_quantity,item_price ):
    if card_item_quantity:
        return card_item_quantity*item_price
    return 0

@app.callback(
        Output({"type": "cart_item_total", "index": MATCH}, "children"), 
        Input({"type": "card_item_quantity", "index": MATCH}, "value"),
        State({"type": "card_item_price", "index": MATCH}, "children"))

def item_card_add_item(card_item_quantity,item_price ):
    if card_item_quantity:
        return card_item_quantity*item_price
    return 0


@app.callback(
        Output({"type": "cart_item_quantity", "index": MATCH}, "value"), 
        Output({"type": "card_item_quantity", "index": MATCH}, "value"), 
         
        Input({"type": "card_item_quantity", "index": MATCH}, "value"),
        Input({"type": "cart_item_quantity", "index": MATCH}, "value"),
        prevent_initial_call=True,
    )

def stored_items(card_item_quantity, cart_item_quantity):
    if card_item_quantity:
        if ctx.triggered_id['type'] =='card_item_quantity':
            return  card_item_quantity, card_item_quantity

        elif ctx.triggered_id['type'] =='cart_item_quantity':
            return  cart_item_quantity, cart_item_quantity
        
    return 0, 0



@callback(
        Output("items_pushed_to_cart", "data"),
        Output('cart', 'children'),
        Input({"type": "card_item_quantity", "index": ALL}, "value"),
        State("items_pushed_to_cart", "data"),
        prevent_initial_call=True,
)

def item_card_add_item(card_item_quantity, items_pushed_to_cart):
    if [i for i in card_item_quantity  if i ]:
        for item in   ctx.triggered:
            item_id = eval(item['prop_id'].replace('.value', ''))['index']
            if item['value']:
                items_pushed_to_cart[item_id] = {
                    'product_code':item_id,
                    'item_quantity': item['value'],
                }

        cart_items = []
        for _item_code, item in items_pushed_to_cart.items():
            cart_items.append(
                dmc.Group(
                    children = [ 
                        dmc.Text(item['product_code'][:20], miw = 150), 
                        dmc.NumberInput(id={"type": "cart_item_quantity", "index": item['product_code']}, value = item['item_quantity'], min=0),
                        dmc.Text( 0, id={"type": "cart_item_total", "index":item['product_code']}) 
                    ]
                )
            )

        return items_pushed_to_cart, html.Div(cart_items)
    
    return no_update


if __name__ == '__main__':
    app.run_server(debug=True)

