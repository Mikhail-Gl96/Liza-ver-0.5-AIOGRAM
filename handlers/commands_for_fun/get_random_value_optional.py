import random
from main import dp
from aiogram.types import Message


# command
# рандом (от) (до) - случайное число в диапазоне (от, до). Если нет "от", то диапазон (1, до). Если нет "от", то диапазон (1, 6)
@dp.message_handler(commands=['rand'])
async def get_random_optional(message: Message):
    try:
        num = None
        if message.text == '/rand':
            num = random.randint(1, 6)
        else:
            user_msg = message.text.split('/rand ')[1].split(' ')
            try:
                args = [int(arg) for arg in user_msg]
                if len(args) == 2:
                    start, end = args
                    # Конечное значение больше начального
                    if (end - start) > 0:
                        num = random.randint(start, end)
                    # Конечное число меньше начального
                    else:
                        num = random.randint(end, start)
                # Если один аргумент, то диапазон будет - (1, число)
                elif len(args) == 1:
                    num = random.randint(1, args[0])
            except ValueError:
                await message.reply("Один из аргументов - не число")
        await message.reply("Моё число - " + str(num))
    except Exception:
        await message.reply('Неизвестная ошибка')
