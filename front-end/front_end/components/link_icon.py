from front_end.styles.styles import Size as Size

import reflex as rx

#import front_end.styles.styles as styles

def link_icon(image: str, url:str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width = Size.DEFAULT.value
        ),
        href=url,
        is_external=True
    )