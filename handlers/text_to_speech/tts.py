import aiohttp
import langdetect
from gtts import gTTS
from langdetect import DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from config import yTTs_key, _separator
from aiogram.types import Message
import os
import random
import requests

from main import dp

from filters import *

ADDITIONAL_LANGUAGES = {
    'uk': 'Ukrainian',
}

DetectorFactory.seed = 0

# ('Голос', usage=["скажи [выражение] - бот сформирует "
#                                 "голосовое сообщение на основе текста голосом Google",
#                                 "озвуч [выражение] - бот сформирует "
#                                 "голосовое сообщение на основе текста голосом Yandex"])

FAIL_MSG = 'Я не смог это произнести :('


async def say_text_google_func(msg, message, format_audio='mp3'):
    # Используется озвучка гугла gTTS
    try:
        text, lang = await args_validation(msg, 'google', message)
        tts = gTTS(text=text, lang=lang)
        # Сохраняем файл с голосом
        # TODO: Убрать сохранение (хранить файл в памяти)
        name_audio = f'audio_google_{message.from_user.id}.{format_audio}'
        tts.save(name_audio)
        audio_file = open(name_audio, 'rb')
        return audio_file, name_audio
    except ValueError or TypeError:
        return Exception


async def say_text_yandex_func(msg, message, format_audio='mp3'):
    # Используется озвучка яндекса. Класс yTTS
    try:
        text, lang = await args_validation(msg, 'yandex', message)
        tts = yTTS(text=text, lang=lang, format='mp3')
        name_audio = f'.{_separator}audio_yandex_{message.from_user.id}.{format_audio}'
        tts.save_file(name=name_audio)
        audio_file = open(f'{name_audio}', 'rb')
        return audio_file, name_audio
    except ValueError:
        return Exception


def get_lang(text):
    try:
        lang = langdetect.detect(text)
        if lang in ('mk', 'bg'):
            lang = 'ru'
    except LangDetectException:
        lang = 'ru'
    return lang


async def args_validation(args=None, tts='google', message=None):
    # Функция проверяет текст на соответствие правилам
    # Возвращает текст и язык сообщения или возбуждает исключение
    google_limit = 450
    yandex_limit = 2000

    if not args or args is "":
        await message.answer('Вы не ввели сообщение!\nПример: voice_google текст')
        return ValueError

    text = ''.join(args)
    text_length = google_limit if tts == 'google' else yandex_limit
    if len(text) > text_length:
        await message.answer('Слишком длинное сообщение!')
        return ValueError

    lang = get_lang(text)
    return text, lang


async def get_data(url, params=None):
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url, data=params) as resp:
            if resp.status != 200:
                raise ValueError
            return await resp.read()


class yTTS(object):
    base_url = "https://tts.voicetech.yandex.net/tts"

    speakers = ['nick', 'silaerkan', "jane", "oksana", "alyss", "omazh", "zahar", "ermil", 'erkanyavas']
    emotion = ["good", "neutral", "evil"]

    # effects = ["behind_the_wall", "hamste ", "megaphone", "pitch_down", "psychodelic", 'pulse', 'train_announce']

    def __init__(self, text, lang='ru_RU', **kwargs):
        # for eff in self.effects:
        #     combinations = [self.speakers[i] + f' {eff}' for i in range(len(self.speakers))]
        #     self.speakers.extend(combinations)

        # Инициализируем данные для запроса
        self.params = {
            "text": text,
            "lang": self.get_lang_name(lang),
            "emotion": random.choice(self.emotion),
            "speaker": random.choice(self.speakers),
            "speed": random.uniform(0.8, 1.5),
            "format": kwargs.get('format_audio'),
        }
        if not yTTs_key:
            pass
        # else:
        #     key_yTTS = {'key': yTTs_key}
        #     self.params.update(key_yTTS)
        self.params.update(kwargs)

    # async def save(self):
    #     # Возвращает объект временного файла. Асинхронно.
    #     tmp = tempfile.NamedTemporaryFile(suffix='.mp3')
    #     data = await get_data(self.base_url, self.params)
    #     with open(tmp.name, 'wb') as f:
    #         f.write(data)
    #     return tmp

    def save_file(self, name='test.mp3', message=None):
        # Сохраняет в файл. Синхронно.
        # print(self.params)
        resp = requests.get(self.base_url, params=self.params, stream=True)
        # print(resp.url)
        resp.raise_for_status()
        with open(name, 'wb') as f:
            # f.write(resp.content)
            for chunk in resp.iter_content(chunk_size=1024):
                f.write(chunk)

    @staticmethod
    def get_lang_name(lang):
        # Преобразует коды стран в понятный формат для yandex speech cloud
        # Яндекс поддерживает только 4 языка: RU, UK, EN, TR
        languages = {
            'en': 'en_US',
            'ru': 'ru_RU',
            'uk': 'uk_UK',
            'tr': 'tr_TR',
        }
        if lang in languages:
            return languages[lang]
        else:
            return languages['ru']


# command
# Команда озвучить текст в mp3 аудиофайл как Google
@dp.message_handler(commands=['say_google'])
async def say_text_google(message: Message):
    try:
        text = message.text.split('say_google ')[1]
        answer = await say_text_google_func(text, message)
        # reply_audio
        await message.reply_audio(answer[0])
        os.remove(f'.{_separator}{answer[1]}')
    except IndexError:
        await message.reply('Добавьте к команде слово для озвучивания')


# command
# Команда озвучить текст в речь как Google
@dp.message_handler(commands=['voice_google'])
async def say_text_google(message: Message):
    try:
        text = message.text.split('voice_google ')[1]
        answer = await say_text_google_func(text, message, format_audio='ogg')
        # reply_audio
        await message.reply_audio(answer[0])
        os.remove(f'.{_separator}{answer[1]}')
    except IndexError:
        await message.reply('Добавьте к команде слово для озвучивания')


# command
# Команда озвучить текст в mp3 аудиофайл как Yandex
@dp.message_handler(commands=['say_yandex'])
async def say_text_yandex(message: Message):
    try:
        text = message.text.split('say_yandex ')[1]
        answer = await say_text_yandex_func(text, message)
        # reply_audio
        await message.reply_audio(answer[0])
        os.remove(f'{answer[1]}')
    except IndexError:
        await message.reply('Добавьте к команде слово для озвучивания')


# command
# Команда озвучить текст в речь как Yandex
@dp.message_handler(commands=['voice_yandex'])
async def voice_text_yandex(message: Message):
    try:
        text = message.text.split('voice_yandex ')[1]
        answer = await say_text_yandex_func(text, message, format_audio='ogg')
        # reply_audio
        await message.reply_voice(answer[0])
        os.remove(f'{answer[1]}')
    except IndexError:
        await message.reply('Добавьте к команде слово для озвучивания')
