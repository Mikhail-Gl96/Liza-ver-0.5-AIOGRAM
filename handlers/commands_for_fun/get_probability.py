from main import dp
from aiogram.types import Message
import random


# command
# Команда пришлет вероятность вашего запроса
@dp.message_handler(commands=['prob'])
async def get_probability(message: Message):
    num = random.random()
    try:
        if message.text == '/prob':
           user_msg = ' '
        else:
            user_msg = '"' + ''.join(message.text.split('/prob ')[1]) + '":  '
        await message.answer('\n' + 'Вот ваша вероятность 🔎 ' + str(user_msg + str(num.__round__(1) * 100) + '%'))
    except ValueError:
        await message.reply_photo('Произошла неизвестная ошибка')
