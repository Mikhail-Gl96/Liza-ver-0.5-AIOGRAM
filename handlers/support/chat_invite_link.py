from main import dp
from aiogram.types import Message


# command
# Создает ссылку на вступление в группу (предыдущая ссылка станет недействительна)
@dp.message_handler(commands=['chat_link'])
async def get_chat_invite_link(message: Message):
    if message.from_user.id != message.chat.id:
        link = await message.chat.export_invite_link()
        await message.answer(link)
    else:
        await message.reply('Создать ссылку не возможно, так как это личные сообщения')
