@app.callback(
        Output('containier', 'children'),
        Input('product_povider', 'value'),
        State("items_pushed_to_cart", "data"),
     
        )


def on_data_set_graph(product_povider, items_pushed_to_cart):

    visible  = []
    hidden = []

    filtered_data = []
    filtered_data_ids = []
    for item in data:
        filtered_data_ids.append(item['product_code'])
        if item['provider'] != product_povider:
            filtered_data.append(item)
    print(filtered_data_ids)


    
    
    for item in filtered_data:
 
        if  item['product_code'] in items_pushed_to_cart:
            product_quantity = items_pushed_to_cart[item['product_code']]['item_quantity']
        else:
            product_quantity = 0


        visible.append(
                    item_card(
                    item['product_code'],  
                    item['product_name'][:20],
                    item['price'],
                    product_quantity,
                    "product_visibility")
            )
        
    for item in items_pushed_to_cart:
        print(item)

        if item in filtered_data_ids:
            hidden.append(
                    item_card(
                    item['product_code'],  
                    item['product_name'][:20],
                    item['price'],
                    product_quantity,
                    "product_visibility")
            )


        # elif item['provider'] == product_povider:
        #     product_visibility='output'
        #     product_quantity = 0
        #     hidden.append(
        #             item_card(
        #             item['product_code'],  
        #             item['product_name'][:20],
        #             item['price'],
        #             product_quantity,
        #             product_visibility)
        #     )

    return html.Div([html.Div(visible), html.Div(hidden)])



    
@app.callback(
        Output('containier', 'children'),
        Input('product_povider', 'value'),
        State("items_pushed_to_cart", "data"),
     
        )


def on_data_set_graph(product_povider, items_pushed_to_cart):

    output  = []
    
    for item in data:
        if  item['product_code'] in items_pushed_to_cart:
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
                        product_visibility)
                )

        elif item['provider'] == product_povider:
            product_visibility='output'
            product_quantity = 0
            output.append(
                    item_card(
                    item['product_code'],  
                    item['product_name'][:20],
                    item['price'],
                    product_quantity,
                    product_visibility)
            )

    return output