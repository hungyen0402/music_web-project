import flet as ft
from flet import*

def main(page : Page):
    page.title = 'Test App'
    page.bgcolor = 'black'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    def _c():
        c = Container(
                    width=300,
                    height=80,
                    alignment = ft.alignment.top_center,
                    content=SearchBar(
                        view_elevation=5,
                        bar_bgcolor='lightblue100',
                        bar_overlay_color='white',
                        bar_hint_text='Search',
                        view_hint_text='Search anything',
                        bar_leading=ft.IconButton(icon='search'),
                    ),
                    padding=5,
                    margin=10,
                    # gradient=LinearGradient(
                    #     begin=alignment.bottom_left,
                    #     end=alignment.bottom_right,
                    #     colors=['lightblue600', 'lightblue900'],
                    # ),
                    border_radius=35,
                )
        return c
    top = Container(
        alignment=ft.alignment.center,
        width=300,
        height=600,
        bgcolor='pink',
        content=Stack(
            width=300,
            height=600,
            controls=[_c()],
            
        ),
        border_radius=35,
    )
    page.add(top)


ft.app(target=main)