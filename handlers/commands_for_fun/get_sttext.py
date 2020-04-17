from main import dp
from aiogram.types import Message, ParseMode
from aiogram.utils.markdown import strikethrough, bold, hstrikethrough

# def hide_link(url: str) -> str:
#     """
#     Hide URL (HTML only)
#     Can be used for adding an image to a text message
#
#     :param url:
#     :return:
#     """
#     return f'<a href="{url}">&#8203;</a>'

# def get_sttext(text):
#     sttext = '&#38;#0822;'+'&#38;#0822;'.join(text) + '&#38;#0822;'
#     return sttext


# command
# Перечеркнуть написанное слово
@dp.message_handler(commands=['stext'])
async def strikethroughtext(message: Message):
    if message.text == '/stext':
        await message.reply('Вы не прислали текст')
    else:
        user_msg = hstrikethrough(''.join(message.text.split('/stext ')[1]))
        await message.answer(user_msg, parse_mode=ParseMode.HTML)
