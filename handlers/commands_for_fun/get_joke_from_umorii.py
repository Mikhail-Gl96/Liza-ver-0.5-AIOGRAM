from main import dp
from aiogram.types import Message
import aiohttp
import json
import random
from parsers import html_decode

# URL = "http://rzhunemogu.ru/RandJSON.aspx?CType=1"

URL = 'http://umorili.herokuapp.com/api/random?num='


# command
# Присылает рандомную шутку
@dp.message_handler(commands=['rumor'])
async def get_joke_from_rzhunemogu(message: Message):
    random_max_number = str(random.randint(1, 50))
    async with aiohttp.ClientSession() as sess:
        async with sess.get(URL + random_max_number) as resp:
            text = await resp.text()
            text = json.loads(text)
            # print(len(text), text)
            choosen_joke_num = random.randint(0, len(text))
            joke = html_decode(text[choosen_joke_num]['elementPureHtml'])
            # print(joke)
            await message.answer(joke)

