

from dash import Dash, Input, html, Output, MATCH, no_update, State, dcc, ALL, ctx

app = Dash(__name__)
import dash_mantine_components as dmc

app.layout = html.Div(
    children = [
        dmc.ChipGroup(
    [dmc.Chip(x, value=x) for x in ["leBerber",'cevital']],
    value="leBerber",
    id = 'product_povider'
),
   dmc.Button('btn', id = 'btn'),
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



def item_card(product_code, product_name, product_price, product_quantity, product_visibility):
    return dmc.Grid(
            children=[
                dmc.Col(html.Div( dmc.Text(product_name, miw = 150)), span=3),
                dmc.Col(html.Div( dmc.Text(product_price, id={"type": "card_item_price", "index":product_code})), span=3),
                dmc.Col(html.Div( dmc.NumberInput(id={"type": "card_item_quantity", "index": product_code}, value = product_quantity)), span=3),
                dmc.Col(html.Div( dmc.Text( id={"type": "card_item_total", "index":product_code}) ), span=3),
            
            ],
            gutter="xl",
            style={'visibility':f'{product_visibility}'}
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
        Output('datastored', 'children'),
        Input('btn', 'n_clicks'),
         State("items_pushed_to_cart", "data"),
     
        )
def uio(n, d):
    return str(d)

    
@app.callback(
        Output('containier', 'children'),
        Input('product_povider', 'value'),
        State("items_pushed_to_cart", "data"),
     
        )


def on_data_set_graph(product_povider, items_pushed_to_cart):

    output  = []
    
    for item in data:
        if  item['product_code'] in items_pushed_to_cart and  item['provider'] != product_povider:
            
            product_visibility='hidden'
            product_quantity = items_pushed_to_cart[item['product_code']]['item_quantity']
            output.append(
                    item_card(
                    item['product_code'],  
                    item['product_name'][:20],
                    item['price'],
                    product_quantity,
                    product_visibility)
            )

        elif item['provider'] == product_povider:
            product_visibility='visible'
            product_quantity = 0
            output.append(
                    item_card(
                    item['product_code'],  
                    item['product_name'][:20],
                    item['price'],
                    product_quantity,
                    product_visibility)
            )

    #         if
    #         data_.append(item)
    #     elif item['product_code']  in items_pushed_to_cart :


    # output = []
    # for item in data_:
    #     if  item['product_code'] in items_pushed_to_cart:
    #         product_quantity = items_pushed_to_cart[item['product_code']]['item_quantity']
    #     else:
    #         product_quantity = 0

    #     output.append(
    #          item_card(
    #         item['product_code'],  
    #         item['product_name'][:20],
    #         item['price'],
    #           product_quantity)
    #     )

    return output

@app.callback(
        Output({"type": "card_item_total", "index": MATCH}, "children"), 
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
    # return no_update

    if ctx.triggered_id['type'] =='card_item_quantity':
        if card_item_quantity:
            return  card_item_quantity, card_item_quantity

    elif ctx.triggered_id['type'] =='cart_item_quantity':
        if cart_item_quantity:
            return  cart_item_quantity, cart_item_quantity
        
    return 0, 0



@app.callback(
       
        Output("items_pushed_to_cart", "data"),
         Output('cart', 'children'),
        Input({"type": "card_item_quantity", "index": ALL}, "value"),
        State("items_pushed_to_cart", "data"),
          prevent_initial_call=True,
        
        )

def item_card_add_item(card_item_quantity, items_pushed_to_cart):
    # print(not items_pushed_to_cart)

    if [i for i in card_item_quantity  if i ]:
        for item in   ctx.triggered:
            item_id = eval(item['prop_id'].replace('.value', ''))['index']
            if item['value']:
                items_pushed_to_cart[item_id] = {
                    'item_id':item_id,
                    'item_quantity': item['value'],

                }
        # print('-----------')
        # items_pushed_to_cart = selected_items + items_pushed_to_cart
        # print(items_pushed_to_cart)
        cart_items = []
        for _item_code, item in items_pushed_to_cart.items():
            # print(item['item_id'], item['item_quantity'])
          
            cart_items.append(dmc.Group(
                    children = [ 
                        dmc.Text(item['item_id'][:20], miw = 150), 
                        # dmc.Text(item['price'], id={"type": "card_item_price", "index": item['product_code']}), 
                        dmc.NumberInput(id={"type": "cart_item_quantity", "index": item['item_id']}, value = item['item_quantity']),
                    ]
                ))

        return items_pushed_to_cart, html.Div(cart_items)
    
    return no_update


if __name__ == '__main__':
    app.run_server(debug=True)


    #     data_  = []
    # for item in data:
    #     if item['provider'] == product_povider or item['product_code']  in items_pushed_to_cart :
    #         data_.append(item)

    # output = []
    # for item in data_:
    #     if  item['product_code'] in items_pushed_to_cart:
    #         product_quantity = items_pushed_to_cart[item['product_code']]['item_quantity']
    #     else:
    #         product_quantity = 0

    #     output.append(
    #          item_card(
    #         item['product_code'],  
    #         item['product_name'][:20],
    #         item['price'],
    #           product_quantity)
    #     )

    # return out
    # putd

    def on_data_set_graph(product_povider, items_pushed_to_cart):

    visible  = []
    hidden = []

    filtered_data = []
    filtered_data_ids = []
    items_in_cart_and_filtered_data = []
    items_in_cart_not_in_filtered_data = []
    not_in_cart_and_filtered_data = []
    for item in data:
        product_code = item['product_code']
        _product_provider = item['provider']
        if  product_code in items_pushed_to_cart and  _product_provider== product_povider:
            items_in_cart_and_filtered_data.append(item)
        elif product_code in items_pushed_to_cart and  _product_provider!= product_povider:
            items_in_cart_not_in_filtered_data.append(item)
        elif product_code not in items_pushed_to_cart and  _product_provider== product_povider:
            not_in_cart_and_filtered_data.append(item)

    print( 'stored and filterd' , len(items_in_cart_and_filtered_data))
    print( 'stored and not filterd' , len(items_in_cart_not_in_filtered_data))
    print( 'not stored and filterd', len(not_in_cart_and_filtered_data ))

        # filtered_data_ids.append(item['product_code'])
        # if item['provider'] != product_povider:
        #     filtered_data.append(item)

    


    for item in items_in_cart_and_filtered_data + not_in_cart_and_filtered_data:

        # it si in cart but not in filterd data 
        
        visible.append(
                    item_card(
                    product_code,  
                    item['product_name'][:20],
                    item['price'],
                    0,
                   )
            )
        
    for item in items_in_cart_not_in_filtered_data:

        # it si in cart but not in filterd data 
        
        visible.append(
                    item_card(
                    product_code,  
                    item['product_name'][:20],
                    item['price'],
                    0,
                   )
            )
    return visible

    


def on_data_set_graph(product_povider, items_pushed_to_cart):

    output  = []

    filtered_data = []
    filtered_data_ids = []
    items_in_cart_and_filtered_data = []
    items_in_cart_not_in_filtered_data = []
    not_in_cart_and_filtered_data = []
    for item in data:
        product_code = item['product_code']
        _product_provider = item['provider']
        if  product_code in items_pushed_to_cart and  _product_provider== product_povider:
            items_in_cart_and_filtered_data.append(item)
        elif product_code in items_pushed_to_cart and  _product_provider!= product_povider:
            items_in_cart_not_in_filtered_data.append(item)
        elif product_code not in items_pushed_to_cart and  _product_provider== product_povider:
            not_in_cart_and_filtered_data.append(item)

    for i in items_in_cart_not_in_filtered_data:
        
        print(i)

    for item in not_in_cart_and_filtered_data + items_in_cart_and_filtered_data:
        product_quantity = 0
        output.append(
                    item_card(
                    item['product_code'],  
                    item['product_name'][:20],
                    item['price'],
                    product_quantity,
                   )
            )


    
    for item in data:
        # if item['provider'] == product_povider:
        #     product_quantity = 0
        #     output.append(
        #             item_card(
        #             item['product_code'],  
        #             item['product_name'][:20],
        #             item['price'],
        #             product_quantity,
        #            )
        #     )
    
        if  item['product_code'] in items_pushed_to_cart:
            print(item)
            product_quantity = items_pushed_to_cart[item['product_code']]['item_quantity']
            if item['provider'] != product_povider:
                product_visibility=True
                
            else:
                product_visibility=True

            output.append(
                        item_card(
                        item['product_code'],  
                        item['product_name'][:20],
                        item['price'],
                        product_quantity,
                       )
                )



    return output
