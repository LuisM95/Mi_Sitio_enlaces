import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(f"© 2013 - {datetime.date.today().year} LUISM95 By LUIS MARTEL V1.",
                href="https://github.com/LuisM95",
                is_external=True),
        rx.text(" BUILDING SOFTWARE WITH ♥ FROM EL SALVADOR TO THE WORLD  ")        
    )
