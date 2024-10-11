import reflex as rx
from front_end.styles.styles import Size as Size

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Luis Martel",
        ),
        position="sticky",
        bg="lightgray",
        padding_x =Size.DEFAULT.value ,
        padding_y= Size.SMALL.value,
        z_index="999",
        color="black",
    )
