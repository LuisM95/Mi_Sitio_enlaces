from enum import Enum
import reflex as rx

#Constantes
MAX_WIDTH = "600px"

#sizes
class Size(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = '0.8em'
    BIG = "2em"

#Styles 

BASE_STYLE = {
    rx.button: {
        'width': '100%',
        'height': '100%',
        'display': 'block',
        'paddig' : Size.SMALL.value,
        'border_radius': Size.DEFAULT.value
    },
    rx.link:{
        'text_decoration':'none',
        '_hover': {}
    }
}

title_styles = dict(
    width="100%",
    padding_top=Size.DEFAULT.value
)

button_title_style = dict(
    font_size=Size.DEFAULT.value
)

button_body_style = dict(
    font_size=Size.SMALL.value
)

