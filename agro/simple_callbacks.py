            
import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify as icon

paper = dmc.Paper(
        children = [



dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Button("Load from database"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Button("Load from database"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),
dmc.Text("Default text", size="md"),


                
        ]
)

footer_style_dict = {
    'color' : '#A519C7',

}
footer_icon_with = 30
footer_icon_color = '#A519C7'
    
footer  = dmc.Paper(
    className = 'footer',
    children =[
        dmc.Group(
            position = 'apart',
            children = [
                dmc.Center(
                    children = [
                        dmc.Stack(
                            align="center",
                            spacing="xs",
                            children = [
                                dmc.ActionIcon(icon(icon="tabler:shopping-bag", width= footer_icon_with, color = footer_icon_color), variant='transparent', id = ''),
                                dmc.Text("Shop"),
                            ]
                        )
                    ]
                ),   
                dmc.Center(
                    children = [
                        dmc.Stack(
                            align="center",
                            spacing="xs",
                            children = [
                                dmc.ActionIcon(icon(icon="ic:sharp-person-outline", width= footer_icon_with, color = footer_icon_color), style = footer_style_dict, variant='transparent'),
                                dmc.Text("Account")
                            ]
                        )
                    ]
                ), 
                dmc.Center(
                    children = [
                        dmc.Stack(
                            align="center",
                            spacing="xs",
                            children = [
                                dmc.ActionIcon(icon(icon="fluent:cart-24-regular",  width= footer_icon_with, color = footer_icon_color), style = footer_style_dict, variant='transparent'),
                                dmc.Text("Cart"),
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

header = dmc.Paper(
    className = 'header',
    children =[
        dmc.Burger(),
        dmc.ActionIcon(
            id = 'theme_switcher',
            n_clicks=0, 
            variant= "transparent",
            style= {'float':'right'},
            children = [
                icon(icon="ic:baseline-light-mode", width=40, color='gold')
                ]
        )
    ]
)