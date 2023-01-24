import discord
from discord import app_commands
from dotenv import load_dotenv
import os
from commands import bored
from typing import List

load_dotenv()

token = os.getenv('TOKEN')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# @tree.command(name = "commandname", description = "My first application Command", guild=discord.Object(id=1038092563120390214)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
# async def first_command(interaction):
#     await interaction.response.send_message("Hello!")

# -------------- COMMAND BUILDERS --------------
@tree.command(name = "bored", description = "Gives you something to do.", guild=discord.Object(id=1038092563120390214))
@app_commands.choices(choice=[
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
async def bored_command(interaction, choice: app_commands.Choice[str]):
    activity = bored.get_activity(choice.value)
    await interaction.response.send_message(f'<@{interaction.user.id}>, you should {activity}!')

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1038092563120390214))
    print("Ready!")

client.run(token)
