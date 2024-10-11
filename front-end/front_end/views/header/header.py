import reflex as rx
from front_end.components.link_icon import link_icon
from front_end.styles.styles import Size as Size
from front_end.components.info_text import info_text

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="LM",variant="soft", size="7", radius="full"),
            rx.vstack(
                rx.heading(
                    "Luis Martel",
                    size='7'
                    ),
                rx.text(
                    "@Kikitho95",
                    margin_top='0px !important',
                    ),
                    rx.hstack(
                        link_icon("https://x.com/Kikitho95"),
                        link_icon("https://github.com/LuisM95")
                    ),
                    align_items='start',
            ),        
            spacing=Size.DEFAULT.value,
        ),
        rx.flex(
            info_text("+3", " Años como Autodidacta!"),
            rx.spacer(),
            info_text("+3", " Años como Autodidacta!"),
            rx.spacer(),
            info_text("+3", " Años como Autodidacta!"),
            width='100%'
        ),
        rx.text("""Soy Luis Martel Estudiante de Software, soy un estudiante apasionado por el mundo de la tecnología,
                 actualmente cursando una carrera técnica en servicios en la nube.
                 Estoy constantemente aprendiendo y creciendo."""
                ),
            spacing=Size.DEFAULT.value,
            align_items='start',
        )