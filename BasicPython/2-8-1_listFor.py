import flet as ft
import time


def main(page: ft.Page):
    fruits = ["Apple", "Banana", "Kiwi", "Orange", "berry"]


    for fruit in fruits:
        page.add(ft.ElevatedButton(fruit,
                                   bgcolor=ft.colors.random_color()))
        time.sleep(1)


ft.app(target=main)
