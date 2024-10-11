import reflex as rx
from front_end.components.link_button import link_button
from front_end.components.title import title
from front_end.styles.styles import Size as Size
def links() -> rx.Component:
    return rx.vstack(
        title("Sitio Web Personal"),
        link_button(
            "Twitter",
            "Cuenta Personal",
            "https://x.com/Kikitho95"
        ),
        link_button(
            "LinkedIn",
            "Informacion Profesional",
            "https://www.linkedin.com/in/luis-enrique-munoz-martel/",
        ),
        link_button(
            "GitHub", 
            "Portafolio de proyectos",
            "https://github.com/LuisM95",
        ),
        link_button(
            "Instagram",
            "Hobbies y viajes",
            "https://www.instagram.com/luismarteel/",
        ),
        width='100%',
        spacing=Size.MEDIUM.value,
    )
