import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="LM",variant="soft", size="6", radius="full"),
        rx.text("@Kikitho95"),
        rx.text("Hola Mi Nombre es Luis Martel"),
        rx.text("""Soy Luis Martel Estudiante de Software, soy un estudiante apasionado por el mundo de la tecnología,
                 actualmente cursando una carrera técnica en servicios en la nube.
                 Estoy constantemente aprendiendo y creciendo."""),
        align="center",
        justify="center",
        display="flex",
        )