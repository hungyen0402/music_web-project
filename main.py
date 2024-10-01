import flet as ft
from flet import*
from unidecode import unidecode

fake_music = [
    'Nơi Này Có Anh',
    'Thằng Điên',
    'Lan Man',
    'Die With A Smile',
    'Thich Thich',
    'Nơi này có em',
    'Thang kho',
    'Tram nam khong quen'
]

def main(page : Page):
    page.title = 'Music Player 1.0.1'
    page.bgcolor = 'black'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window.width = 350


    # Search Bar  
    def _bar_search():

        # Return result search
        result_search = Container(
            visible=False,
            content=Column(
                [ Text('Result Music', weight='bold', color = 'black'),
                Column()]
            ) # sửa chữ thành màu đen 
        )
        # Search Music Name
        def change_music(e):
            if e.data:
                result_search.content.controls[1].controls.clear()
                result_search.visible = True
                search_music = unidecode(e.data.lower())
                matching_music = [music for music in fake_music if search_music in unidecode(music.lower())]
                match_music = '\n'.join(matching_music)
                result_search.content.controls[1].controls.append(
                   
                        ListTile(
                            title=Text(match_music, size=17, style = 'italic', color = 'black'),
                            on_click=lambda e : print(match_music)
                            
                        ) 
                    
                )
            else:
                result_search.visible = False
            page.update()

        # Search Bar
        bar_search = SearchBar(
            view_elevation=5,
            bar_bgcolor='lightblue100',# màu nền 
            bar_overlay_color='black', # màu phủ 
            bar_hint_text='Search',
            view_hint_text='Search anything',
            bar_leading=ft.IconButton(icon='search'),
            on_change=change_music,
            full_screen= True
        )
        return Column([
            bar_search,
            result_search,
        ])
    # Menu Tabs
    def _TapMenu():
       
        mytab = Row(
            alignment='spaceBetween',
            controls=[
                IconButton(icon='Menu', 
                           icon_color='white',
                           on_click=lambda e : print('Menu')
                           ),
                IconButton(icon='Home', icon_color='white'),
                IconButton(icon='Favorite', icon_color='white'),
                IconButton(icon='Person', icon_color='white'),
            ]
        )
        return mytab
    # Background
    top = Container(
        alignment=ft.alignment.center,
        width=300,
        height=600,
        bgcolor='pink',
        content=Stack(
            controls=[
                Column(
                    width=280,
                    height=580,
                    controls=[
                        # Search and Image Screen
                        Container(
                            alignment=ft.alignment.top_center,
                            content=Stack(
                                controls=[
                                    _bar_search(),
                                    # Image(
                                    #     width=300,
                                    #     height=530,
                                    #     src='Images/Logo.png',
                                    #     fit='cover',
                                    # ),
                    
                                ]
                            )
                        ),
                        # Menu Tabs
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


ft.app(target=main, view=AppView.WEB_BROWSER, port=2905)