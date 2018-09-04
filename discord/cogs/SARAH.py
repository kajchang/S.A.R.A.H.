from discord.ext import commands
import discord
import aiohttp
import asyncio
from io import BytesIO
import re


class SARAH:
    def __init__(self, bot):
        self.bot = bot

        @self.bot.event
        async def on_message(message):
            async with aiohttp.ClientSession() as session:
                bracket_pattern = '\[(.*?)\]'

                card_matches = re.findall(bracket_pattern, message.content)

                for card in card_matches:
                    async with session.get('http://novablitz.pythonanywhere.com/cards/{}'.format(''.join(card.split()))) as response:
                        if response.status == 200:
                            card_data = await response.json()

                            async with session.get(card_data['image']) as response:
                                image = BytesIO(await response.read())

                            await self.bot.send_file(message.channel, fp=image, filename='{}.png'.format(card_data['name']))

                else:
                    await self.bot.process_commands(message)

        @self.bot.event
        async def on_ready():
            await self.bot.change_presence(game=discord.Game(name='NovaBlitz'))

    @commands.command(pass_context=True, description='Searches for a card')
    async def card(self, ctx, *args):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://novablitz.pythonanywhere.com/cards/{}'.format(''.join(arg for arg in args))) as response:
                if response.status == 404:
                    await self.bot.say('No Cards Found.')

                else:
                    card_data = await response.json()
                    async with session.get(card_data['image']) as response:
                        image = BytesIO(await response.read())

                    await self.bot.send_file(ctx.message.channel, fp=image, filename='{}.png'.format(card_data['name']))

    @commands.command(description='Information on Nova Token')
    async def nvt(self):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.coingecko.com/api/v3/coins/nova-token') as response:
                token_data = await response.json()
                change = float(token_data['market_data']
                               ['price_change_percentage_24h'])
                embed = discord.Embed(
                    title='Nova Token', type='rich', color=discord.Colour(0x40e0d0))
                embed.add_field(name='Price', value='${0:f}'.format(token_data['market_data']
                                                                    ['current_price']['usd']))
                embed.add_field(name='24h Change', value='{0:f}% {1}'.format(
                    change, ':chart_with_downwards_trend:' if change < 0 else (':chart_with_upwards_trend:' if change > 0 else ':bar_chart:')))
                embed.add_field(
                    name='Info', value='[Token Information](https://novablitz.com/token-sale/)')
                embed.add_field(
                    name='Exchanges', value='Buy on [Radar Relay](https://app.radarrelay.com/NVT/WETH) and [ForkDelta](https://forkdelta.app/#!/trade/NVT-ETH)')

                await self.bot.say(embed=embed)

    @commands.command(description='Links for Playing NovaBlitz')
    async def play(self):
        embed = discord.Embed(title='How to Get NovaBlitz',
                              type='rich', color=discord.Colour(0x40e0d0))
        embed.add_field(
            name='Steam', value='[Download for Free on Steam](http://store.steampowered.com/app/388370)')
        embed.add_field(
            name='Mobile Beta', value='[Sign Up for the Mobile Beta](https://goo.gl/forms/yC7tMdlERUctx2d53)', inline=False)

        await self.bot.say(embed=embed)

    @commands.command(description='Information on this bot')
    async def info(self):
        embed = discord.Embed(title='Bot Information',
                              type='rich', color=discord.Colour(0x40e0d0))
        embed.add_field(name='Author', value='<@288851267847979010>')
        embed.add_field(
            name='Github Repo', value='[Bot Repository](https://github.com/kajchang/S.A.R.A.H.)')
        embed.add_field(name='Add to Your Server',
                        value='[Invite Me](https://discordapp.com/oauth2/authorize?client_id=476208085246017536&scope=bot&permissions=0)')

        await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(SARAH(bot))
