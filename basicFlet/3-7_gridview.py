import flet as ft


def main(page: ft.Page):
    page.title = "GridView"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width=800
    page.padding = 50


    images_grid = ft.GridView(
        expand=1,       # 크기를 칸에 맞추어 늘려줍니다
        runs_count=5,    # 한줄에 몇칸씩 보여줄지 결정합니다
        max_extent=150,  #그리드뷰 칸의 가로세로 최대크기를 정합니다
        spacing=5,        #주축(mainaxis) 간격 행간의 공백
        run_spacing=5,    #교차축(crossaxis) 간격 열간의 공백
    )


    # 먼저, GridVidw를 만들어 페이지에 추가합니다.
    page.add(images_grid)


     # 60개의 이미지를 GriveView에 붙여줍니다.
    for i in range(0, 60):
        images_grid.controls.append(
            ft.Image(
                src=f"https://picsum.photos/150/150?{i}",
                fit=ft.ImageFit.NONE,
                border_radius=ft.border_radius.all(10),
            )
        )
    page.update()


ft.app(main)
