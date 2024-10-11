import flet as ft
from random import randint


def main(page: ft.Page):
    page.title =  "숫자게임"
    page.horizontal_alignment="center"  #가로 페이지 정렬=중앙
    page.vertical_alignment="center"  #세로 페이지 정렬=중앙
    #  작은수와 큰수 범위를 정해 랜덤으로 숫자를 저장합니다.
    lowerNum, upperNum = 1, 10
    randomNumber = randint(lowerNum,upperNum)


    def checkButton(e):


        guessValue = int(guessNumber.value)
        if guessValue < randomNumber:
            resultText.value = "더 큰 숫자입니다."
            resultText.bgcolor = "red"
        elif guessValue > randomNumber:
            resultText.value = "더 작은 숫자입니다."
            resultText.bgcolor = "blue"
        else:
            resultText.value = "정답입니다!"


        page.update()


    guessNumber = ft.TextField(label="숫자를 맞혀봐",
        width=150, border_color="green",border_width=3)
    checkNumber = ft.OutlinedButton('Check!',
                                    on_click=checkButton)
    resultText = ft.Text()


    page.add(guessNumber,
             checkNumber,
             resultText
             )
ft.app(target=main)
