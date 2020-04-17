import aiohttp
from main import dp
from aiogram.types import Message


# command
# Отправить адрес сайта и получить скриншот (не со всеми сайтами сработает)
@dp.message_handler(commands=['screen'])
async def get_site_screenshot(message: Message):
    if message.text == '/screen':
        await message.reply('Вы не прислали сайт')
    else:
        user_msg = ''.join(message.text.split('/screen ')[1])
        async with aiohttp.ClientSession() as sess:
            async with sess.get("http://mini.s-shot.ru/1024x768/1024/png/?" + user_msg.strip()) as resp:
                await message.reply_photo(await resp.read())
