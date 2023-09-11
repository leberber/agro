
from dash import Dash, dcc, html, Input, Output, ALL, Patch, callback, ctx, no_update, MATCH, State
import dash_mantine_components as dmc



app = Dash(__name__)

data= {
    'huile':{'1L':'140', '2L':'280', '5L':'500'},
    'sucre':{'1K':'40', '2K':'80', '5L':'150'},
   
}
# dmc.Paper(artile_type, style= {'border':'3px solid red'}) id={'type': 'articled','index': key},
article_card = []
for article, value in data.items():
    artile_type = []
    for article_type, value in value.items():
        artile_type.append(
            dmc.Grid(
                children=[
                    dmc.Col(dmc.Text(article_type,  id={'type': f'name_{article}_{article_type}','index': article}), span=3,  className='item_type_column'),
                    dmc.Col(dmc.Text(value, id={'type': f'price_{article}_{article_type}','index': article}), span=3,  className='item_type_column'),
                    dmc.Col(dmc.NumberInput( hideControls = True, className='item_type_number_input', id={'type': f'number_input_{article}_{article_type}','index': article}), span=3, className='item_type_column'),
                    
                    dmc.Col(dmc.Text(value, id={'type': f'somme_{article}_{article_type}','index': article}), span=3,  className='item_type_column'),
                ],
                justify="center",
                align="center",
                gutter="xl",
                className='item_type_grid'

            ),
    )
    article_card.append(
        dmc.Card(
            children=[
                dmc.CardSection(
                    dmc.Image(
                        src=f"assets/{article}.png",
                    )
                ),
                dmc.Group(
                    [
                        dmc.Text(f"{article}", weight=500),
                        dmc.Badge("On Sale", color="red", variant="light"),
                    ],
                    position="apart",
                    mt="md",
                    mb="xs",
                ),
                dmc.Paper(artile_type, ),

                dmc.Button(
                    "Add to Cart",
                    variant="light",
                    color="blue",
                    fullWidth=True,
                    mt="md",
                    radius="md",
                ),
            ],
            withBorder=True,
            shadow="sm",
            radius="md",
            style={"width": 396},
        )
    )


        
app.layout = html.Div(
    
       article_card
    
)

# @callback(
#     Output({'type': 'articled', 'index': ALL}, 'children'),
#     Input({'type':'article', 'index': ALL}, 'value'),
#  prevent_initial_call = True
# )
# def update_segments( values ):
#     print(ctx.triggered)
#     return ['2L',no_update, '3C']

# @callback(
#     Output({'type': 'articled', 'index': ALL}, 'children'),
#     Input({'type':'article', 'index': ALL}, 'value'),
#  prevent_initial_call = True
# )
# def update_segments( values ):
#     print(ctx.triggered)
#     return ['2L',no_update, '3C']

# @callback(
#     Output({'type': 'articled', 'index': MATCH}, 'children'),
#     Input({'type': 'article', 'index': MATCH}, 'value'),
#     State({'type': 'article', 'index': MATCH}, 'id'),
# )
# def display_output(value, id):
#     print(value, id)
#     return value

# app.clientside_callback(
#     """function (value,id) {
#     //console.log(value,id)
#     console.log(window.dash_clientside.callback_context.triggered)
#     console.log('------------------------')
    
#     return value
#     }""",
#     Output({'type': 'articled', 'index': MATCH}, 'children'),
#     Input({'type': 'article', 'index': MATCH}, 'value'),
#     State({'type': 'article', 'index': MATCH}, 'id'),

# )


# @callback(
#     Output("dropdown-container-div", "children"), Input("add-filter-btn", "n_clicks"),
#     prevent_initial_call=True
# )
# def display_dropdowns(n_clicks):
#     patched_children = Patch()
#     new_dropdown = dcc.Dropdown(
#         ["NYC", "MTL", "LA", "TOKYO"],
#         id={"type": "city-filter-dropdown", "index": n_clicks},
#     )
#     patched_children.append(new_dropdown)
#     return patched_children


# @callback(
#     Output("dropdown-container-output-div", "children"),
#     Input({"type": "city-filter-dropdown", "index": ALL}, "value"),
#     prevent_initial_call=True
# )
# def display_output(values):
#     print(values)
#     print(ctx.triggered)
#     print('------------------------')
#     print(html.Div(
#         [html.Div(f"Dropdown {i + 1} = {value}") for (i, value) in enumerate(values)]
#     ))
#     return html.Div(
#         [html.Div(f"Dropdown {i + 1} = {value}") for (i, value) in enumerate(values)]
#     )

# app.clientside_callback(
#     """function (n,s) {
#     console.log(n)
#     console.log(window.dash_clientside.callback_context.triggered)
#     console.log('------------------------')
    
#     return window.dash_clientside.no_update
#     }""",
#     Output("output", "children"), 
#     Input({"type": "city-filter-dropdown", "index": ALL}, "value"),
#     Input("add-filter-btn", "n_clicks"),
#     prevent_initial_call=True
# )

if __name__ == "__main__":
    app.run(app.run_server(debug=True, host='0.0.0.0', port=8050))

