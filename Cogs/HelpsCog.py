import discord
from discord.ext import commands

class HelpsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.Bot = bot

    @commands.slash_command()
    async def info(self, ctx: discord.ApplicationContext):
        embed = discord.Embed(
            title=self.Bot.user.name, description=f'{self.Bot.user.name} 機器人', color=0xeee657)
        dataset = {
            'Author': 'ThanatosDi',
            'Server count': len(self.Bot.guilds),
            'py-cord version': f"{discord.__version__} {discord.version_info.releaselevel}"
        }
        for key, value in dataset.items():
            embed.add_field(name=key, value=value)
        return await ctx.respond(embed=embed)
    
    @commands.slash_command()
    async def invite(self, ctx: discord.ApplicationContext):
        embed = discord.Embed()
        embed.description = "[invite](https://discord.com/api/oauth2/authorize?client_id=929801458558312498&permissions=414464732224&scope=bot%20applications.commands)"
        return await ctx.respond(embed=embed)