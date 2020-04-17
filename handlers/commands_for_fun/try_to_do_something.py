import random
from main import dp
from aiogram.types import Message


answers = ['Успех  ✅', 'Неудачно  ❌', 'Попробуй еще раз  ⚠ ']


# command
# Спросить бота получится ли что-то у меня
@dp.message_handler(commands=['try'])
async def get_evaluating_of_something(message: Message):
    if message.text == '/try':
        user_msg = ''
    else:
        user_msg = ''.join(message.text.split('/try ')[1])
    await message.reply(answers[random.randint(0, len(answers) - 1)] + ' \nВаш запрос: ' + str(user_msg))

