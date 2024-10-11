import reflex as rx
import front_end.styles.styles as styles

from front_end.components.navbar import navbar # import the
from front_end.views.header.header import header
from front_end.views.links.links import links   
from front_end.components.footer import footer
from front_end.styles.styles import Size as Size

class State(rx.State):
    pass 

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width= styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
                 
            ),
        ),
        footer(),
    )




app = rx.App(
    style = styles.BASE_STYLE
)
app.add_page(index)
app._compile()