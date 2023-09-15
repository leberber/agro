window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {

        show_dcc_stored_items: function (data, search, category_chips, provider_chips, load_more) {
        
           

            let filtereddata = data.filter((country) => country.product_name.toLowerCase().startsWith(search));
            console.log(load_more)
            // if (filter_chips) {
            //     filtereddata = data.filter((item) => item.category == filter_chips );
            // }
             if (category_chips) {
                if (category_chips.length !== 0)  {
                    filtereddata = filtereddata.filter( item => category_chips.includes( item.category ) );
                }
            }

       
            // if (filter_chips) {
            //     filtereddata = data.filter((item) => item.category == filter_chips );
            // }
             if (provider_chips) {
                if (provider_chips.length !== 0)  {
              
                    filtereddata = filtereddata.filter( item => provider_chips.includes( item.provider ) );
                }
              
            }
            let filteredDataLength = filtereddata.length
            let paginations_size = 4
            let start = load_more * paginations_size
            let end = start + paginations_size
            let remaining_items = filteredDataLength - end
            console.log(start, end, filteredDataLength)

            
            filtereddata = filtereddata.slice(0, end)
            

            let article_card = []
            filtereddata.forEach((article)=> {
                article_card.push(
                    {'props': {'children': [
                        {'props': {'children': {'props': {'children': {'props': {'src': article.product_image, 'width': 200}, 'type': 'Image', 'namespace': 'dash_mantine_components'}}, 'type': 'Center', 'namespace': 'dash_mantine_components'}, 'p': 30}, 'type': 'CardSection', 'namespace': 'dash_mantine_components'},
                         {'props': {'children': [{'props': {'children': article.product_name, 'id':  article.product_code, 'className': 'article_name'}, 'type': 'Text', 'namespace': 'dash_mantine_components'}]}, 'type': 'Text', 'namespace': 'dash_mantine_components'}, 
                         {'props': {'children': 
    
                         {'props': {'children': [
                                {'props': {'children': {'props': {'children': `${article.price} DA`, 'id': `price_${ article.product_code}`, 'className': 'price_test'}, 'type': 'Text', 'namespace': 'dash_mantine_components'}, 'className': 'item_type_column', 'span': 4}, 'type': 'Col', 'namespace': 'dash_mantine_components'},
                                {'props': {'children': {'props': {'id': `number_input_card_${ article.product_code}`, 'className': 'item_type_number_input', 'hideControls': true, 'value': 0}, 'type': 'NumberInput', 'namespace': 'dash_mantine_components'}, 'className': 'item_type_column', 'span': 2}, 'type': 'Col', 'namespace': 'dash_mantine_components'}, 
                                {'props': {'children': {'props': {'children': '0 DA', 'id': `sum_${ article.product_code}`, 'className': 'price_test'}, 'type': 'Text', 'namespace': 'dash_mantine_components'}, 'className': 'item_type_column', 'span': 4}, 'type': 'Col', 'namespace': 'dash_mantine_components'}
                            ], 'align': 'center', 'className': 'item_type_grid', 'gutter': 'xl', 'justify': 'center'}, 'type': 'Grid', 'namespace': 'dash_mantine_components'}
                        
                        
                        }, 'type': 'Paper', 'namespace': 'dash_mantine_components'}
                        ], 'radius': 'md', 'shadow': 'sm', 'style': {'width': 396}, 'withBorder': true}, 'type': 'Card', 'namespace': 'dash_mantine_components'}
                )
                });
        
                if(remaining_items > 0) {
                    return [{'props': {'children': article_card}, 'type': 'Div', 'namespace': 'dash_html_components'}, remaining_items, 'block']


                }
            return [{'props': {'children': article_card}, 'type': 'Div', 'namespace': 'dash_html_components'}, remaining_items, 'none']
       
     

    },
        update_cart_itmes: function (number_input, item_name, price, data) {
       
            item_code = window.dash_clientside.callback_context.states_list[0]['id']
            price = price.match(/\d+/)[0] 
            if (number_input) {
                data[item_code] = {
                    'price':price,
                    'quantity':number_input,
                    'total': price*number_input
                    }
                let total = number_input*price
               
                return [data,  `${total.toFixed(2)} DA`]
            }
       delete data[item_code]
        
        return [data,'0 DA']
        
        },

    show_cart_items: function (data) {
       
        var articles = [];
        Object.entries(data).forEach(([item_name, item_order]) => {
           
            articles.push(
                {'props': {'children': [
                    {'props': {'children': {'props': {'src': 'assets/sucre.png', 'width': 40}, 'type': 'Image', 'namespace': 'dash_mantine_components'}, 'className': '', 'span': 3}, 'type': 'Col', 'namespace': 'dash_mantine_components'},
                    {'props': {'children': {'props': {'children': item_name}, 'type': 'Text', 'namespace': 'dash_mantine_components'}, 'className': '', 'span': 3}, 'type': 'Col', 'namespace': 'dash_mantine_components'}, 
                    {'props': {'children': {'props': {'children': item_order['price']}, 'type': 'Text', 'namespace': 'dash_mantine_components'}, 'className': '', 'span': 2}, 'type': 'Col', 'namespace': 'dash_mantine_components'}, 
                    {'props': {'children': {'props': {id :`number_input_cart_${item_name}`, 'hideControls': true, 'value': item_order['quantity']},  'type': 'NumberInput', 'namespace': 'dash_mantine_components'}, 'className': '', 'span': 2}, 'type': 'Col', 'namespace': 'dash_mantine_components'}, 
                    {'props': {'children': {'props': {'children': item_order['total']}, 'type': 'Text', 'namespace': 'dash_mantine_components'}, 'className': '', 'span': 2}, 'type': 'Col', 'namespace': 'dash_mantine_components'}
                ], 
                'align': 'center', 
                'className': 'checkout_grids',
                 'gutter': 'xl', 'justify': 'center'
                }, 'type': 'Grid', 'namespace': 'dash_mantine_components'}

            )
            
        
        });

        let items = {'props': {'children': articles}, 'type': 'Div', 'namespace': 'dash_html_components'}
        let header = {'props': {'children': [
            {'props': {'children': '', 'className': '', 'span': 3}, 'type': 'Col', 'namespace': 'dash_mantine_components'},
            {'props': {'children': {'props': {'children': 'Article'}, 'type': 'Text', 'namespace': 'dash_mantine_components'}, 'className': '', 'span': 3}, 'type': 'Col', 'namespace': 'dash_mantine_components'}, 
            {'props': {'children': {'props': {'children': 'Prix Unite'}, 'type': 'Text', 'namespace': 'dash_mantine_components'}, 'className': '', 'span': 2}, 'type': 'Col', 'namespace': 'dash_mantine_components'}, 
            {'props': {'children': {'props': {'children': 'Quantite'}, 'type': 'Text', 'namespace': 'dash_mantine_components'}, 'className': '', 'span': 2}, 'type': 'Col', 'namespace': 'dash_mantine_components'}, 
            {'props': {'children': {'props': {'children': 'Total'}, 'type': 'Text', 'namespace': 'dash_mantine_components'}, 'className': '', 'span': 2}, 'type': 'Col', 'namespace': 'dash_mantine_components'}
        ], 
        'align': 'center', 
        'className': 'checkout_grids',
         'gutter': 'xl', 'justify': 'center'
        }, 'type': 'Grid', 'namespace': 'dash_mantine_components'}

        return {'props': {'children': [header, items]}, 'type': 'Div', 'namespace': 'dash_html_components'}

    },
   
    },


    
});