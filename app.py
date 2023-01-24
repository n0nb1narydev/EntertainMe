import discord
from discord import app_commands
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('TOKEN')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "commandname", description = "My first application Command", guild=discord.Object(id=1038092563120390214)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1038092563120390214))
    print("Ready!")

client.run(token)