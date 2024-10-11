import flet as ft 

def main(page: ft.Page):
    # 6
    def compare_values(e):
        a = int(txt_a.value)
        b = int(txt_b.value)
        result = f"a == b: {a == b}\n"
        result += f"a != b: {a != b}\n"
        result += f"a > b: {a > b}\n"
        result += f"a < b: {a < b}\n"
        result += f"a >= b: {a >= b}\n"
        result += f"a <= b: {a <= b}\n"
        relation_result.value = result
        page.update()
    # 123
    txt_a = ft.TextField(label=" A ")
    txt_b = ft.TextField(label=" B ")
    button_compare = ft.ElevatedButton(text="비교하기",
                     on_click=compare_values)
    relation_result = ft.Text(size=20)    
    # 4
    page.add(txt_a,txt_b,button_compare,relation_result)


ft.app(main) # 5 7
