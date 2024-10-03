import reflex as rx
from front_end.components.navbar import navbar # import the
from front_end.views.header.header import header
from front_end.views.links.links import links   

class State(rx.State):
    pass 

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        align="center",
        justify="center",
        display="flex",
    )

app = rx.App()
app.add_page(index)
app._compile()