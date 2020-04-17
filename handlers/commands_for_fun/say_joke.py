from main import dp
from aiogram.types import Message
import aiohttp


URL = "http://rzhunemogu.ru/RandJSON.aspx?CType=1"


# command
# Присылает рандомную шутку
@dp.message_handler(commands=['rzhu'])
async def get_joke_from_rzhunemogu(message: Message):
    async with aiohttp.ClientSession() as sess:
        async with sess.get(URL) as resp:
            text = await resp.text()
            joke = "".join(text.replace('\r\n', '\n').split("\"")[3:-1])
            await message.answer(joke)
