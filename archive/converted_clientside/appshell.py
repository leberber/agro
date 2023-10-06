import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify as icon
from utils import id_dict

footer_icon_with = 30
footer_icon_color = '#A519C7'

def footer_action_link (_id, _index, _icon, is_default=False):
    icon_text_size = 'xs'
    icon_and_text_color = {}
    if is_default:
        icon_and_text_color = {'color':'rgb(34, 139, 230)'}

    return  dmc.Center(
                children = [
                    dmc.Stack(
                        align="center",
                        children = [
                            dmc.ActionIcon(
                                id = id_dict (f'{_id}', _index),
                                variant='transparent',  
                                style = icon_and_text_color,
                                children = [
                                    icon(icon=_icon, width = footer_icon_with)
                                ]
                            ),
                            dmc.Text(_index.capitalize(), size=icon_text_size, style = icon_and_text_color, id = id_dict (f'{_id}_text', _index)),
                        ]
                    )
                ]
            ) 
    
footer  = dmc.Paper(
    className = 'footer',
    shadow='xl',
    children =[
        dmc.Group(
            position = 'apart',
            children = [
                footer_action_link ("page_switcher_action", "shop", 'tabler:shopping-bag', is_default=True),
                footer_action_link ("page_switcher_action", "account", 'ic:sharp-person-outline'),
                footer_action_link ("page_switcher_action", "cart", 'ic:outline-shopping-cart')
            ]
        )
    ]
)

header = dmc.Paper(
    className = 'header',
    shadow='xs',
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