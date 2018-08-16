from discord.ext import commands
import os

bot = commands.Bot(
    command_prefix='!',
    description='Ultra-intelligent Card Playing AI')

extensions = ['cogs.SARAH']

for extension in extensions:
    bot.load_extension(extension)

bot.run(os.environ.get('TOKEN'))
