// ctx = window.dash_clientside.callback_context;

window.dash_clientside = Object.assign({}, window.dash_clientside, {
   
    clientside: {
        theme_switcher: function (n_clicks) {

            let lightIcon = {'props': {'icon': 'ic:baseline-light-mode', 'width': 40, 'color':'gold'}, 'type': 'DashIconify', 'namespace': 'dash_iconify'}
            let darkIcon = {'props': {'icon': 'ic:sharp-dark-mode', 'width': 40, 'color':'#e8e3e6'}, 'type': 'DashIconify', 'namespace': 'dash_iconify'}
            let lightColorScheme =  { 
                "colorScheme": "light",
                "shadows": {
       
                    "xs": "0px 4px 3px -3px rgba(0, 0, 0, 0.05)",
                    "xl": "inset 0px 4px 3px -3px rgba(0, 0, 0, 0.05)",
                }
            }
            let darktColorScheme =  { 
                "colorScheme": "dark",
                "shadows": {
               
                    "xs": "0px 4px 3px -3px rgba(66, 66, 66, 1)",
                    "xl": "inset 0px 4px 3px -3px rgba(66, 66, 66, 1)",
                }
            }
        
            if (n_clicks % 2 === 0) { 
                return [lightColorScheme, lightIcon]
              } 
         
          return [darktColorScheme, darkIcon]
        },

        page_switcher: function(page_switcher_input) {
            ctx = window.dash_clientside.callback_context;
 
            pages_list = ctx.inputs_list[0];
            triggered_input = JSON.parse(ctx.triggered[0].prop_id.replace(".n_clicks", "")).index
            let output_list = []
            pages_list.forEach((page) => output_list.push(page.id.index));
            let number_of_pages = output_list.length
            let triggered_input_index = output_list.indexOf(triggered_input)

            let page_output_list = Array(number_of_pages).fill({'display':'none'})
            let action_item_output_list = Array(number_of_pages).fill({})
            page_output_list[triggered_input_index] = {'display':'block',//  'animation': '2s ease-out 0s 1 FadeIn'
        }
            action_item_output_list[triggered_input_index] = {'color':'rgb(34, 139, 230)'}
       
  
            return [page_output_list, action_item_output_list, action_item_output_list];
        },

        make_cards: function(product_provider, product_category, search, load_more, items_pushed_to_cart, _data){

        const no_update = window.dash_clientside.no_update
        let list_items_pushed_to_cart = _data.filter( item => Object.keys(items_pushed_to_cart).includes( item.product_code ) )

        _data = _data.filter((country) => country.product_name.toLowerCase().startsWith(search));

        if (!(search)) {
                _data = _data.filter( item =>  item.category === product_category );
                _data = _data.filter( item =>  item.provider === product_provider );
        }
   

        let items_in_cart_not_in_filtered_data = list_items_pushed_to_cart.filter(x => !_data.includes(x));
        
        let filteredDataLength = _data.length
        let paginations_size = 5
        let start = load_more * paginations_size
        let end = start + paginations_size
        let remaining_items = filteredDataLength - end

        display =  'block'
        if (remaining_items <= 0) { display ='none' }

        _data = _data.slice(0, end)
        
        let visible = [];
        let hidden = [];
        let items_in_cart_and_filtered_data = [];
        let not_in_cart_and_filtered_data = [];

        _data.forEach( function(item) {
                let product_code = item['product_code'];
                if (product_code in items_pushed_to_cart) {
                items_in_cart_and_filtered_data.push(item);
                } else  {
                not_in_cart_and_filtered_data.push(item);
                }
        });
            
    
        var product_quantity = null;

        (not_in_cart_and_filtered_data.concat(items_in_cart_and_filtered_data)).forEach(function(item) {
        var product_code = item['product_code'];
  
        if ( items_in_cart_and_filtered_data.includes(item)) {
                product_quantity = items_pushed_to_cart[item['product_code']]['item_quantity'];

        }
       
        
        visible.push(
                shop_card(
                item['product_name'],
                product_code,
                item['price'],
                product_quantity,
                '/assets/images/' + product_code + '.png'
                )
        );
        });

        items_in_cart_not_in_filtered_data.forEach(function(item) {
        product_quantity = items_pushed_to_cart[item['product_code']]['item_quantity'];
        var product_code = item['product_code'];
        hidden.push(
                shop_card(
                item['product_name'],
                product_code,
                item['price'],
                product_quantity,
                '/assets/images/' + product_code + '.png'
                )
                
        );
        });

        if (_data.length===0){
                visible = {'props': {'children': ['No product found, adjust your search'], 'style': {'height': 200, 'width': '100%'}}, 'type': 'Center', 'namespace': 'dash_mantine_components'}
                
        }
        cards = {'props': {'children': [
                {'props': {'children': visible}, 'type': 'Div', 'namespace': 'dash_html_components'},
                {'props': {'children': hidden, 'style': {'display': 'none'}}, 'type': 'Div', 'namespace': 'dash_html_components'}
                ]}, 'type': 'Div', 'namespace': 'dash_html_components'}
              
        
    
        return [cards, remaining_items, display]
        
         

            
           

        },
        item_card_add_item: function(cart_click, x_click, card_item_quantity, items_pushed_to_cart) {
    
        const ctx = window.dash_clientside.callback_context
        const no_update = window.dash_clientside.no_update
        // avoid intial calls and unnecessary triggers
        if (ctx.triggered.length !=1 ) { 
                
                return [no_update, no_update]
        }
        

        const triggered_id = JSON.parse(ctx.triggered[0]['prop_id'].split(".")[0])
        
        // console.log()
        ctx.inputs_list[0].forEach( function(item) {
                let item_quantity = item['value']
                // console.log(item_quantity)
                let item_id = item['id']['index']
                if (item_quantity || item_quantity === 0) {
                        items_pushed_to_cart[item_id] = {
                        product_code: item_id,
                        item_quantity: item_quantity
                        }
                }           
        })
        // console.log(triggered_id.type)
        if (triggered_id.type ==='x_out_from_cart') {
                items_pushed_to_cart[triggered_id['index']][ 'item_quantity'] = 0
             }
        if (triggered_id.type ==='card_item_quantity') {
                return [items_pushed_to_cart, no_update]
        }

        let cart_items = []

        cart_items.push(header)



        Object.entries(items_pushed_to_cart).forEach(([_,item]) => {
                product_code= item['product_code']
                product_quantity = item['item_quantity']
                if (product_quantity ===0){
                        styles = {'display':'none'}
                        
                } else{
                        styles = {}

                }
                    
                cart_items.push(
                    cart_item ( '/assets/images/' + product_code + '.png', product_code, product_quantity, styles)
                )
            })

        
        return [items_pushed_to_cart, {'namespace': 'dash_html_components',
        'props': {'children': cart_items},
        'type': 'Div'}]
        },

      CardItemDetails(clicked_item, data) {
        ctx = window.dash_clientside.callback_context;
        
        function item_detail_card (triggered_id){
                return {'namespace': 'dash_mantine_components',
                'props': {'children': [{'namespace': 'dash_mantine_components',
                                        'props': {'children': {'namespace': 'dash_mantine_components',
                                                               'props': {
                                                                         'src': '/assets/images/' + triggered_id + '.png'},
                                                               'type': 'Image'}},
                                        'type': 'CardSection'},
                                       {'namespace': 'dash_mantine_components',
                                        'props': {'children':triggered_id.replace(/_/g, " "),
                                                  'weight': 500},
                                        'type': 'Text'},
                                       {'namespace': 'dash_mantine_components',
                                        'props': {'children': ` Cheer on your favorite red and white team in eye-popping style with these red & white striped game bib overalls! Each pair is made of 100 percent cotton for a comfortable, breathable fit regardless of the weather and includes easily adjustable shoulder straps for fans with long torsos`,
                                                  'color': 'dimmed',
                                                  'size': 'sm'},
                                        'type': 'Text'}],
                          'radius': 'md',
                        //   'shadow': 'sm',
                        //   'withBorder': true
                        },
                'type': 'Card'}

        }
 

          if (clicked_item.some((elem) => !!elem )) {
            triggered_id = JSON.parse(ctx.triggered[0].prop_id.replace(".n_clicks", "")).index
            
          return [true, item_detail_card (triggered_id)]
          }
         
            return [false, '']
        }
      
       


        
     

   
    },
});