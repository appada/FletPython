import flet as ft 
import sqlite3
from datetime import datetime

def start_db():
        with sqlite3.connect("fletmemo.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS fletmemo (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    memo TEXT,
                    mcolor TEXT,
                    created TEXT
                )
            ''')

def fetch_all():
    with sqlite3.connect("fletmemo.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM fletmemo ORDER BY ID DESC")
        return cursor.fetchall()

colorText = ft.colors.random_color()
    
def main(page: ft.Page):
#    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width=360
    page.window.height=700
    page.title="Flet Memo"
    page.scroll = "always"
    
    start_db()
    
    def theme_change(e):
        page = e.page
        #page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        if page.theme_mode == "dark":
            page.theme_mode = "light"
            page.update()
        else:
            page.theme_mode = "dark"
            page.update()
    
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MENU),
        title=ft.Text("Flet Memo"),
        bgcolor=ft.colors.BLUE_GREY_800,
        actions=[ft.IconButton(icon=ft.icons.WB_SUNNY,on_click=theme_change)]
    )
    
        

            
    memo_grid = ft.GridView(
        expand=1,
        runs_count=3,
        max_extent=200,
        width=700,
        spacing=10,
        run_spacing=10,
        auto_scroll=True
    )
   # 그리드뷰와 리스트뷰를 바꾸어서 비교해 보세요.
   # memo_grid3 = ft.ListView(expand=1, spacing=20, padding=20)
    
    def load_data():
        memo_grid.controls.clear()
        for row in fetch_all():
            memo_grid.controls.append(
              ft.Container(content=
                           ft.Column(
                               [ft.Text(str(cell), color="black") for cell in row]
                               ),
                           bgcolor=row[2] ,border_radius=20, padding=20, 
                           on_click=delete_memo, data=row[0])  
            )
        page.update()
    
    def delete_memo(e):
        memo_id = e.control.data
        with sqlite3.connect("fletmemo.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM fletmemo WHERE ID = ?", (memo_id))
            conn.commit()
        load_data()
        show_snackbar(f"메모를 삭제했습니다.", "blue")    

    def addMemo(e):
        memo = memo_text.value
        memocolor = memo_button.data
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with sqlite3.connect("fletmemo.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO fletmemo (memo, mcolor, created) VALUES (?, ?, ?)",
                           (memo, memocolor, created_at))
        load_data()
        memo_text.value=''
        show_snackbar(f"메모를 저장했습니다.", "green")
    
    def show_snackbar(message, color):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(message, color="white"),
            bgcolor=color,
        )
        page.snack_bar.open = True
        page.update()
        
        
    def color_change(e):
        global colorText
        colorText = ft.colors.random_color()
        memo_text.bgcolor=colorText
        memo_button.data= colorText
        memo_color_sample.bgcolor = colorText
        page.update()
    
    memo_text = ft.TextField(label="memo",multiline=True,width=700)
    memo_button = ft.ElevatedButton("메모입력", data=colorText, on_click=addMemo)
    memo_color = ft.ElevatedButton("배경선택", on_click=color_change)
    memo_color_sample = ft.Container(width=50, height=50, bgcolor=colorText)
    select_color = ft.Row([ memo_button, memo_color, memo_color_sample ],
                          width=700, alignment=ft.MainAxisAlignment.END)
    
    page.add(memo_text,
             select_color,
             memo_grid)
    
    load_data()

ft.app(main)
