import reflex as rx 
import front_end.styles.styles as styles
from front_end.styles.styles import Size as Size

def title(text:str) -> rx.Component:
    return rx.heading(
        text,
        size='5',
        style=styles.title_styles
    )