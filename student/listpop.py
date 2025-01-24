import flet as ft 


# 가로 행 row , 세로 열 column
def main(page: ft.Page):
    
    total_list =[]
    
    def add_number(e):
        total_list.append(input_text.value)
        to_listbox()
        
    def pop_number(e):
        total_list.pop()
        to_listbox() 
        
    def to_listbox():
        listbox_total.value=''
        for item in total_list:
            listbox_total.value += str(item)+"\n"
        page.update()
        
        
    
    input_text = ft.TextField(label='Enter Number', on_submit=add_number)
    add_button = ft.IconButton(ft.Icons.ADD, icon_size=40, on_click=add_number)
    pop_button = ft.IconButton(ft.Icons.REMOVE, icon_size=40, on_click=pop_number)
    
    listbox_total = ft.TextField(expand=True,multiline=True,min_lines=13,max_lines=13)
    
    line_1 = ft.Row([ input_text, add_button, pop_button ])
    
    page.add( line_1, listbox_total)
    
ft.app(main)
