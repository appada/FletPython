import flet as ft
from flet import Page,GridView,TextField,Container,Text,Alignment

def main(page: Page):
    page.title = "간단한 계산기"
    page.window.width = 250
    page.window.height = 350
    page.vertical_alignment = "center"
    page.padding=10
    
    #계산함수
    def button_clicked(e):
        data = e.control.data
        if data == "C":
            result_input.value = "0"
        elif data == "=":
            try:
                result_input.value = str(eval(result_input.value))
            except:
                result_input.value = "바르게입력하세요"
        else:
            if result_input.value == "0":
                result_input.value = data
            else:
                result_input.value += data
        result_input.update()
    #
    button_list = ["7", "8", "9", "/",
                   "4", "5", "6", "*",
                   "1", "2", "3", "-",
                   "C", "0", "=", "+"]
    #Grid View
    cal_buttons = GridView(
        expand=1, 
        runs_count=4,  # 시작수
        max_extent=50,  # 그리드뷰 칸의 가로세로 최대크기
        spacing=3, #주축 간격 mainaxis (행간)
        run_spacing=3, #교차축 간격 crossaxis
    )
    # Ui
    result_input = TextField(value="0", text_align="right", width=230,
                          border=3, border_radius=20, border_color="grey")
    button_container = Container(content=cal_buttons, height=210, width=210, 
                                    bgcolor="bluegrey",
                                    padding=10,
                                    border_radius=20
                                    )
    #
    page.add(result_input, 
             button_container)
    
    # Fetch Data
    for index, buttonItem in enumerate(button_list):
        button_bgcolor = "black"
        if index in [3, 7, 11, 12, 14, 15]:
            button_bgcolor = "orange"
        
        item_box = Container(content=Text(buttonItem, size=30), 
                                bgcolor=button_bgcolor,
                                alignment=Alignment(0, 0),
                                border_radius=20,
                                data=buttonItem,
                                on_click=button_clicked)
        cal_buttons.controls.append(item_box)
    #    
    page.update()
    
ft.app(target=main)
