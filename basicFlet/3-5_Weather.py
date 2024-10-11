import flet as ft
import python_weather

          
# Functions
def get_weather_icon(condition):
    if condition == "Thunderstorm":
        return '🌩'
    elif condition == "Light rain":
        return '🌧'
    elif condition == "Rainy":
        return '☔️'
    elif condition == "Snowy":
        return '☃️'
    elif condition == "Windy":
        return '🌫'
    elif condition == "Sunny":
        return '☀️'
    elif condition == "Cloudy":
        return '☁️'
    elif condition == "Partly cloudy":
        return '☁️'
    elif condition == "Clear":
        return '😌'
    else:
        return '🤷‍'
    
def to_celsius(fa):
    changeNumber =  (int(fa) - 32) * 5.0/9.0
    return round( changeNumber,1)


# --- MAIN --- 
def main(page: ft.Page):
    async def get_weather(e):
        async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
           weather = await client.get(inputBox.value)
           temperText.value = str(to_celsius(weather.temperature))+'°'
           humidityPercent.value = '💧'+str(weather.humidity)+'%'
           cityName.value = inputBox.value
           iconImage.value = get_weather_icon(weather.description)
           weather_text.value = weather.description
           page.update()   
        #return weather
    
    page.title="PageLayout"
    page.window.width=300
    page.window.height=350
    page.horizontal_alignment = page.vertical_alignment = "center"
    

    # Ui
    cityName = ft.Text('testcity',size=30,weight=ft.FontWeight.BOLD)
    humidityPercent = ft.Text('💧22%',color="blueaccent",size=20,weight=ft.FontWeight.BOLD)
    weather_city = ft.Container(content=ft.Row([cityName, humidityPercent],
                                       alignment=ft.MainAxisAlignment.SPACE_BETWEEN),margin=10)
    
    iconImage=ft.Text('☀️', size=70)
    temperText=ft.Text('20°', size=60,color="black", weight=ft.FontWeight.BOLD)
    weather_imogi = ft.Row([iconImage, temperText], alignment=ft.MainAxisAlignment.CENTER)
    
    weather_text = ft.Text('Sunny', weight=ft.FontWeight.BOLD, size=35, color="white")
    
    inputBox= ft.TextField(value='seoul', label="city name", border_width=5, bgcolor="black")
    weather_search = ft.Row([ft.IconButton(icon=ft.icons.REPLAY,icon_size=30, on_click=get_weather),
                             ft.Container(content=inputBox, width=150),
                             ft.IconButton(icon=ft.icons.SEARCH,icon_size=30, on_click=get_weather)],
                             alignment=ft.MainAxisAlignment.CENTER)
    # Group
    weatherInfo = ft.Column([weather_city,
                             weather_imogi,
                             weather_text,
                             weather_search],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    # Body
    body = ft.Container(width=300,
                        image=ft.DecorationImage("https://picsum.photos/300/300?1", fit="fill"),
                        border_radius=ft.border_radius.all(30),
                        expand=1,
                        content=weatherInfo)
    #
    page.add(body)
    
   
    
ft.app(main)
