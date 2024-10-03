import reflex as rx
from front_end.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitter", "https://x.com/Kikitho95"),
        link_button("LinkedIn", "https://www.linkedin.com/in/luis-enrique-munoz-martel/"),
        link_button("GitHub", "https://github.com/LuisM95"),
        link_button("Instagram", "https://www.instagram.com/luismarteel/"),        
    )
