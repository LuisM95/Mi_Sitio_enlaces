import reflex as rx

from front_end.styles.styles import Size as Size
from front_end.styles.colors import TextColor as TextColor
from front_end.styles.colors import Color as Color

def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.text.strong(
            title, 
            font_weight='bold', 
            color = Color.PRIMARY.value
        ),
        f' {body}', 
        font_size=Size.MEDIUM.value,
        color = TextColor.BODY.value
    )