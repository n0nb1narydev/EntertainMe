import discord
from discord import app_commands
from dotenv import load_dotenv
import os
from commands import bored, name_age
# from typing import List

load_dotenv()

token = os.getenv('TOKEN')
guild_id = os.getenv('GUILD_ID')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# @tree.command(name = "commandname", description = "My first application Command", guild=discord.Object(id=1038092563120390214)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
# async def first_command(interaction):
#     await interaction.response.send_message("Hello!")

# -------------- COMMAND BUILDERS --------------
@tree.command(name = "bored", description = "Gives you something to do.", guild=discord.Object(id=guild_id))
@app_commands.describe(type='Type of activity.')
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

@tree.command(name = "name_age", description = "Guesses the age of the person by their name.", guild=discord.Object(id=guild_id))
@app_commands.describe(name='Enter a name.')
async def name_age_command(interaction, name: str):
    age = name_age.get_name_age(name)
    await interaction.response.send_message(content=f"I would say someone with the name {name} is about {age} years old.")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=guild_id))
    print("Ready!")

client.run(token)
