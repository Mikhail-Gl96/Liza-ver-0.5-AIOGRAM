from main import dp
from config import BOT_NAME
from filters import *
from bot_commands import get_all_commands as get_BOT_COMMANDS


# command
# Команда вызова помощи
@dp.message_handler(commands=['help'])
async def help_msg(message: Message):
    BOT_COMMANDS = get_BOT_COMMANDS()
    commands = [f'/{i} - {BOT_COMMANDS.get(i)},\n' for i in BOT_COMMANDS.keys()]
    await message.answer(f'Привет, я {BOT_NAME}.\n'
                         f'Я умею делать следующе вещи:\n{"".join(commands)}')
