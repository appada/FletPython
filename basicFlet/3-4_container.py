import flet as ft 

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    button1 = ft.ElevatedButton('Button')
    buttons_row = ft.Container(content=ft.Row([button1, button1]),
                               bgcolor="amber")
    container1 = ft.Container(content=buttons_row, 
                              width=250, 
                              height=250, 
                              bgcolor="green",
                              padding=25,
                              margin=25,
                              )
    page.add(container1)
    
ft.app(target=main)
