import reflex as rx
import front_end.styles.styles as styles
from front_end.styles.styles import Size as Size

def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.text.strong(title, font_weight='bold', color='blue'),
        f' {body}', font_size=Size.MEDIUM.value,
    )