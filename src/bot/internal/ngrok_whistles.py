import aiohttp
from aiohttp import BasicAuth

from src.config import settings


async def blink1_blue():
    async with aiohttp.ClientSession() as session:
        auth = BasicAuth(settings.NGROK_USER.get_secret_value(), settings.NGROK_PASS.get_secret_value())
        ngrok_url = settings.NGROK_URL.get_secret_value()
        await session.get(ngrok_url + 'blink/blue', auth=auth)


async def sheet_update(cell: str, value: int):
    async with aiohttp.ClientSession() as session:
        auth = BasicAuth(settings.NGROK_USER.get_secret_value(), settings.NGROK_PASS.get_secret_value())
        ngrok_url = settings.NGROK_URL.get_secret_value()
        await session.get(ngrok_url + f'update/sheet/{cell}/{value}', auth=auth)
