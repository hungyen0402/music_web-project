from flet import *
import flet as ft


def main(page : Page):
    bgcolor = "#710B46"
    primary = "#41005E"
    secondary = "#F1DEFA"
    tertiary = "#B19FF9"

    page.title = 'Music Player'
    page.window.width = 400
    page.window.height = 700
    page.horizontal_alignment = 'center'
    page.theme_mode = 'dark'

    def click_search(e):
        home_screen.content.controls[1].focus()
        page.update()
        
    home_screen = Container(
        width=350,
        height=650,
        border_radius=25,
        bgcolor=bgcolor,
        content=Column(
            controls=[
                # First Row in Page - Title and Search Icon 
                Row(alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        Container(
                            width=50
                        ),
                        Text(value='Music Player', 
                             color=ft.colors.WHITE,
                             weight='bold',
                             italic=True, size=30,
                        ),

                        Container(
                            alignment=ft.alignment.bottom_center,
                           
                            width=300,
                            height=50,
                            content=Stack(
                                controls=[
                                    _TapMenu(),
                                ]
                            ),
                            padding=1,
                            bgcolor='pink',

                        ),
                    ]
                )
            ],
        ),

        border_radius=35,
    )
    page.add(top)


ft.app(target=main)