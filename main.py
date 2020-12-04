import asyncio
import aiohttp

from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN, _host, _port, _login_proxy, _password_proxy, _proxy_type
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# PROXY_AUTH = aiohttp.BasicAuth(login=_login_proxy, password=_password_proxy)

loop = asyncio.get_event_loop()     # Создание асинхронного потока
# Тип парсинга - теги как в html
# bot = Bot(token=BOT_TOKEN, parse_mode='HTML', proxy=f'{_proxy_type}://{_host}:{_port}', proxy_auth=PROXY_AUTH)
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot=bot, loop=loop, storage=MemoryStorage())  # Доставщик сообщений

if __name__ == '__main__':
    from handlers.handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)
