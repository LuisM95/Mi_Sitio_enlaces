import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="LM",variant="soft", size="6", radius="full"),
        rx.text("@Kikitho95"),
        rx.text("Hola Mi NMombre es Luis Martel"),
        rx.text("""Soy Luis Martel Estudiante de Software, soy un estudiante apasionado por el mundo de la tecnología,'\n'
                 actualmente cursando una carrera técnica en servicios en la nube. '\n'
                 Estoy constantemente aprendiendo y creciendo."""),
        align="center",
        justify="center",
        display="flex",
        )