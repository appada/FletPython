import flet as ft
from colors.colorlist import colors_list

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = True
    color_container = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=100,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )
    page.add(color_container)
    
    for color in colors_list:
        color_box = ft.Column([ft.Container( bgcolor=color, width=200, height=30),  ft.Text(color, size=12)  ])
        color_container.controls.append(color_box)
    page.update()
    
ft.app(target=main)
