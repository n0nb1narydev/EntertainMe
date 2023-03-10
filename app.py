import discord
from discord import app_commands
from dotenv import load_dotenv
import os
from commands import bored, name_age, weather, date

load_dotenv()

# --------------  IMPORTANT VARIABLES -------------- 
token = os.getenv('TOKEN')
guild_id = os.getenv('GUILD_ID')
weather_key = os.getenv('WEATHER_KEY')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# -------------- COMMAND BUILDERS --------------
@tree.command(name = "bored", description = "Gives you something to do.", guild=discord.Object(id=guild_id))
@app_commands.describe(type='Type of activity')
@app_commands.choices(type=[
        app_commands.Choice(name="Education", value="education"),
        app_commands.Choice(name="Recreational", value="recreational"),
        app_commands.Choice(name="Social", value="social"),
        app_commands.Choice(name="DIY", value="diy"),
        app_commands.Choice(name="Charity", value="charity"),
        app_commands.Choice(name="Cooking", value="cooking"),
        app_commands.Choice(name="Relaxation", value="relaxation"),
        app_commands.Choice(name="Busywork", value="busywork"),
        app_commands.Choice(name="Music", value="music"),
        ])
async def bored_command(interaction, type: app_commands.Choice[str]):
    activity = bored.get_activity(type.value)
    await interaction.response.send_message(content=f'<@{interaction.user.id}>, I think you should {activity} today!')


@tree.command(name="name_age", description="Guesses the age of the person by their name.", guild=discord.Object(id=guild_id))
@app_commands.describe(name='Enter a name.')
async def name_age_command(interaction, name:str):
    age = name_age.get_name_age(name)
    await interaction.response.send_message(content=f"I would say someone with the name {name} is about {age} years old.")


@tree.command(name="weather", description="Gets weather for specified location.", guild=discord.Object(id=guild_id))
@app_commands.describe(zip_code='Enter a Zip Code')
@app_commands.describe(country_code='Enter Country Code (e.g. us)')
@app_commands.describe(units='Choose a unit of measurement')
@app_commands.choices(units=[
    app_commands.Choice(name="Metric", value="metric"),
    app_commands.Choice(name="Imperial", value="imperial")
])
async def weather_command(interaction, zip_code:int, units:app_commands.Choice[str], country_code:str):
    # age = name_age.get_name_age(name)
    embed = weather.get_weather(weather_key, zip_code, units.value, country_code)
    await interaction.response.send_message(embed=embed)


@tree.command(name="date_fact", description="Gets a random fact about the date you entered.", guild=discord.Object(id=guild_id))
@app_commands.describe(month='Choose a month')
@app_commands.choices(month=[
    app_commands.Choice(name="January", value=1),
    app_commands.Choice(name="February", value=2),
    app_commands.Choice(name="March", value=3),
    app_commands.Choice(name="April", value=4),
    app_commands.Choice(name="May", value=5),
    app_commands.Choice(name="June", value=6),
    app_commands.Choice(name="July", value=7),
    app_commands.Choice(name="August", value=8),
    app_commands.Choice(name="September", value=9),
    app_commands.Choice(name="October", value=10),
    app_commands.Choice(name="November", value=11),
    app_commands.Choice(name="December", value=12)
])
@app_commands.describe(day='Enter a day.')
async def date_fact_command(interaction, month:app_commands.Choice[int], day:int):
    fact = date.get_date_fact(month.value, day)
    await interaction.response.send_message(content=f"{fact}",ephemeral=True)



# -------------- ON READY -------------- 
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=guild_id))
    print("Ready!")


# -------------- RUN APP -------------- 
client.run(token)
