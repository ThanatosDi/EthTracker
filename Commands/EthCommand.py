import discord
from discord.ext import commands
from modules.EthGasAPI import EthGasAPI
from modules.logger import Logger

logger = Logger(
    name="EthCommand"
)

class EthCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.eth_api = EthGasAPI()

    @commands.slash_command(name='gas')
    async def eth(self, ctx: discord.ApplicationContext):
        await self.eth_api.fetch()
        respond = self.eth_api.respond
        respond.pop('sources', None)
        embed=discord.Embed(title="Eth Gas and Price", description="Ethereum Gas and Price", color=0xff0000)
        ethPrice = respond.pop('ethPrice', 0)
        lastUpdated = int(str(respond.pop('lastUpdated', 0))[:10])
        for key, value in respond.items():
            embed.add_field(name=key, value=f"GWEI: {value['gwei']}", inline=False)
        embed.add_field(name='Eth Price', value=ethPrice, inline=False)
        embed.add_field(name='Last Updated', value=f'<t:{lastUpdated}>', inline=False)
        await ctx.respond(embed=embed)




