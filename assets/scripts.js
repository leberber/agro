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

        make_cards: function(product_provider, items_pushed_to_cart, _data){
            function shop_card(product_name, product_code, product_price,  product_quantity, image_path) {
                return  {'namespace': 'dash_mantine_components',
                'props': {'children': [{'namespace': 'dash_mantine_components',
                                        'props': {'children': [{'namespace': 'dash_mantine_components',
                                                                'props': {'children': {'namespace': 'dash_mantine_components',
                                                                                        'props': {'className': 'card-image',
                                                                                                'src': image_path},
                                                                                        'type': 'Image'},
                                                                        'id': {'index': product_code,
                                                                                'type': 'card_image_action'},
                                                                        'style': {'height': '100%',
                                                                                    'width': '100%'}},
                                                                'type': 'ActionIcon'}],
                                                'className': 'card-image-column',
                                                'p': 5,
                                                'span': 3},
                                        'type': 'Col'},
                                        {'namespace': 'dash_mantine_components',
                                        'props': {'children': [{'namespace': 'dash_mantine_components',
                                                                'props': {'children': [{'namespace': 'dash_mantine_components',
                                                                                        'props': {'children': {'namespace': 'dash_mantine_components',
                                                                                                                'props': {'children':  product_name,
                                                                                                                        'size': 'lg',
                                                                                                                        'weight': 500},
                                                                                                                'type': 'Text'},
                                                                                                'px': 0,
                                                                                                'span': 7},
                                                                                        'type': 'Col'},
                                                                                        {'namespace': 'dash_mantine_components',
                                                                                        'props': {'children': {'namespace': 'dash_mantine_components',
                                                                                                                'props': {'align': 'right',
                                                                                                                        'children': product_price,
                                                                                                                        'color': 'green',
                                                                                                                        'id': {'index': product_code,
                                                                                                                                'type': 'card_item_price'},
                                                                                                                        'size': 'md',
                                                                                                                        'weight': 900},
                                                                                                                'type': 'Text'},
                                                                                                'px': 0,
                                                                                                'span': 5},
                                                                                        'type': 'Col'}]},
                                                                'type': 'Grid'},
                                                                {'namespace': 'dash_mantine_components',
                                                                'props': {'children': [{'namespace': 'dash_mantine_components',
                                                                                        'props': {'children': [{'namespace': 'dash_mantine_components',
                                                                                                                'props': {'align': 'center',
                                                                                                                        'children': [{'namespace': 'dash_mantine_components',
                                                                                                                                        'props': {'className': 'card-quantity-input',
                                                                                                                                                'h': 30,
                                                                                                                                                'hideControls': true,
                                                                                                                                                'id': {'index': product_code,
                                                                                                                                                        'type': 'card_item_quantity'},
                                                                                                                                                'mih': 20,
                                                                                                                                                'min': 0,
                                                                                                                                                'placeholder': 0,
                                                                                                                                                'size': 'lg',
                                                                                                                                                'value': product_quantity,
                                                                                                                                                'w': 50},
                                                                                                                                        'type': 'NumberInput'},
                                                                                                                                        {'namespace': 'dash_mantine_components',
                                                                                                                                        'props': {'align': 'right',
                                                                                                                                                'children': 'Quantity',
                                                                                                                                                'size': 'md',
                                                                                                                                                'weight': 600},
                                                                                                                                        'type': 'Text'}]},
                                                                                                                'type': 'Stack'}],
                                                                                                'px': 0,
                                                                                                'span': 4},
                                                                                        'type': 'Col'},
                                                                                        {'namespace': 'dash_mantine_components',
                                                                                        'props': {'children': [{'namespace': 'dash_mantine_components',
                                                                                                                'props': {'align': 'center',
                                                                                                                        'children': [{'namespace': 'dash_mantine_components',
                                                                                                                                        'props': {'children': null,
                                                                                                                                                'id': {'index': product_code,
                                                                                                                                                        'type': 'card_item_total'},
                                                                                                                                                'lh': '30px',
                                                                                                                                                'size': 'md',
                                                                                                                                                'weight': 'bolder'},
                                                                                                                                        'type': 'Text'},
                                                                                                                                        {'namespace': 'dash_mantine_components',
                                                                                                                                        'props': {'align': 'right',
                                                                                                                                                'children': 'Total',
                                                                                                                                                'size': 'md',
                                                                                                                                                'weight': 600},
                                                                                                                                        'type': 'Text'}]},
                                                                                                                'type': 'Stack'}],
                                                                                                'px': 0,
                                                                                                'span': 5},
                                                                                        'type': 'Col'}],
                                                                        'justify': 'flex-end'},
                                                                'type': 'Grid'}],
                                                'span': 'auto'},
                                        'type': 'Col'}],
                        'className': 'card-grid',
                        'justify': 'center'},
                'type': 'Grid'}
            }
            // console.log( c(2, 5))
            
            let visible = [];
            let hidden = [];
            let items_in_cart_and_filtered_data = [];
            let items_in_cart_not_in_filtered_data = [];
            let not_in_cart_and_filtered_data = [];
            
            _data.forEach(function(item) {
              let product_code = item['product_code'];
              var _product_provider = item['provider'];
              
              if (product_code in items_pushed_to_cart && _product_provider === product_provider) {
                items_in_cart_and_filtered_data.push(item);
              } else if (product_code in items_pushed_to_cart && _product_provider !== product_provider) {
                items_in_cart_not_in_filtered_data.push(item);
              } else if  (!(product_code in items_pushed_to_cart) && (_product_provider === product_provider)) {
                not_in_cart_and_filtered_data.push(item);
              }
            });
            var product_quantity = null;
            (not_in_cart_and_filtered_data.concat(items_in_cart_and_filtered_data)).forEach(function(item) {
                var product_code = item['product_code'];
                
                if (item in items_in_cart_and_filtered_data) {
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
              
            return {'props': {'children': [
                {'props': {'children': visible}, 'type': 'Div', 'namespace': 'dash_html_components'},
             {'props': {'children': hidden, 'style': {'display': 'none'}}, 'type': 'Div', 'namespace': 'dash_html_components'}
            ]}, 'type': 'Div', 'namespace': 'dash_html_components'}
        
         
            // console.log(items_in_cart_and_filtered_data, items_in_cart_not_in_filtered_data, not_in_cart_and_filtered_data)
            
           

        }
        


        
     

   
    },
});