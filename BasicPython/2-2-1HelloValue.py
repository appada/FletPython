import flet as ft


def main(page: ft.Page):
    page.title ="Greetings" # 페이지 제목
    greeting1 = ft.Text("Hello, Flet!", size=50)
    greeting2 = ft.Text("oh, Hi Nice Meet You", color=ft.colors.RED,
                        size=40)
    greeting3 =  ft.Text("Welcome to Flet", bgcolor="yellow",
                 color ="blue", size=30 )

  page.add( greeting1, greeting2, greeting3 )

ft.app(main)
