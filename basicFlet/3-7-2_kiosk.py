import flet as ft
import data_list

#order 저장용 클래스
class Orders:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def main(page: ft.Page):
    page.window.width=768
    page.window.height=1366
    page.padding = 50
    page.horizontal_alignment=ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MENU),
        title=ft.Text("Simple Kiosk"),
        center_title=True,
        bgcolor=ft.colors.TEAL_700,
    )
    
    kiosk_menu = ft.GridView(
        expand=1,
        runs_count=3,
        max_extent=250,
        width=700,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )
    
    # Functions
    order_list = []
    def order_reset(e):
        order_list.clear()
        order_menu.controls=[ft.Text('음료를 선택해 주세요')]
        total_count.value = 0
        total_txt.value = 0    
        page.update()
        
    def order_add(e):
        total_count.value = int(total_count.value) + 1
        addorder = Orders(e.control.data[0], e.control.data[1])
        order_list.append([addorder.name, addorder.price])
        order_menu.controls.append(ft.Row([ft.Text(addorder.name),
                                           ft.Text(addorder.price)]))
        total_sum = 0
        for item in order_list:
            total_sum += int(item[1])
        total_txt.value=total_sum    
        page.update()
    
    # Ui
    total_txt = ft.Text('0')
    total_count = ft.Text('0')
    order_menu=ft.Column([ft.Text(
        '안녕하세요.\n저희 가계를 찾아주셔서 감사합니다.\n주문서 작성후 제출해주세요')])
    order_right_total=ft.Row([ft.Text('합  계 :'),total_txt])
    order_right_count=ft.Row([ft.Text('주문수 :'),total_count])
    order_right= ft.Column([order_right_total, order_right_count,
                            ft.ElevatedButton('초기화', on_click=order_reset),
                            ]) #ft.ElevatedButton('주문하기')
    order_row=ft.Row([order_menu, order_right], width=700, 
                     alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    # Page
    page.add(ft.Divider(),order_row,ft.Divider(), kiosk_menu)
    

    # Fetch Data
    for product in data_list.productList:
        item_image=ft.Image(src=product.image_path, width=140, height=140, 
                            fit="fill", border_radius=20)
        item_name=ft.Text(product.name, bgcolor="black",  
                          weight=ft.FontWeight.BOLD, size=15)
        item_button=ft.FilledTonalButton(product.price, 
                                         data=[product.name,product.price] , 
                                         on_click=order_add)
    
        item_box = ft.Container(content=ft.Column([item_image,
                                                   item_name,
                                                   item_button],
                                                  horizontal_alignment="center",
                                                  ),
                                height=500, 
                                )
        kiosk_menu.controls.append(item_box)
    #    
    page.update()
    
ft.app(main)
