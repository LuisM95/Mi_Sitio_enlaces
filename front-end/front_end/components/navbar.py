import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Luis Martel",
            height="40px",
        ),
        position="sticky",
        bg="lightblue",
        padding_x="16px",
        padding_y="8px",
        z_index="999",
        color="gray",
    )
