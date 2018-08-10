from discord.ext import commands
import os

bot = commands.Bot(
    command_prefix='!',
    description='Ultra-intelligent Card Playing AI')

extensions = ['cogs.SARAH']

for extension in extensions:
    bot.load_extension(extension)

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(os.environ.get('TOKEN'))
