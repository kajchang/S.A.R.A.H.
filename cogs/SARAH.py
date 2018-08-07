from discord.ext import commands
import discord
import aiohttp
import asyncio
from io import BytesIO


class SARAH:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, description='Search for information on a card.')
    async def card(self, ctx, *args):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://novablitz.pythonanywhere.com/cards/{}'.format(''.join(arg for arg in args))) as response:
                if response.status == 404:
                    await self.bot.say('No Cards Found.')

                else:
                    card_data = await response.json()
                    async with aiohttp.ClientSession() as session:
                        async with session.get(card_data['image']) as response:
                            image = BytesIO(await response.read())

                    await self.bot.send_file(ctx.message.channel, fp=image, filename='{}.png'.format(card_data['name']))


def setup(bot):
    bot.add_cog(SARAH(bot))
