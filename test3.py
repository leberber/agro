
from dash import Dash, dcc, html, Input, Output, ALL, Patch, callback, ctx, no_update, MATCH, State
import dash_mantine_components as dmc



app = Dash(__name__)

data= {
    'huile':['1L', '2L', '3L'],
    'sucre':['1K', '2K', '5K'],
    'tomate':['1C', '2C', '3C']
}

drop_downs = []
for key, value in data.items():
    drop_downs.append(
        dmc.Group(
[  dmc.SegmentedControl(
            id={'type': 'article','index': key},
            data=value
        ),
        html.Div( id={'type': 'articled','index': key}, )]
        )
      
    )

# dmc.Card(
#     children=[
#         dmc.CardSection(
#             dmc.Image(
#                 src="https://images.unsplash.com/photo-1527004013197-933c4bb611b3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=720&q=80",
#                 height=160,
#             )
#         ),
#         dmc.Group(
#             [
#                 dmc.Text("Norway Fjord Adventures", weight=500),
#                 dmc.Badge("On Sale", color="red", variant="light"),
#             ],
#             position="apart",
#             mt="md",
#             mb="xs",
#         ),
#         dmc.Text(
#             "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway",
#             size="sm",
#             color="dimmed",
#         ),
#         dmc.Button(
#             "Book classic tour now",
#             variant="light",
#             color="blue",
#             fullWidth=True,
#             mt="md",
#             radius="md",
#         ),
#     ],
#     withBorder=True,
#     shadow="sm",
#     radius="md",
#     style={"width": 350},
# )
        
app.layout = html.Div(
    
       drop_downs
    
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

app.clientside_callback(
    """function (value,id) {
    //console.log(value,id)
    console.log(window.dash_clientside.callback_context.triggered)
    console.log('------------------------')
    
    return value
    }""",
    Output({'type': 'articled', 'index': MATCH}, 'children'),
    Input({'type': 'article', 'index': MATCH}, 'value'),
    State({'type': 'article', 'index': MATCH}, 'id'),

)


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
    app.run(debug=True)

