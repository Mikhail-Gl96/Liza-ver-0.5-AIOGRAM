# from main import dp, bot
# from aiogram.types import Message
# import requests
# import random
#
#
# api_link_stt = 'https://speech.googleapis.com/v1p1beta1/speech:recognize'
#
# Request_body = {
#   "audio": {
#     "content": f"/* Your audio */"
#   },
#   "config": {
#     "enableAutomaticPunctuation": True,
#     "encoding": "LINEAR16",
#     "languageCode": "ru-RU",
#     "model": "default"
#   }
# }
#
#
# class yTTS(object):
#     base_url = "https://stt.api.cloud.yandex.net/speech/v1/stt:recognize"
#
#     def __init__(self, lang='ru_RU', **kwargs):
#         # Инициализируем данные для запроса
#         self.params = {
#             "lang": self.get_lang_name(lang),
#             "topic": 'general',
#             "profanityFilter": False,
#             "format": 'ogg',
#         }
#         self.params.update(kwargs)
#
#     def get_text(self):
#         resp = requests.get(self.base_url, params=self.params, stream=True)
#         resp.raise_for_status()
#         print(resp.content)
#     @staticmethod
#     def get_lang_name(lang):
#         # Преобразует коды стран в понятный формат для yandex speech cloud
#         # Яндекс поддерживает только 4 языка: RU, UK, EN, TR
#         languages = {
#             'en': 'en_US',
#             'ru': 'ru_RU',
#             'tr': 'tr_TR',
#         }
#         if lang in languages:
#             return languages[lang]
#         else:
#             return languages['ru']
#
#
# # command
# # Распознования речи в текст
# @dp.message_handler(commands=['stt'])
# async def speech_to_text(message: Message):
#     reply_msg_id = message.reply_to_message.message_id
#     voice_msg_id = message.reply_to_message.voice.file_id
#     data_bytes = await dp.bot.get_file(voice_msg_id)
#     print(message)
#
#
#
#     await message.answer(f'{message.reply_to_message}')
#
#
#
