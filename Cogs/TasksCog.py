import json
from datetime import datetime

import aiohttp
import discord
from config import config
from discord.ext import commands, tasks
from modules.EthGasAPI import EthGasAPI
from modules.logger import Logger

logger = Logger(
    name=__name__,
    filehandler=config.LOG_LEVEL, 
    streamhandler=config.STDOUT_LEVEL
)

class EthGasTaskCog(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot
        self.eth_api = EthGasAPI()
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(minutes=5)
    async def printer(self):
        await self.eth_api.fetch()
        now = datetime.now().strftime('%H:%M:%S')
        activity = discord.Activity(
            name=f"Gas: {self.eth_api.gas} Price: {self.eth_api.price} Update: {now}", 
            type=3
        )
        return await self.bot.change_presence(activity=activity)
    
    @printer.before_loop
    async def before_printer(self):
        logger.info(f'等待 Bot 執行...')
        await self.bot.wait_until_ready()