import discord
import config
import traceback
from settings import cogloader

from discord.ext import commands


bot = commands.AutoShardedBot(
    command_prefix=commands.when_mentioned_or('?'),
    intents=discord.Intents.all(),
    allowed_mentions=discord.AllowedMentions.none(),
    max_messages=5000,
    status=discord.Status.online,
    activity=discord.Activity(type=discord.ActivityType.playing, name=f'in TPK'),
    description=f"I serve the kingdom of Paws."
)

for extension in cogloader.extensions:
    try:
        bot.load_extension(extension)
        print(f'[EXTENSION] {extension} has loaded successfully.')
    except Exception as e:
        tb = traceback.format_exception(type(e), e, e.__traceback__)
        tbe = "".join(tb) + ""
        print(f'[WARNING] Could not load extension {extension}: {tbe}')

bot.run(config.bottoken)