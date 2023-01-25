import requests
import discord

weather_gifs = {'sunny':'https://media.tenor.com/pr0DwlFUbLUAAAAC/happy-sun.gif',
                'cloudy':'https://i.pinimg.com/originals/d5/38/f7/d538f7976546294953deda9d409725bf.gif',
                'rainy':'https://media.tenor.com/e0-Qotha3QMAAAAM/gray-clouds-rain.gif',
                'thunderstorm':'https://media.tenor.com/yxs6gKztcuUAAAAi/kawaii-anime.gif',
                'snowy':'https://media.tenor.com/7J0E_UbskFQAAAAd/panda-cute-panda.gif',
                'default': 'https://media.tenor.com/eZqKP1ThC2oAAAAC/todays-weather-weather.gif'
                }

# ------------- CONVERSION FUNCTIONS -------------
def celcius(kelvin):
    temp = f'{round(kelvin - 273.15)}°C'
    return temp


def fahrenheit(kelvin):
    temp = f'{round(1.8*(kelvin-273) + 32)}°F'
    return temp


def kmph(knots):
    speed = f'{round(knots * 1.852)} km/h'
    return speed


def mph(knots):
    speed = f'{round(knots * 1.15078)} mph'
    return speed


# ------------- MAIN FUNCTION -------------
def get_weather(api_key, zip_code, units, country_code=''):
    # Data Retrieval
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key}")
    data = response.json()

    print(data)

    city = data['name']
    weather_description = data['weather'][0]['main'].lower()
    weather_details = data['weather'][0]['description']
    temperature = data['main']['temp']
    high_temperature = data['main']['temp_max']
    low_temperature = data['main']['temp_min']
    feel_temp = data['main']['feels_like']
    speed = data['wind']['speed']
    humidity  = data['main']['humidity']

    # Conversions
    if units == 'imperial':
        temperature = fahrenheit(temperature)
        high_temperature = fahrenheit(high_temperature)
        low_temperature = fahrenheit(low_temperature)
        feel_temp = fahrenheit(feel_temp)
        speed = mph(speed)
    elif units == 'metric':
        temperature = celcius(temperature)
        high_temperature = celcius(high_temperature)
        low_temperature = celcius(low_temperature)
        feel_temp = celcius(feel_temp)
        speed = kmph(speed)

    # # Get appropriate embed gif
    if('rain' in weather_description):
        embed_image = weather_gifs['rainy']
    elif('clear'in weather_description):
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
    embed.add_field(name="Current Temperature", value=f"{temperature}", inline=True)
    embed.add_field(name="Feels Like", value=f"{feel_temp}", inline=True)
    embed.add_field(name="Today's Forecast", value=f"{low_temperature}/{high_temperature}", inline=True)
    embed.add_field(name="Wind", value=f"{speed}", inline=True)
    embed.add_field(name="Humidity", value=f"{humidity}%", inline=True)
    embed.set_image(url=embed_image)

    return embed