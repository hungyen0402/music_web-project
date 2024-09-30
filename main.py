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
        border_radius=35,
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
                            width=50
                        ),
                    ]
                ),
                # Second Row in Page - Search Box
                ft.TextField(
                    filled= True,
                    prefix_icon=ft.icons.SEARCH,
                    hint_text='Search',
                    width=400,
                    border_width=2,
                    border_radius=20,
                    focused_color=secondary,
                    focused_border_color=secondary,
                    autofocus=False,
                ),
            
                # Result search name music
                ft.Column(
                    width=400,
                    height=480,
                    scroll=ScrollMode.AUTO,
                    controls=[]
                ),

                # Menu Row
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        IconButton(icon=ft.icons.HOME, icon_color=ft.colors.WHITE,
                                   icon_size=30),

                        IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE,
                                   icon_size=30,
                                   on_click=click_search
                                   ),

                        IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE,
                                   icon_size=30),
                    ]
                )
            ]
        )
    )

    page.add(home_screen
             )

ft.app(target=main)