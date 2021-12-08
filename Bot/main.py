import discord
from discord.ext import commands
import music

cogs = [music]
client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)



client.run("ODk2NTE2MTY5OTI0NzY3NzU1.YWIPvw.3mfIyEy25j3KNXENlrbmSQh8m7o")
