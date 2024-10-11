import flet as ft


def main(page: ft.Page):
    page.title = "Column"
    page.window.width  = 300
    page.window.height = 500


    apple = ft.Text(value="Apple",size=15)
    melon = ft.Text(value="Melon",size=15)
    orange = ft.Text(value="Orange",size=12)


    container1 = ft.Container(content=apple, height=50,
                              width=50, bgcolor="red")
    container2 = ft.Container(content=melon, height=50,
                              width=50, bgcolor="green")
    container3 = ft.Container(content=orange, height=50,
                              width=50, bgcolor="orange",
                  border_radius=ft.border_radius.all(20),
                 alignment=ft.alignment.center)


    page.add(ft.Column([container1,
                        container2, 
                        container3],
                        height=200, width=300,
          alignment=ft.MainAxisAlignment.CENTER,
          horizontal_alignment=ft.CrossAxisAlignment.CENTER
                       ),
             ft.Divider(),
             ft.Row([container1, container2, container3],
                    height=200,
                    width=300,
                    alignment=ft.MainAxisAlignment.CENTER,
           vertical_alignment=ft.CrossAxisAlignment.CENTER
                    )
             )
    page.update()


ft.app(main)
