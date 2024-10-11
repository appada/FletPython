import flet as ft


def main(page:ft.Page):
    page.add( ft.Icon('favorite'),
              ft.Icon(ft.icons.FAVORITE, color="red"),
              ft.IconButton(ft.icons.SEARCH, icon_color=ft.colors.BLUE),
              ft.IconButton("search", icon_color="red"),
              )

ft.app(main)
