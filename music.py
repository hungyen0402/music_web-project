import flet as ft
from flet import *
import time
import threading

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
        on_loaded=lambda _: update_total_time(),
        on_position_changed=lambda _: update_current_time()
    )

    def play(e):
        audio.resume()
        play_button.visible = False
        pause_button.visible = True
        play_button.update()
        pause_button.update()
        threading.Thread(target=update_slider).start()

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
        total_time = audio.get_duration() / 1000
        total_time_text.value = f"{int(total_time) // 60}:{int(total_time % 60):02d}"
        total_time_text.update()
        slider.max = total_time
        slider.update()

    def update_current_time():
        current_time = audio.get_current_position() / 1000
        current_time_text.value = f"{int(current_time) // 60}:{int(current_time % 60):02d}"
        current_time_text.update()
        slider.value = current_time
        slider.update()
        if current_time >= audio.get_duration() / 1000 - 1:
            audio.pause()
            next_song(None)

    def update_slider():
        while audio.get_current_position() < audio.get_duration():
            current_time = audio.get_current_position() / 1000
            slider.value = current_time
            slider.update()
            time.sleep(0.1)

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
            [
                audio,
                ft.Row(
                    controls=[back_button],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            width=270,
                            height=270,
                            shadow=ft.BoxShadow(
                                spread_radius=6,
                                blur_radius=10,
                                color=ft.colors.with_opacity(0.35,"black"),
                            ),
                            image_fit="cover",
                            content=ft.Stack(
                                controls=[
                                    ft.Image(
                                        src='Images/image1.jpg',
                                        fit=ft.ImageFit.CONTAIN,
                                        border_radius=ft.border_radius.all(10)
                                    ),
                                ],
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Divider(
                    height=10,
                    color="transparent"
                ),
                ft.Column(
                    [
                        ft.Row(
                            controls=[
                                ft.Text("  "+"Nơi Này Có Anh",size=18,weight=ft.FontWeight.BOLD,color="black"),
                            ],
                        ),
                        ft.Row(
                            controls=[
                                ft.Text("   "+"Sơn Tùng MTP",size=15,opacity=0.81,color="grey"),
                            ],
                        ),
                    ],
                    spacing=1,
                ),
                ft.Divider(
                    height=10,
                    color="transparent"
                ),
                ft.Column(
                    [
                        ft.Row(
                            controls=[
                                current_time_text,
                                ft.Text("                                               "),
                                total_time_text,
                            ],
                             alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        ),
                        slider,
                        ft.Row(
                            [
                                prev_button,
                                play_button,
                                pause_button,
                                next_button
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY
                        ),
                    ],
                    spacing=0,
                ),
                ft.Divider(
                    height=10,
                    color="transparent"
                ),
                
                ft.Container(
                    width=60,
                    height=60,
                ),
            ],
        ),
        border_radius=25,
    )

    page.add(main_container)

ft.app(target=main)
