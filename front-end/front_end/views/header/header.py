import reflex as rx
import front_end.constants as const

from front_end.components.link_icon import link_icon
from front_end.styles.styles import Size as Size
from front_end.components.info_text import info_text
from front_end.styles.colors import TextColor as TextColor
from front_end.styles.colors import Color as Color

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="LM",variant="soft", size="7", radius="full"),
            rx.vstack(
                rx.heading(
                    "Luis Martel",
                    size='4',
                    color = TextColor.HEADER.value
                    ),
                rx.text(
                    "@Kikitho95",
                    margin_top = Size.ZERO.value ,
                    color = TextColor.BODY.value
                    ),
                    rx.hstack(
                        link_icon(
                            const.TWITTER_X_URL,
                            "/assets/icons/square-x-twitter.svg"
                            ),
                        link_icon(
                            const.GITHUB_URL,
                            "/square-github.svg"
                            ),
                            spacing='3'
                    ),
                    align_items='start',
            ),        
            spacing='5',
        ),
        rx.flex(
            info_text("+3", " Años como Autodidacta!"),
            rx.spacer(),
            info_text("+3", " Años como Autodidacta!"),
            rx.spacer(),
            info_text("+3", " Años como Autodidacta!"),
            width='100%'
        ),
        rx.text(
                """Soy Luis Martel Estudiante de Software, soy un estudiante apasionado por el mundo de la tecnología,
                actualmente cursando una carrera técnica en servicios en la nube.
                Estoy constantemente aprendiendo y creciendo.""", 
                color = TextColor.BODY.value 
            ),
            spacing='5',
            align_items='start',
        )