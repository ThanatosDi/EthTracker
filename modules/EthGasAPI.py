import json

import aiohttp
from config import config


class EthGasAPI():
    def __init__(self):
        self._respond = None

    async def fetch(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(config.ETH_API) as response:
                if response.status == 200:
                    self._respond = json.loads(await response.text())
                    return self._respond
                return None

    @property
    def gas(self):
        if self._respond == None:
            return 0
        return self._respond['normal']['gwei']

    @property
    def price(self):
        if self._respond == None:
            return 0
        return self._respond['ethPrice']

    @property
    def respond(self) -> dict:
        if self._respond == None:
            return {}
        return self._respond
