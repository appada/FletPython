import flet as ft


def main(page: ft.Page):
    page.title ="Greetings"
    page.add(
             ft.Text("Hello, Flet!", size = 50),
             ft.Text("oh, Hi Nice Meet You", color = ft.colors.RED,
                     size = 40),
             ft.Text("Welcome to Flet",color = "blue" ,size = 30 )
        )
  
ft.app(main)
