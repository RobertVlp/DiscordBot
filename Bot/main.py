#    This file is part of DiscrodBot.

#    DiscordBot is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    DiscordBot is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with DiscordBot. If not, see <https://www.gnu.org/licenses/>.

import discord
from discord.ext import commands
import music

cogs = [music]
client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)



client.run("ODk2NTE2MTY5OTI0NzY3NzU1.YWIPvw.3mfIyEy25j3KNXENlrbmSQh8m7o")
