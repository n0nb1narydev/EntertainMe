import requests
import discord

weather_gifs = {'sunny':'https://media.tenor.com/pr0DwlFUbLUAAAAC/happy-sun.gif',
                'cloudy':'https://media.tenor.com/pr0DwlFUbLUAAAAC/happy-sun.gif',
                'rainy':'https://media.tenor.com/e0-Qotha3QMAAAAM/gray-clouds-rain.gif',
                'thunderstorm':'https://media.tenor.com/yxs6gKztcuUAAAAi/kawaii-anime.gif',
                'snowy':'https://media.tenor.com/7J0E_UbskFQAAAAd/panda-cute-panda.gif',
                'default': 'https://media.tenor.com/eZqKP1ThC2oAAAAC/todays-weather-weather.gif'
                }

def get_weather(api_key, zip_code, units, country_code=''):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key}")
    data = response.json()

    city = data['name']
    weather_description = data['weather'][0]['main'].lower()
    weather_details = data['weather'][0]['description']
    temperature = data['main']['temp']
    if units == 'imperial':
        temperature = round(1.8*(temperature-273) + 32)
    elif units == 'metric':
        temperature = round(temperature - 273.15)
    high_temperature = data['main']['temp_max']
    low_temperature = data['main']['temp_min']

    # # Get appropriate embed gif
    if('rain' in weather_description):
        embed_image = weather_gifs['rainy']
    elif('sun'in weather_description):
        embed_image = weather_gifs['sunny']
    elif('cloud' in weather_description):
        embed_image = weather_gifs['cloudy']
    elif('storm' in weather_description):
            embed_image = weather_gifs['thunderstorm']
    elif('snow'in weather_description):
            embed_image = weather_gifs['snowy']
    else:
        embed_image = weather_gifs['default']

    embed=discord.Embed(
        title=f"Weather in {city}", 
        description=f"The current weather in {city} right now is **{weather_details}**.", 
        color=0xFFFFFF)
    embed.add_field(name="Current Temperature", value=f"{temperature}", inline=False)
    embed.set_image(url=embed_image)
    # weather = data['age']
    return embed