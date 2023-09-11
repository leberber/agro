
from dash import Dash, dcc, html, Input, Output, ALL, Patch, callback, ctx

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Button("Add Filter", id="add-filter-btn", n_clicks=0),
        html.Div(id="dropdown-container-div", children=[]),
        html.Div(id="dropdown-container-output-div"),
        html.Div(
            id = 'output',
            children=[
                'df'
            
            ]
        ),
    ]
)
    #   if (!(typeof id === 'string' || id instanceof String)) {
    #         id = JSON.stringify(id, Object.keys(id).sort());
    #     };

@callback(
    Output("dropdown-container-div", "children"), Input("add-filter-btn", "n_clicks"),
    prevent_initial_call=True
)
def display_dropdowns(n_clicks):
    patched_children = Patch()
    new_dropdown = dcc.Dropdown(
        ["NYC", "MTL", "LA", "TOKYO"],
        id={"type": "city-filter-dropdown", "index": n_clicks},
    )
    patched_children.append(new_dropdown)
    return patched_children


@callback(
    Output("dropdown-container-output-div", "children"),
    Input({"type": "city-filter-dropdown", "index": ALL}, "value"),
    prevent_initial_call=True
)
def display_output(values):
    print(values)
    print(ctx.triggered)
    print('------------------------')
    print(html.Div(
        [html.Div(f"Dropdown {i + 1} = {value}") for (i, value) in enumerate(values)]
    ))
    return html.Div(
        [html.Div(f"Dropdown {i + 1} = {value}") for (i, value) in enumerate(values)]
    )

app.clientside_callback(
    """function (n,s) {
    console.log(n)
    console.log(window.dash_clientside.callback_context.triggered)
    console.log('------------------------')
    
    return window.dash_clientside.no_update
    }""",
    Output("output", "children"), 
    Input({"type": "city-filter-dropdown", "index": ALL}, "value"),
    Input("add-filter-btn", "n_clicks"),
    prevent_initial_call=True
)

if __name__ == "__main__":
    app.run(debug=True)

# from dash import html, Output, Input, Dash, no_update, dcc
# import json
# import time
# import dash_mantine_components as dmc

# app = Dash(__name__)
# app.layout = html.Div(

#     [
#         html.Div(
#             id = 'output',
#             children=[
            
#             ]
#         ),
#         html.Button('button', id ='btn'),

#     ]
# )


# app.clientside_callback(
#     """function (n) {
#     return n
#     }""",
#     Output("output", "children"), 
#     Input("btn", "n_clicks")
# )



# if __name__ == "__main__":
#     app.run_server(debug=True)


