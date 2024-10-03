import reflex as rx 

def link_button(text:str, url:str) -> rx.Component:
    return rx.link(
        rx.button(text),
        href=url,
        underline="auto",
        is_external=True,
    )