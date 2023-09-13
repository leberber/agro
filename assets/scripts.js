window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        update_cart_itmes: function (number_input, artile, article_type, price, data) {
            price = price.match(/\d+/)[0] 
            if (number_input) {
                data[artile+'_'+article_type] = {
                    'price':price,
                    'quantity':number_input,
                    'total': price*number_input
                    }
                let total = number_input*price
                console.log(data)
                return [data,  `${total.toFixed(2)} DA`]
            }
        return window.dash_clientside.no_update
        
        },

    show_cart_items: function (data) {
       
        var articles = [];
        // const entries = Object.entries(data);
        // Object.entries(data).forEach(([key, value]) => {
        //     Object.entries(value).forEach(([key, value]) => {
        //         console.log('sub',key, value)
            
        //     });

        // });
        Object.entries(data).forEach(([key, value]) => {
            articles.push(
                {'props': {'children': [
                    {'props': {'children': {'props': {'src': 'assets/sucre.png', 'width': 40}, 'type': 'Image', 'namespace': 'dash_mantine_components'}, 'className': '', 'span': 3}, 'type': 'Col', 'namespace': 'dash_mantine_components'},
                    {'props': {'children': {'props': {'children': key}, 'type': 'Text', 'namespace': 'dash_mantine_components'}, 'className': '', 'span': 3}, 'type': 'Col', 'namespace': 'dash_mantine_components'}, 
                    {'props': {'children': {'props': {'children': value['price']}, 'type': 'Text', 'namespace': 'dash_mantine_components'}, 'className': '', 'span': 2}, 'type': 'Col', 'namespace': 'dash_mantine_components'}, 
                    {'props': {'children': {'props': {id :key, 'hideControls': true, 'value': value['quantity']},  'type': 'NumberInput', 'namespace': 'dash_mantine_components'}, 'className': '', 'span': 2}, 'type': 'Col', 'namespace': 'dash_mantine_components'}, 
                    {'props': {'children': {'props': {'children': value['total']}, 'type': 'Text', 'namespace': 'dash_mantine_components'}, 'className': '', 'span': 2}, 'type': 'Col', 'namespace': 'dash_mantine_components'}
                ], 
                'align': 'center', 
                'className': 'checkout_grids',
                 'gutter': 'xl', 'justify': 'center'
                }, 'type': 'Grid', 'namespace': 'dash_mantine_components'}

            )
            
        
        });

    //     data.forEach((element) => arr.push(
    // console.log(element)
    //     ));
 
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
    show_dcc_stored_items: function (data, search) {
       
        if (search){
            data = Object.keys(data).sort().reduce((a, c) => (a[c] = data[c], a), {})
            data = Object.keys(data)
                .filter((key) => key.includes(search))
                .reduce((obj, key) => {
                    return Object.assign(obj, {
                    [key]: data[key]
                    });
            }, {});

        } else{
            data = Object.keys(data)
            .filter((key) => key.includes('a'))
            .reduce((obj, key) => {
                return Object.assign(obj, {
                [key]: data[key]
                });
        }, {});

        }
   

        // console.log(names);

        let article_card  = []
        Object.entries(data).forEach(([article, value]) => {
            // console.log(article, value)
            let artile_type = []
            Object.entries(value).forEach(([article_type, value]) => {
                artile_type.push(
                        {'props': {'children': [
                            {'props': {'children': 
                                    {'props': {'children': article_type, 'id': `name_${article}_${article_type}`}, 'type': 'Text', 'namespace': 'dash_mantine_components'},
                                    'className': 'item_type_column', 'span': 2
                                }, 'type': 'Col', 'namespace': 'dash_mantine_components'
                            }, 
                            {'props': {'children': {'props': {'children': value, 'id': `price_${article}_${article_type}`, 'className': 'price_test'}, 'type': 'Text', 'namespace': 'dash_mantine_components'}, 'className': 'item_type_column', 'span': 4}, 'type': 'Col', 'namespace': 'dash_mantine_components'},
                            {'props': {'children': {'props': {'id': `number_input_${article}_${article_type}`, 'className': 'item_type_number_input', 'hideControls': true, 'value': 0}, 'type': 'NumberInput', 'namespace': 'dash_mantine_components'}, 'className': 'item_type_column', 'span': 2}, 'type': 'Col', 'namespace': 'dash_mantine_components'}, 
                            {'props': {'children': {'props': {'children': '0 DA', 'id': `sum_${article}_${article_type}`, 'className': 'price_test'}, 'type': 'Text', 'namespace': 'dash_mantine_components'}, 'className': 'item_type_column', 'span': 4}, 'type': 'Col', 'namespace': 'dash_mantine_components'}
                        ], 'align': 'center', 'className': 'item_type_grid', 'gutter': 'xl', 'justify': 'center'}, 'type': 'Grid', 'namespace': 'dash_mantine_components'}
                )
            });
            article_card.push(
                {'props': {'children': [
                    {'props': {'children': {'props': {'children': {'props': {'src': 'assets/huile.png', 'width': 200}, 'type': 'Image', 'namespace': 'dash_mantine_components'}}, 'type': 'Center', 'namespace': 'dash_mantine_components'}, 'p': 30}, 'type': 'CardSection', 'namespace': 'dash_mantine_components'},
                     {'props': {'children': [{'props': {'children': article, 'id': article, 'className': 'article_name'}, 'type': 'Text', 'namespace': 'dash_mantine_components'}]}, 'type': 'Text', 'namespace': 'dash_mantine_components'}, 
                     {'props': {'children': artile_type}, 'type': 'Paper', 'namespace': 'dash_mantine_components'}
                    ], 'radius': 'md', 'shadow': 'sm', 'style': {'width': 396}, 'withBorder': true}, 'type': 'Card', 'namespace': 'dash_mantine_components'}
            )


        });


     
       return {'props': {'children': article_card}, 'type': 'Div', 'namespace': 'dash_html_components'}
     

    }
    },


    
});