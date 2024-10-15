import flet as ft 
from playsound import playsound

class ButtonList:
    def __init__(self, sound_path, colorname):
        self.sound_path = sound_path
        self.colorname = colorname 

xylbuttons = [
    ButtonList('./assets/note1.wav', 'red'),
    ButtonList('./assets/note2.wav', 'orange'),
    ButtonList('./assets/note3.wav', 'yellow'),
    ButtonList('./assets/note4.wav', 'lime'),
    ButtonList('./assets/note5.wav', 'green'),
    ButtonList('./assets/note6.wav', 'lightblue'),
    ButtonList('./assets/note7.wav', 'purple'),
]
        

def main(page: ft.Page):
    page.window.width = 400
    
    def sound_play(e):
        button_sound = e.control.data
        playsound(button_sound)
    
    button_list = ft.ListView(expand=1, spacing=20, padding=20)

    page.add(button_list)
    
    for buttonItem in xylbuttons:
        button4list = ft.ElevatedButton(buttonItem.colorname,
                                        height=50,
                                        bgcolor=buttonItem.colorname,
                                        on_click=sound_play,
                                        data = buttonItem.sound_path
                                        )
        button_list.controls.append(button4list)
    
    page.update()
        
    
    

if __name__ =='__main__':
    ft.app(main)
