import discord
import time
import aiohttp
import psutil
import platform
import re

from collections import Counter
from settings import links
from discord.ext import commands

class Utility(commands.Cog, name="Utility"):
    def __init__(self, bot):
        self.bot = bot

# <:TPK_wolfwhat:848290879076696135>p[

    @commands.command()
    async def ping(self, ctx):
        """ See BadWolf's latency to discord """
        discord_start = time.monotonic()
        async with aiohttp.ClientSession() as session:
            async with session.get('https://discord.com') as r:
                if r.status == 200:
                    discord_end = time.monotonic()
                    discord_ms = f"**{round((discord_end - discord_start) * 1000)}** ms"
                else:
                    discord_ms = "fucking dead"
                await ctx.send(f"{discord_ms} ping <:TPK_wolfwhat:848290879076696135>")

    @commands.command(alias=["botinfo"])
    async def about(self, ctx):
        """ Information about BadWolf """
        chtypes = Counter(type(c) for c in self.bot.get_all_channels())
        voice = chtypes[discord.channel.VoiceChannel]
        text = chtypes[discord.channel.TextChannel]
        cpup = psutil.cpu_percent()
        core = psutil.cpu_count()
        mem = psutil.virtual_memory().total >> 20
        mem_usage = psutil.virtual_memory().used >> 20
        storage_free = psutil.disk_usage('/').free >> 30
        storage = psutil.disk_usage('/').total >> 30
        boottime = psutil.boot_time()
        joshua = await self.bot.fetch_user(links.joshua)
        Toothy = await self.bot.fetch_user(links.Toothy)
        users = sum(x.member_count for x in self.bot.guilds)

        e = discord.Embed(color=discord.Color.dark_teal())
        e.set_thumbnail(url=self.bot.user.avatar.url)
        e.title = f"{self.bot.user.name} information"
        e.description = f"""
__**General information**__
Developers:
- **[{joshua}](https://discord.com/users/{links.joshua})**
- **[{Toothy}](https://discord.com/users/{links.Toothy})**

Library: [Enhanced-discord.py {discord.__version__}](https://github.com/iDevision/enhanced-discord.py)
Code: [Find it by clicking here](https://github.com/ThePawKingdom/TPKBot)

__**System**__
System Software: `{platform.system()} {platform.release()}`
CPU Usage: `{cpup}`%
RAM: `{mem_usage}`/`{mem}` MB
Storage `{storage_free}` / `{storage}` GB
Cores: `{core}`
Boot time: <t:{re.sub(".[0-9]$", '', f'{boottime}')}:R>
__**Statistics**__
`{len(self.bot.guilds)}` guilds
`{users}` bot users
`{len(self.bot.commands)}` commands
`{voice:,}` voice channels
`{text:,}` text channels
"""
        await ctx.send(embed=e)
# `{len([c for c in set(self.bot.walk_commands())])}` commands

def setup(bot):
    bot.add_cog(Utility(bot))
