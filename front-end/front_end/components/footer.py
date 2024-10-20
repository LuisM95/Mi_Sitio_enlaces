import reflex as rx
import datetime

from front_end.styles.styles import Size as Size
from front_end.styles.colors import TextColor as Textcolor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"), #crear y cambiar logo
        rx.link(
            f"© 2013 - {datetime.date.today().year} LUISM95 By LUIS MARTEL V1.",
            href = "https://github.com/LuisM95",
            is_external = True,
            font_size = Size.MEDIUM.value
        ),
        rx.text(
            " BUILDING SOFTWARE WITH ♥ FROM EL SALVADOR TO THE WORLD  ",
            font_size = Size.MEDIUM.value,
            margin_top = Size.ZERO.value 
            ),
        margin_bottom = Size.MEDIUM.value,
        padding_bottom = Size.MEDIUM.value,
        color = Textcolor.FOOTER.value
    ),
    
