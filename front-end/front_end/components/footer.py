import reflex as rx
import datetime
from front_end.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"© 2013 - {datetime.date.today().year} LUISM95 By LUIS MARTEL V1.",
            href="https://github.com/LuisM95",
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            " BUILDING SOFTWARE WITH ♥ FROM EL SALVADOR TO THE WORLD  ",
            font_size=Size.MEDIUM.value,
            margin_top='opx !important'
            ),
        margin_bottom=Size.MEDIUM.value,                
    ),
    
