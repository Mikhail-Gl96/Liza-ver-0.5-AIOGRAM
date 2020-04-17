from main import dp
from config import BOT_NAME
from filters import *
from bot_commands import get_all_commands as get_BOT_COMMANDS


# command
# Команда вызова помощи
@dp.message_handler(commands=['help'])
async def help_msg(message: Message):
    new_str = '\n'
    BOT_COMMANDS = get_BOT_COMMANDS()
    commands = [f'/{i} - {BOT_COMMANDS.get(i)},\n' for i in BOT_COMMANDS.keys()]
    # add additional commands of one function which are comma-separated
    for i in range(len(commands)):
        split_left = commands[i].split(' -')[0]
        if split_left.count(',') > 0:
            split_left_corrected = split_left.replace(', ', ', /')
            commands[i] = split_left_corrected + commands[i].split(' -')[1]
    await message.answer(f'Привет, я {BOT_NAME}.\n'
                         f'Я умею делать следующе вещи:\n\n{f"{new_str}".join(commands)}')
