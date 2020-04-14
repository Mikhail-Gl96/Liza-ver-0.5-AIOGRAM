from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery


class Button(BoundFilter):
    def __init__(self, key, contains=False):
        self.key = key
        self.contains = contains

    async def check(self, message) -> bool:
        if isinstance(message, Message):    # Если это обычное сообщение тип Message
            if self.contains:
                return self.key in message.text
            else:
                return message.text == self.key
        elif isinstance(message, CallbackQuery):    # Если это CallbackQuery сообщение
            if self.contains:
                return self.key in message.data
            else:
                return self.key == message.data

# Button('Кнопка 1')