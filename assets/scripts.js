window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        update_cart_itmes: function (number_input, artile, article_type, price, data) {
            price = price.match(/\d+/)[0] 
            data[artile+'_'+article_type] = {
                        'price':price,
                        'quantity':number_input,
                        'total': price*number_input
                        }
           
            let total = number_input*price
            
            return [data,  `${total.toFixed(2)} DA`
        ]
        },

    show_cart_items: function (data) {
        console.log(data)
        var articles = [];
        // const entries = Object.entries(data);
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
            
            console.log(
               key
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

    }
    },


    
});