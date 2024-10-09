import flet as ft
from icons.iconlist import icons_list

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = True
    item_container = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )
    page.add(item_container)
    
    # 버튼 생성
    
    for icon_name in icons_list:
        item_container.controls.append(
            ft.Column([
                ft.IconButton(icon=icon_name, icon_size=40),
                ft.Text(icon_name),
                ])
            )
    page.update()
    
ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8080)
