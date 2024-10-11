import flet as ft


def main(page: ft.Page):
    page.title = "ListView"
    page.window.width=400


    list_view = ft.ListView(expand=1,   #화면 채우기 기본속성
                     spacing=10,  # 공간 여백
                     padding=20,  # 패딩
                     auto_scroll=True, # 자동 스크롤
                     divider_thickness=1, # 화면을 나누는 줄
                     horizontal=False #수평 수직, 기본은 False
                     )


     # 컨테이너로 만든 listBox 30개를 생성합니다.
    for i in range(0, 30):
        listBox=ft.Container(content=ft.Text(f"Line { i+1 }", size=20),
                             bgcolor=ft.colors.random_color(),
                             height=30
                             )
        list_view.controls.append(listBox) # 컨테이너로 만든 listBox 추가


    page.add(list_view)


ft.app(main)
