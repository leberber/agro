// ctx = window.dash_clientside.callback_context;
window.dash_clientside = Object.assign({}, window.dash_clientside, {
   
    clientside: {
        

        theme_switcher: function (n_clicks) {

            let lightIcon = {'props': {'icon': 'ic:baseline-light-mode', 'width': 40, 'color':'gold'}, 'type': 'DashIconify', 'namespace': 'dash_iconify'}
            let darkIcon = {'props': {'icon': 'ic:sharp-dark-mode', 'width': 40, 'color':'#e8e3e6'}, 'type': 'DashIconify', 'namespace': 'dash_iconify'}
            let lightColorScheme =  { "colorScheme": "light"}
            let darktColorScheme =  { "colorScheme": "dark", "shadows": {
                "md": "1px 1px 3px rgba(0,0,0,.25)",
                "xs": "5px 5px 3px rgba(232, 223, 223,.1)",
            } }
        

      
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
            page_output_list[triggered_input_index] = {'display':'block',  'animation': '2s ease-out 0s 1 FadeIn'}
            action_item_output_list[triggered_input_index] = {'color':'rgb(34, 139, 230)'}
            console.log(page_output_list, action_item_output_list);
  
            return [page_output_list, action_item_output_list, action_item_output_list];
        }
        


        
     

   
    },
});