import reflex as rx

import front_end.constants as const

from front_end.components.link_button import link_button
from front_end.components.title import title
from front_end.styles.styles import Size as Size


def links() -> rx.Component:
    return rx.vstack(
        title("Sitio Web Personal"),
        link_button(
            "Twitter",
            "Cuenta Personal",
            const.TWITTER_X_URL,
            "/icons/square-x-twitter.svg"
        ),
        link_button(
            "LinkedIn",
            "Informacion Profesional",
            const.LINKEDIN_URL,
            "/icons/linkedin.svg"
        ),
        link_button(
            "GitHub", 
            "Portafolio de codigos de proyectos",
            const.GITHUB_URL,
            "/icons/square-github.svg"
        ),
        link_button(
            "Instagram",
            "Hobbies y viajes",
            const.INSTAGRAM_URL,
            "/icons/square-instagram.svg"
        ),
        width='100%',
        spacing='6',
    )
