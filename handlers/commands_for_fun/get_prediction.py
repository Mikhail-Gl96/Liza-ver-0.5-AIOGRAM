import random
from main import dp
from aiogram.types import Message


# Инициализируем возможные ответы
answers = '''Абсолютно точно!
Да.
Нет.
Скорее да, чем нет.
Не уверен...
Однозначно нет!
Если ты не фанат аниме, у тебя все получится!
Можешь быть уверен в этом.
Перспективы не очень хорошие.
А как же иначе?.
Да, но если только ты не смотришь аниме.
Знаки говорят — «да».
Не знаю.
Мой ответ — «нет».
Весьма сомнительно.
Не могу дать точный ответ.
'''.splitlines()


# command
# Спросить у шара предсказаний
@dp.message_handler(commands=['orbp'])
async def tell_truth(message: Message):
    await message.reply("🔮" + random.choice(answers))

