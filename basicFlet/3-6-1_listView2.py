import flet as ft


def main(page: ft.Page):
    page.title = "ListView"
    page.window.width=400


    list_view = ft.ListView(expand=1,
                     spacing=10,
                     padding=20,
                     auto_scroll=True,
                     divider_thickness=1
                     )


    for i in range(0, 30):
        colorRandom=ft.colors.random_color(),
        list_tile=ft.ListTile(
                   leading=ft.Container(width=100,bgcolor=colorRandom[0]),
                            title=ft.Text(f"Line { i+1 }", size=20),
                            subtitle=ft.Text(colorRandom[0]),
                            trailing=ft.PopupMenuButton(
                                icon=ft.icons.MORE_VERT,
                                items=[
                                    ft.PopupMenuItem(text="Item 1"),
                                    ft.PopupMenuItem(text="Item 2"),
                                ],
                            ),
        )
        list_view.controls.append(list_tile)


    page.add(list_view)
ft.app(main)
