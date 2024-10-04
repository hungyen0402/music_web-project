import flet as ft

def main(page: ft.Page):
    page.window.bgcolor = ft.colors.TRANSPARENT
    page.bgcolor = ft.colors.TRANSPARENT
    page.window.title_bar_hidden = True
    page.window.frameless = True
    page.window.left = 400
    page.window.top = 200
    page.add(ft.ElevatedButton("I'm a floating button!"))

ft.app(main)