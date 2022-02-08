import asyncio

import discord
from discord.ext import commands

from Cogs import Cogs
from Commands import Commands
from config import config
from modules.logger import Logger

Bot = commands.Bot(command_prefix=config.COMMAND_PREFIX)

logger = Logger(
    'EthTracker',
    filehandler='INFO',
    streamhandler='DEBUG'
)


@Bot.event
async def on_ready():
    if Bot.is_ready():
        logger.info(
            f'Discord Bot now running. [{str(Bot.user.name)}] login success!')

if __name__ == '__main__':
    Bot.remove_command('help')
    Bot.remove_command('info')
    for cog in Cogs:
        Bot.add_cog(cog(Bot))
    for command in Commands:
        Bot.add_cog(command(Bot))
    Bot.run(config.DISCORD_TOKEN)

    # for module in env.COGS:
    #     Bot.add_cog(eval(module)(Bot))
    # for extension in env.EXTENSIONS:
    #     Bot.load_extension(f'modules.{extension}')
