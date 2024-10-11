import flet as ft


def main(page: ft.Page):
    page.title = "Counter"


    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()


    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()


    txt_number = ft.Text("0", size=50)


    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE,
                              on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, 
                              on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER, 
                      # 열의 중앙에 정렬
        )
    )


ft.app(main)
