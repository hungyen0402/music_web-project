from flet import *
import flet as ft
import time
import threading
from ytmusicapi import YTMusic
from pytube import YouTube
import os

def main(page : Page):
    bgcolor = LinearGradient(
        begin=ft.alignment.bottom_left,
        end= ft.alignment.top_right,
        colors=['#f46464', '#3d2f5e']
    )
    primary = "#41005E"
    secondary = "#F1DEFA"
    tertiary = "#B19FF9"

    page.title = 'Music Player'
    page.window.width = 320
    page.window.height = 650
    page.horizontal_alignment = 'center'
    page.theme_mode = 'dark'

    def change_music_screen(e):
        
            main_container.visible = True
            home_screen.visible = False
            page.update()
    
    def change_home_screen(e):
        
            main_container.visible = False
            home_screen.visible = True
            page.update()
   
        

    # Music Screen
    playlist = [
        "audio/Nơi Này Có Anh.mp4",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
    ]
    current_song_index = 0

    audio1 = ft.Audio(
        src='https://music.youtube.com/watch?v=qHpE45b4INk', 
        volume=1, 
        autoplay=True,
        # on_loaded=lambda _: update_total_time(),
        # on_position_changed=lambda _: update_current_time()
    )

    def play(e):
        audio1.resume()
        play_button.visible = False
        pause_button.visible = True
        play_button.update()
        pause_button.update()
        threading.Thread(target=update_slider).start()
        home_screen.content.controls[3].visible = True
        home_screen.content.controls[2].height = 370
        page.update()

    def pause(e):
        audio1.pause()
        play_button.visible = True
        pause_button.visible = False
        play_button.update()
        pause_button.update()

    def next_song(e):
        nonlocal current_song_index
        current_song_index = (current_song_index + 1) % len(playlist)
        audio1.src = playlist[current_song_index]
        play_button.visible = False
        pause_button.visible = True
        audio1.autoplay = True
        audio1.update()
        play_button.update()
        pause_button.update()
        update_total_time()

    def prev_song(e):
        nonlocal current_song_index
        current_song_index = (current_song_index - 1) % len(playlist)
        audio1.src = playlist[current_song_index]
        play_button.visible = False
        pause_button.visible = True
        audio1.autoplay = True
        audio1.update()
        play_button.update()
        pause_button.update()
        update_total_time()

    def update_total_time():
        total_time = audio1.get_duration() / 1000
        total_time_text.value = f"{int(total_time) // 60}:{int(total_time % 60):02d}"
        total_time_text.update()
        slider.max = total_time
        slider.update()

    def update_current_time():
        current_time = audio1.get_current_position() / 1000
        current_time_text.value = f"{int(current_time) // 60}:{int(current_time % 60):02d}"
        current_time_text.update()
        slider.value = current_time
        slider.update()
        if current_time >= audio1.get_duration() / 1000 - 1:
            audio1.pause()
            next_song(None)

    def update_slider():
        while audio1.get_current_position() < audio1.get_duration():
            current_time = audio1.get_current_position() / 1000
            slider.value = current_time
            slider.update()
            time.sleep(0.1)

    def back(e):
        audio1.pause()


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
        width=320,
        height=600,
        gradient=bgcolor,
        visible=False,
        content=ft.Column(
            [
                audio1,
                ft.Row(
                    controls=[
                        IconButton(icon=ft.icons.ARROW_BACK, icon_color=ft.colors.WHITE,
                                   icon_size=30, on_click=change_home_screen)
                    ],
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


    # Home_Screen

    def click_search(e):
        home_screen.content.controls[1].focus()
        page.update()
    
    # Return music, download music and play
    def playmusic(e):
        videoId = e.control.subtitle.value
        videoUrl = 'https://music.youtube.com/watch?v=' + str(videoId)
    
        yt = YouTube(videoUrl)
		#  DOWNLOAD THE VIDEO 
        video_stream = yt.streams.filter(only_audio=True).first()
        result = video_stream.download(output_path='assets/audio/')
        if not result == '':
            print('DOWNLOAD FINISHED')
           
            print(result)
            audio1.src = result
           

            audio1.play()
            audio1.autoplay = True
            page.update()
        page.update()

    # Search
    def search_song(e):
        result = YTMusic().search(query=e.data, filter='songs')
        home_screen.content.controls[2].controls.clear()
        if not result == '':
            for x in result:
                home_screen.content.controls[2].controls.append(
				ListTile(
                    leading=Image(
                        src=x['thumbnails'][1]['url'],
                        fit="cover",
                        width=70,
                        height=70,
                        border_radius=10
                    ),
                    title=Column([
                        Text(x['title'],weight="bold"),
                        Text(x['artists'][0]['name'], weight='bold')
                        ]),
                    subtitle=Text(x['videoId'],size=10),
    
                    # AND IF CLICK THIS LISTTILE THEN RUN FUNCTION
                    on_click=lambda e:playmusic(e)
				)
			)
            
            page.update()
                
    home_screen = Container(
        width=320,
        height=600,
        border_radius=25,
        gradient=bgcolor,
        visible=True,
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
                    on_submit=lambda e : search_song(e)
                ),
               
            
                # No Content - Result search name music
                ft.Column(
                    width=320,
                    height=420,
                    scroll=ScrollMode.AUTO,
                    controls=[]
                ),
                
                # Mini Music Screen
                ft.Container(
                    width=320,
                    height=50,
                    visible=False,
                    gradient=bgcolor,
                    border_radius=25,
                    content=Row(
                        controls=[
                            Container(
                               width=5  
                            ) ,

                            ft.Image(src='Images/image1.jpg',
                                    width=50,
                                    height=50,
                                    border_radius=25,
                                    
                            ),
                            
                        ]
                    )
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

                        ft.IconButton(icon=ft.icons.PERSON, icon_color=ft.colors.WHITE
                                      , on_click=change_music_screen),
                    ]
                )
            ]
        )
    )


    
    page.overlay.append(audio1)
    page.add(home_screen,
             main_container
             )
    


ft.app(target=main, assets_dir='assets', web_renderer=WebRenderer.HTML)