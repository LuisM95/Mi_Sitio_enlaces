from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
import reflex as rx

#Constantes
MAX_WIDTH = "600px"

#sizes
class Size(Enum):
    ZERO = '0px !important'
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = "0.8em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"

#Styles 

BASE_STYLE = {
    'background': Color.BACKGROUND.value,
    rx.button: {
        'width': '100%',
        'height': '100%',
        'display': 'block',
        'color': TextColor.HEADER.value,
        'paddig' : Size.SMALL.value,
        'border_radius': Size.DEFAULT.value,
        'background': Color.CONTENT.value,
        '_hover': {
            'background': Color.SECONDARY.value
        },
    },
    rx.link:{
        'text_decoration':'none',
        '_hover': {}
    }
}

title_styles = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    color= TextColor.HEADER.value
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    color =  TextColor.HEADER.value
)

button_body_style = dict(
    font_size=Size.SMALL.value,
    color =  TextColor.BODY.value
)

