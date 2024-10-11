import flet as ft
def main(page: ft.Page):
    page.title = "Button Click Example"
    def button_clicked(e):
        button.data += 1
        txt.value = f"Button clicked {button.data} time(s)"
        page.update()


    txt = ft.Text()
    button = ft.OutlinedButton(text="Button'click' (e)vent", 
                                on_click=button_clicked, data=0)
    page.add(txt, button) #페이지에 추가한 순서대로 출력이 된다.
  
ft.app(main)
