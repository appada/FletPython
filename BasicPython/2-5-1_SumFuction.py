import flet as ft


def main(page: ft.Page):
    def sum_values(e):
        a = int(txt_a.value)     # txt_a 텍스트 필드의 값 정수로 반환
        b = int(txt_b.value)    # txt_b 텍스트 필드의 값 정수로 반환
        sum_result.value = a + b  
        page.update()
    #
    txt_a = ft.TextField(label=" A ")
    txt_b = ft.TextField(label=" B ")
    sum_button = ft.ElevatedButton(text="계산하기", on_click=sum_values)
    sum_result = ft.Text('결과', size=20)    
    #
    page.add(txt_a,txt_b,sum_button,sum_result)


ft.app(main)
