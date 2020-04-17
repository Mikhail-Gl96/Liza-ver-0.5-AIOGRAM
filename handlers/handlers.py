from main import bot, dp

from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from aiogram.types import Message, CallbackQuery, Chat
from config import admin_id, BOT_NAME
from keyboard import ListOfButtons
from filters import *
from aiogram.dispatcher.storage import FSMContext
from states import Form
import json
from bot_commands import import_all_commands_functions
import_all_commands_functions()  # Create a file with functions for import
# Import all handler's functions from other dirs
from filename_handler_functions_import import *


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='Бот запущен')


# Абсолютно не обязательно создавать свой фильтр для текста, так как есть встроенный.
# @dp.message_handler(text="text")
# @dp.message_handler(text_contains="text")
# @dp.message_handler(text_startswith="text")
# @dp.message_handler(text_endswith="text")

# Работает для message, callback_query, inline_query и poll хендлеров
# Вот почитать https://github.com/aiogram/aiogram/blob/dev-2.x/aiogram/dispatcher/filters/builtin.py#L203

"""
How to make the collector automatically collect information about the functions?

Example:
# command  <-- This string "# command" is needed if you want your function be seen for the collector
# Команда первого приветсвия нового пользователя    <-- This is the description of function which would be posted via 
                                                        help message
@dp.message_handler(commands=['start'])      <-- Now the script search for "@dp.message_handler(commands=[" part 
                                                 to show the function in help message 
        (commands=['start', 'start1', ...])  <-- You can set more commands separate by comma

< the normal example of async handler's function is below >
async def start_msg(message: Message):
    await message.answer(f'Привет, я {BOT_NAME}. Чтобы узнать как мной управлять - напиши команду /help')
"""


# command
# Команда первого приветсвия нового пользователя
@dp.message_handler(commands=['start'])
async def start_msg(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name} {message.from_user.last_name}.\n'
                         f'Я {BOT_NAME}. Чтобы узнать меня поближе - напиши команду /help')


# command
# Команда тестовая
@dp.message_handler(commands=['rnj'])
async def who_is(message: Message):
    new_str = '\n'
    admins = await message.chat.get_administrators()
    data = f'info = {message.text}\n ' \
        f'who= {message.from_user}\n' \
        f'chat= {message.chat}\n' \
        f'members={await message.chat.get_members_count()}\n' \
        f'text= {message.text}\n {message.chat.description}'
    await message.answer(data)




# @dp.message_handler(state=Form.Name)
# async def name_func(message: Message, state: FSMContext):
#     name = message.text
#     await state.update_data(name=name)
#     await message.answer('Введите фамилию')
#     await Form.Surname.set()

#
#
# @dp.message_handler(state=Form.Surname)
# async def name_func(message: Message, state: FSMContext):
#     surname = message.text
#     await state.update_data(surname=surname)
#     await message.answer('Введите фамилию')
#     data = await state.get_data()
#     print(data)
#     text = f'Name = {data["name"]}\nSurname= {data["surname"]}'
#     await state.reset_state(with_data=False)
#     await message.answer(text=text)
#
#
# @dp.message_handler(commands=['info'])
# async def e_else(message, state):
#     data = await state.get_data()
#     print(data, type(data))
#     if not data:
#         await message.answer('Я вас еще не знаю')
#     else:
#         await message.answer("Вы прошли регистрацию. Вас зовут {name} {surname}".format(**data))

# @dp.message_handler()
# async def echo(message: Message):
#     text = f'Привет, ты написал: {message.text}'
#     # await bot.send_message(chat_id=message.from_user.id,
#     #                        text=text)
#     await message.answer(text=text)

# @dp.message_handler()
# async def echo(message: Message):
#     text = f'Привет, ты написал: {message.text}'
#     # await bot.send_message(chat_id=message.from_user.id,
#     #                        text=text)
#     await message.answer(text=text)


# @dp.message_handler(text_startswith="Привет")
# async def hello_user(message: Message):
#     await message.reply(f"Привет {message.from_user.first_name} {message.from_user.last_name}")
#
#
# @dp.message_handler(Button('Кошелек'))
# async def btn1(message: Message):
#     await message.reply("Вы нажали на кнопку 1", reply_markup=ReplyKeyboardRemove())
#
#
# @dp.callback_query_handler(Button('user', contains=True))
# async def c_btn1(call: CallbackQuery):
#     await call.message.edit_reply_markup()  # Закрыть клавиатуру
#     await call.message.reply(call.data)
#     username = call.data.split('user ')[1]
#     await call.message.reply(f"Вы нажали на кнопку 1. Вы {username}")
#
#
# @dp.message_handler(Button('Имя'))
# async def btn1(message: Message):
#     await message.reply("Вы нажали на кнопку Имя", reply_markup=ReplyKeyboardRemove())
#
#
# @dp.callback_query_handler(Button('2'))
# async def c_btn1(call: CallbackQuery):
#     await call.message.edit_reply_markup()  # Закрыть клавиатуру
#     await call.message.reply("Вы нажали на кнопку 2 Имя")
#
#
# @dp.message_handler()
# async def keyboards(message: Message):
#     text = "Нажми на кнопку"
#     keyboard = ListOfButtons(
#         text=["Кошелек", "Имя"],
#         callback=[f'user {message.from_user.first_name} {message.from_user.last_name}', '2'],
#         align=[2]
#     ).inline_keyboard
#     # inline_keyboard - клава в чате
#     # reply_keyboard - Клава как кнопки
#     await message.reply(text=text, reply_markup=keyboard)



