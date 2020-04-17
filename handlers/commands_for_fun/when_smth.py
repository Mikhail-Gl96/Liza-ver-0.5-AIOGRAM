import random
from main import dp
from aiogram.types import Message


answers = [f'через {random.randint(1, 59)} минут(ы) {random.randint(1, 59)} секунд(ы)',
          f'через {random.randint(1, 59)} минут(ы)', f'через {random.randint(1, 31)} дней(день)',
          f'через {random.randint(1, 12)} месяца(ев)', f'через {random.randint(1, 1000)} лет(год)',
          'сейчас', 'завтра', 'послезавтра', 'после обеда', 'вечером', 'когда рак на горе свистнет', 'никогда']


# command
# Команда когда [текст после когда]- выбрать случайную дату когда произойдет что вынаписали
@dp.message_handler(commands=['when'])
async def when_func(message: Message):
    if message.text == '/when':
        user_msg = ''
    else:
        user_msg = ''.join(message.text.split('/when ')[1])
    await message.reply(answers[random.randint(0, len(answers) - 1)] + " " + str(user_msg))


