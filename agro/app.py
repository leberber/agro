

from dash import Dash, dcc, html, Input, Output, State, ALL,  MATCH, callback, ctx, no_update,   clientside_callback, ClientsideFunction
from dash_iconify import DashIconify as icon
import dash_mantine_components as dmc

from appshell import  footer, header
from utils import id_dict
# from pages.shop import  shop

app = Dash(
    __name__,
    external_stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
    ],
)

def shop_card(image_path):
    return dmc.Grid(
            className = 'card-grid',
            justify = 'center',
            
            children = [
                dmc.Col(
                className = 'card-image-column',
                p = 5,
                    span = 3,
                    children = [
                        dmc.Image(src=image_path, className = 'card-image')  
                    ]
                ),
                dmc.Col(
                    span = 'auto',
                    children = [
                        dmc.Grid(
                            children=[
                                dmc.Col(dmc.Text("Confiture Matina Abricot", size="lg", weight=500,), span=7, px = 0),
                                dmc.Col(dmc.Text("1687.24 DA", size="md", weight=900, align="right" , color = 'green'), span=5,  px = 0),
                            ],
                        ),
                        dmc.Grid(
                            justify = 'flex-end',
                            children=[
                                dmc.Col( 
                                span=4, px = 0,
                                    children =[
                                        dmc.Stack(
                                            align="center",
                                            children = [
                                                dmc.NumberInput(min=0, w = 50, size = 'lg', hideControls =  True, className='card-quantity-input'),
                                                dmc.Text("Quantity", size="md", weight=600, align="right" ),

                                            ]
                                        ) 
                                    ]
                                ),
                                dmc.Col(    
                                    span=5, px = 0,
                                    children =[
                                        dmc.Stack(
                                            align="center",
                                            children = [
                                                dmc.Text("0 DA", size="md", lh = '30px', weight='bolder'),
                                                dmc.Text("Total", size="md", weight=600, align="right" ),                                               

                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                    ]
                )
            ]
        )
shop = dmc.Paper(
    id = id_dict('page_layout_id', 'shop'),
    style = {'display':'block'},
    className = 'page',

    children = [
        shop_card("/assets/Ramy_Délice.png" ), 
        shop_card("/assets/Ramy_Délice300_360.jpg" ), 
        shop_card("/assets/Ramy_Délice300_420.jpg" ), 
        shop_card("/assets/Ramy_Délice_300_500.jpg" ), 
        shop_card("/assets/Confitures_MATINA_Abricot.png" ), 
        shop_card("/assets/Couscous_Gros_300_300.png" ), 
        shop_card("/assets/Couscous_Gros2.png" ), 

    ]
)

account = dmc.Paper(
    id = id_dict('page_layout_id', 'account'),
    className = 'page',
    style = {'display':'none'},
    children = [
        dmc.Text("account_page", size="md", color ='yellow'),
        dmc.Text("account_page", size="md"),
        dmc.Text("account_page", size="md"),
        dmc.Text("Default text", size="md"),
        dmc.Text("Default text", size="md"),
    ]
)

cart = dmc.Paper(
    id = id_dict('page_layout_id', 'cart'),
    style = {'display':'none'},
    className = 'page',
    children = [
        dmc.Text("cart_page", size="md", color ='blue'),
        dmc.Text("cart_page", size="md"),
        dmc.Text("cart_page", size="md"),
        dmc.Text("Default text", size="md"),
        dmc.Text("Default text", size="md"),

    ]
)
content = dmc.Container(
    className = 'content',
    children = [
        shop,
        account,
        cart,
    ]
)
   
app.layout = html.Div(
    children=[  
        dmc.MantineProvider(
            theme={"primaryColor": "indigo"},
            id = 'theme',
            withGlobalStyles=True,
            children=[
                html.Div(
                    children = [
                        header,
                        content,
                        footer
                    ]
                )
            ]
        ) 
    ]
)

clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='page_switcher'
    ),
    Output({"type": "page_layout_id", "index": ALL}, "style"), 
    Output({"type": "page_switcher_action", "index": ALL}, "style"),
    Output({"type": "page_switcher_action_text", "index": ALL}, "style"),
    Input({"type": "page_switcher_action", "index": ALL}, "n_clicks"),
    prevent_initial_call=True
)

clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='theme_switcher'
    ),
    Output("theme", "theme"),
    Output("theme_switcher", "children"),
    Input("theme_switcher", "n_clicks"),
    prevent_initial_call=True
)

if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8050 )

