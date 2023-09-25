#.to_plotly_json()
from dash import Dash, dcc, html, Input, Output, ALL, Patch, callback, ctx, no_update, MATCH, State, clientside_callback, ClientsideFunction
import dash_mantine_components as dmc
import json
from dash_iconify import DashIconify

import random
import pandas as pd


app = Dash(__name__, 
           suppress_callback_exceptions=True
           )


data = pd.read_csv('products.csv')
data = data.to_dict('records')
print(data)


# data = sorted(data, key=lambda x: x['product_name'])


# for i in range(0,50):
#     s = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
#     data[str(s)+'huile'+str(i)] = {'1L':'140', '2L':'280', '5L':'500'}
# print(json.dumps(data, indent=4))
# print(data.__sizeof__())

# print(      dmc.Image(
#             width=200,
#             height=100,
#             withPlaceholder=True,
#             placeholder=[dmc.Loader(color="gray", size="sm").to_plotly_json()],
#         ).to_plotly_json())
# print(dmc.Button("Light button", variant="default", size = 'sm', radius='xl', compact=True).to_plotly_json(),)
        
app.layout = html.Div(
    children=[
        dcc.Store(id = 'store_items_data'),
        dcc.Store(id = 'store_categories'),
        dcc.Store(id= 'current_items_in_layout'),
        html.Div(id = 'pa'),
        


        
             dmc.ActionIcon(
            DashIconify(icon="material-symbols:garden-cart", width=20),
            size="lg",
            variant="filled",
            id="cart-icon",
            n_clicks=0,
            mb=10,
        ),
        html.Div(id = 'filter_chips_container'),
        dmc.Text(id='void'),
             dmc.TextInput(
                 id = 'search_item',
            style={"width": 380},
            placeholder="Search",
            rightSection=DashIconify(icon="guidance:search"),
        ),
   
        html.Div(id ='test_store'),
        dmc.Button("Load more", id = 'load_more',variant="default", size = 'sm', radius='xl', compact=True, n_clicks=0, leftIcon = dmc.Badge("23", id = 'load_more_number') ),
       dcc.Store(id = 'items-in-chart', data = {}, #storage_type='local'
                 ),
        dmc.Modal(
            size="55%",
            id="cart-modal",
            zIndex=10000,
            # opened = False,
            children=[
                html.Div( id = 'cart-items'),
            ],
        ),
    ]  
)



@callback(
        Output('store_items_data', 'data'),
        Output('filter_chips_container', 'children'),
        Input('void', 'children'))
def on_data_set_graph(void):

    filters = {
         "category": set(),
         "provider": set()

         }
    for item in data:
        filters["category"].add(item['category'])
        filters["provider"].add(item['provider'])
    filters["category"] =  list(filters["category"])
    filters["provider"] =  list(filters["provider"])


    chips_category  = dmc.ChipGroup(
                children = [
                     dmc.Chip(x, value=x) for x in  filters["category"]
                ],
                multiple=True,
                id = 'filter_chips_category'
            )
    chips_provider  = dmc.ChipGroup(
                children = [
                     dmc.Chip(x, value=x) for x in  filters["provider"]
                ],
                multiple=True,
                id = 'filter_chips_provider'
            )

    return data, html.Div([chips_category, chips_provider])







clientside_callback(
     ClientsideFunction(
        namespace='clientside',
        function_name='show_dcc_stored_items'
    ),
    Output("test_store", "children"),
    Output("load_more_number", "children"),
    Output("load_more", "display"),
    


    
    Input("store_items_data", "data"),
   
    Input("filter_chips_category", "value"),
    Input("filter_chips_provider", "value"),
    Input("load_more", "n_clicks"),
    Input("search_item", "value"),
    State('items-in-chart', 'data'),
)
    
    
clientside_callback(
     ClientsideFunction(
        namespace='clientside',
        function_name='show_cart_items'
    ),
    Output("cart-items", "children"),
    Input("items-in-chart", "data"),
    prevent_initial_call=True,

)

clientside_callback(
    """function (cart_icon, open) {
        
        return  ! open
    }""",
  Output("cart-modal", "opened"),
    Input("cart-icon", "n_clicks"),
    State("cart-modal", "opened"),
     prevent_initial_call=True,

)


def product_calls_nested(article):
    clientside_callback(
        """function (value, data) {
        article_code = window.dash_clientside.callback_context.inputs_list[0]['id'].replace('number_input_cart_', "")
        console.log(value, data)
        return window.dash_clientside.no_update
       
      
   

        }""",
        Output('items-in-chart','data', allow_duplicate=True),
        
        Input(f"number_input_cart_{article}", "value"),
        State('items-in-chart', 'data'),
        prevent_initial_call=True,
    )
    
for article in data:
        article = article['product_code']
        product_calls_nested(article)

        
def product_calls(article):
    clientside_callback(
     ClientsideFunction(
        namespace='clientside',
        function_name='update_cart_itmes'
    ),
        Output('items-in-chart','data', allow_duplicate=True),
        Output( f'sum_{article}', 'children'),
       
        Input( f'number_input_card_{article}', 'value'),

        State( f'{article}', 'children'),
        State( f'price_{article}', 'children'),
        State('items-in-chart', 'data'),
        prevent_initial_call =True
    )

for article in data:

    article = article['product_code']
    # print(article)
    product_calls(article)




if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8040, 
                #    dev_tools_ui=False
                   )


   
        #     if (value){
      
        #        console.log(value, 'inside', typeof(value),  typeof(0))

        #     price = price.match(/\d+/)[0] 
        #     data[article_code].quantity=value
        #     data[article_code].total=value*price
         

        # //  console.log(value*price, data)
        #         return  [value*price, data]
        #         }

        #     if (value ==1) {
        #     console.log('if 0')
        #       data[article_code].quantity=value
        #         data[article_code].total=value*1
              
        #         delete data.article_code;
        #         console.log(value, '0',  data, article_code)
               
        #          return  [90, data]
             
        #      }
