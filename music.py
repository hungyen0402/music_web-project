import flet as ft
from flet import *

def main(page: Page):
    page.title = 'Music Player 1.0.1'
    page.bgcolor = 'black'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window.width = 350

    playlist = [
        "audio/NoiNayCoAnh-SonTungMTP.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
    ]
    current_song_index = 0

    audio = ft.Audio(
        src=playlist[current_song_index], 
        volume=1, 
        autoplay=False,
        on_loaded=lambda _: update_total_time()
    )

    def play(e):
        audio.play()
        play_button.visible = False
        pause_button.visible = True
        play_button.update()
        pause_button.update()

    def pause(e):
        audio.pause()
        play_button.visible = True
        pause_button.visible = False
        play_button.update()
        pause_button.update()

    def next_song(e):
        nonlocal current_song_index
        current_song_index = (current_song_index + 1) % len(playlist)
        audio.src = playlist[current_song_index]
        play_button.visible = False
        pause_button.visible = True
        audio.autoplay = True
        audio.update()
        play_button.update()
        pause_button.update()
        update_total_time()

    def prev_song(e):
        nonlocal current_song_index
        current_song_index = (current_song_index - 1) % len(playlist)
        audio.src = playlist[current_song_index]
        play_button.visible = False
        pause_button.visible = True
        audio.autoplay = True
        audio.update()
        play_button.update()
        pause_button.update()
        update_total_time()

    def update_total_time():
        total_time = audio.get_duration()/1000
        total_time_text.value = f"{int(total_time)//60}:{int(total_time % 60):02d}"
        total_time_text.update()

    def back(e):
        audio.pause()

    play_button = ft.IconButton(icon=ft.icons.PLAY_ARROW, on_click=play, visible=True, icon_color="black")
    pause_button = ft.IconButton(icon=ft.icons.PAUSE, on_click=pause, visible=False, icon_color="black")
    next_button = ft.IconButton(icon=ft.icons.SKIP_NEXT, on_click=next_song, icon_color="black")
    prev_button = ft.IconButton(icon=ft.icons.SKIP_PREVIOUS, on_click=prev_song, icon_color="black")
    back_button = ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=back, icon_color="black")
    slider = ft.Slider(min=0, thumb_color="transparent", on_change_end=None)
    current_time_text = ft.Text("00:00", color="black")
    total_time_text = ft.Text("00:00", color="black")

    main_container = ft.Container(
        alignment=ft.alignment.center,
        width=300,
        height=600,
        bgcolor=ft.colors.PURPLE_100,
        content=ft.Column(
            controls=[
                audio,
                ft.Row(
                    controls=[back_button],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Row(
                    controls=[
                        ft.Text("       Nơi Này Có Anh", color='black'),
                    ],
                ),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Stack(
                        controls=[
                            ft.Image(
                                width=250,
                                height=300,
                                src='Images/image1.jpg',
                                border_radius=10,
                            ),
                        ],
                    ),
                ),
                ft.Column(
                    controls=[
                        ft.Row(
                            
                            controls=[
                                current_time_text,
                                ft.Text("                                   "),
                                total_time_text,
                            ],
                             alignment=ft.MainAxisAlignment.SPACE_EVENLY
                        ),
                        slider,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                ft.Row(
                    controls=[
                        prev_button,
                        play_button,
                        pause_button,
                        next_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Container(
                    height=30,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        border_radius=35,
    )
    page.add(main_container)

ft.app(target=main)
