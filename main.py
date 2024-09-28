import flet as ft
from flet import*
fake_music = [
    'Nơi Này Có Anh',
    'Thằng Điên',
    'Lan Man',
    'Die With A Smile',
    'Thich Thich',
]

def main(page : Page):
    page.title = 'Music Player 1.0.1'
    page.bgcolor = 'black'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
   

    # Search Bar  
    def _bar_search():

        # Return result search
        result_search = Container(
            visible=False,
            content=Column(
                [ Text('Result Music', weight='bold'),
                Column()]
            )
        )
        # Search Music Name
        def change_music(e):
            if e.data:
                result_search.content.controls[1].controls.clear()
                result_search.visible = True
                search_music = e.data.lower()
                matching_music = [music for music in fake_music if search_music in music.lower()]
                match_music = '\n'.join(matching_music)
                result_search.content.controls[1].controls.append(
                   
                        ListTile(
                            title=Text(match_music, size=17, weight='bold'),
                            on_click=lambda e : print(match_music)
                            
                        ) 
                    
                )
            else:
                result_search.visible = False
            page.update()

        # Search Bar
        bar_search = SearchBar(
            view_elevation=5,
            bar_bgcolor='lightblue100',
            bar_overlay_color='white',
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
    

    # Background
    top = Container(
        alignment=ft.alignment.center,
        width=300,
        height=600,
        bgcolor='pink',
        content=Stack(
            width=280,
            height=580,
            controls=[
                        Image(
                            width=300,
                            height=600,
                            src='Images/Logo.png',
                            fit='cover',
                        ),
                        _bar_search(),
                      ],
        ),

        border_radius=35,
    )
    page.add(top)


ft.app(target=main)