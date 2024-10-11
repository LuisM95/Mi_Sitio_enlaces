import reflex as rx 
import front_end.styles.styles as styles

def link_button(title:str, body:str, url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="battery-full",
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items='center'
                )                
            )
        ),
        href=url,
        is_external=True,
        width="100%",
    )
    
   