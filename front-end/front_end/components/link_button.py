import reflex as rx 
import front_end.styles.styles as styles

def link_button(title:str, body:str, url:str, image:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src = image,
                    width = styles.Size.LARGE.value,
                    height = styles.Size.LARGE.value,
                    margin = styles.Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(title, style = styles.button_title_style),
                    rx.text(body, style = styles.button_body_style),
                    align_items = 'center',
                    spacing = styles.Size.ZERO.value,
                    margin = styles.Size.ZERO.value  
                )                
            )
        ),
        href=url,
        is_external=True,
        width="100%",
    )
    
   