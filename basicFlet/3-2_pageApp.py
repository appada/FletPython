import flet as ft 
def main(page: ft.Page):
    page.title="PageLayout"
    # Top Appbar
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MENU),
        title=ft.Text("Top AppBar"),
        center_title=True,
        bgcolor=ft.colors.TEAL_700,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
        ]
    )
    # Bottom Appbar
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE_GREY_800,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.HOME,),
                ft.Text('Bottom AppBar'),
                ft.IconButton(icon=ft.icons.EMAIL),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )
    # FloatingActionButton
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD)
    
    #Tab pages
    tab_pages = ft.Tabs(
        tab_alignment=ft.TabAlignment.CENTER,
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="        Tab 1        ",
                content=ft.Container(
                    content=ft.Image(src="https://cdn.pixabay.com/photo/2023/12/23/08/42/island-8465139_1280.png"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="        Tab 2        ",
                content=ft.Container(
                    content=ft.Image(src="https://cdn.pixabay.com/photo/2024/06/12/16/25/plant-8825881_1280.png"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="       Tab 3        ",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
        ],
        expand=1,
    )
    
    # Body
    page.add(tab_pages)
    
    
    
    page.update()
    
ft.app(main)
