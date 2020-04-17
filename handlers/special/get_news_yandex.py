from random import choice
import aiohttp
import xmltodict
import html
from main import dp
from aiogram.types import Message


# yandex news
news = {"армия": "https://news.yandex.ru/army.rss",
        "авто": "https://news.yandex.ru/auto.rss",
        "мир": "https://news.yandex.ru/world.rss",
        "главное": "https://news.yandex.ru/index.rss",
        "игры": "https://news.yandex.ru/games.rss",
        "интеренет": "https://news.yandex.ru/internet.rss",
        "кино": "https://news.yandex.ru/movies.rss",
        "музыка": "https://news.yandex.ru/music.rss",
        "политика": "https://news.yandex.ru/politics.rss",
        "наука": "https://news.yandex.ru/science.rss",
        "экономика": "https://news.yandex.ru/business.rss",
        "спорт": "https://news.yandex.ru/sport.rss",
        "происшествия": "https://news.yandex.ru/incident.rss",
        "космос": "https://news.yandex.ru/cosmos.rss"}


def unquote(data):
    temp = data
    if issubclass(temp.__class__, str):
        return html.unescape(html.unescape(temp))
    if issubclass(temp.__class__, dict):
        for k, v in temp.items():
            temp[k] = unquote(v)
    if issubclass(temp.__class__, list):
        for i in range(len(temp)):
            temp[i] = unquote(temp[i])
    return temp


# command
# news - показать новость, news [тема] - показать новость определённой тематики, news помощь/help - показать доступные темы
@dp.message_handler(commands=['news'])
async def get_yandex_news(message: Message):
    url = news["главное"]

    if message.text == '/news':
        args = ''
    else:
        args = ''.join(message.text.split('/news ')[1]).split(" ")

    if args:
        category = args.pop()

        if category.lower() in ["помощь", "помощ", "помоги", "помог", 'help']:
            await message.answer(f"news [тема], где тема - это одно из следующих слов:\n"
                                 f"{', '.join([k[0].upper() + k[1:] for k in news.keys()])}")

        if category.lower() in news:
            url = news[category]

    async with aiohttp.ClientSession() as sess:
        async with sess.get(url) as resp:
            xml = xmltodict.parse(await resp.text())
            items = xml["rss"]["channel"]["item"]
            item = unquote(choice(items))

            await message.answer(f'👉 {item["title"]}\n'
                                 f'👉 {item["description"]}')
