import flet as ft
def main(page: ft.Page):
    page.title = "Fruits"
    apple = ft.Text(value="Apple", color="red")
    banana = ft.Text(value="Banana", color="yellow")
    kiwi = ft.Text(value="Kiwi", color="green")
    orange = ft.Text(value="Orange", color="orange")


    page.add(apple, banana, kiwi, orange)
    page.update()


ft.app(main)
