import flet as ft

def main(page: ft.Page):
    page.title = 'Page layout.'
    page.appbar = ft.AppBar(title=ft.Text('Top AppBar Text'),
                            center_title = True,
                            bgcolor= ft.colors.TEAL_800,
                            actions= [ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
                                      ft.IconButton(ft.icons.FILTER_3)
                                      ]
                            )
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE_GREY_800,
        content = ft.Row([
            ft.IconButton(icon= ft.icons.HOME),
            ft.Text('Bottom AppBar'),
            ft.IconButton(icon=ft.icons.EMAIL)
        ], alignment= ft.MainAxisAlignment.SPACE_BETWEEN)
    )
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD)
    
    #body
    bodyImage = ft.Image("https://picsum.photos/300/400?31")
    
    page.add(bodyImage)
    page.update()
        
ft.app(target=main)


