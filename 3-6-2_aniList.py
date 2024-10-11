import flet as ft
import requests

def fetch_datas():
    response = requests.get("https://ghibliapi.vercel.app/films")
    if response.status_code == 200:
        films = response.json()
        return [{"image": film["image"], 
                 "title": film["title"], 
                 "description": film["description"]} 
                for film in films]
    return []

def main(page: ft.Page):
    page.title = "애니 리스트"
    page.window.width=700
    page.window.height=800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MENU),
        title=ft.Text("Animation List"),
        center_title=True,
        bgcolor=ft.colors.BLUE_GREY_800,
        actions=[ft.IconButton(icon=ft.icons.SEARCH)]
    )
    
    #ListView
    aniList = ft.ListView(spacing=10, padding=20, auto_scroll=True, expand=1)

    ani_datas = fetch_datas()
    for aniData in ani_datas:
        leftImage = ft.Image(src=aniData['image'], width=300)
        rightDescription = ft.Column([ft.Text(aniData['title'],size=25, color="grey",
                                               weight=ft.FontWeight.BOLD),
                                      ft.Text(aniData['description'],)],
                                    height=450,width=280,
                                    alignment=ft.MainAxisAlignment.START)
        aListTile = ft.Row([leftImage, rightDescription], alignment=ft.VerticalAlignment.START)        
        aniList.controls.append(aListTile)

    animation_Cards = ft.Container(content=aniList, height=600, width=600)
    page.add(animation_Cards)

ft.app(target=main)
