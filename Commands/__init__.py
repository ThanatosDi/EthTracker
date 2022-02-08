import discord
from discord.ext import commands

from .EthCommand import EthCommand

Commands = [EthCommand]

# def setup(bot: commands.Bot):
#     for command in Commands:
#         bot.add_cog(command(bot))
