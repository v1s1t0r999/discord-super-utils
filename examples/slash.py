"""
The SlahsManager is deprecated.
It is no longer supported.
Install v0.2.4 (ig) - pip install discordSuperUtils-0.2.4
"""


import discord
from discord.ext import commands

import discordSuperUtils

bot = commands.Bot(command_prefix="-", intents=discord.Intents.all())
slash = discordSuperUtils.SlashManager(bot)


@bot.event
async def on_ready():
    print("Slash manager is ready.", bot.user)


@slash.command()
async def ping(ctx):
    await ctx.reply(f"Pong! ping is {bot.latency * 1000}ms")


bot.run("token")
