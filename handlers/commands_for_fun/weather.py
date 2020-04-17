from main import dp
from aiogram.types import Message
import time
import aiohttp
from config import _accuweather_api_key


# сервис для определения погоды: http://openweathermap.org/api
# введите свой ключ, если будете использовать!
code = _accuweather_api_key
default_city = "Москва"

if code is None or '':
    code = "fe198ba65970ed3877578f728f33e0f9"
    # open key, not recommended

text_to_days = {"завтра": 1, "послезавтра": 2, "через день": 2, "через 1 день": 2,
                "через 2 дня": 3, "через 3 дня": 4, "через 4 дня": 5,  "через 5 дней": 6,
                "через 6 дней": 7, "через 7 дней": 8}


# command
# Команда погода [город] [опционально: когда]- показать погоду в городе (в именительном падеже) завтра, послезавтра, через 1-7 дней
@dp.message_handler(commands=['weather'])
async def when_func(message: Message):
    if message.text == '/weather':
        user_msg = None
    else:
        user_msg = ''.join(message.text.split('/weather')[1])

    city = default_city
    days = 0

    if user_msg:
        arguments = "".join(user_msg)

        for k, v in sorted(text_to_days.items(), key=lambda x: -len(x[0])):
            if k in arguments:
                arguments = arguments.replace(k, "")
                days = v

        possible_city = arguments.replace(" в ", "").strip()

        if possible_city:
            city = possible_city

    if days == 0:
        url = f"http://api.openweathermap.org/data/2.5/weather?APPID={code}&lang=ru&q={city}"
    else:
        url = f"http://api.openweathermap.org/data/2.5/forecast/daily?APPID={code}&lang=ru&q={city}&cnt={days + 1}"

    async with aiohttp.ClientSession() as sess:
        async with sess.get(url) as resp:
            response = await resp.json()
            if "cod" in response and response["cod"] == '404':
                return await message.answer("Город не найден!")

            if days != 0:
                answer = f"{city}. Погода.\n\n"

                for i in range(1, len(response["list"])):
                    day = response["list"][i]
                    temperature = day["temp"]["day"] - 273
                    humidity = day["humidity"]
                    description = day["weather"][0]["description"]
                    wind = day["speed"]
                    cloud = day["clouds"]
                    date = time.strftime("%Y-%m-%d", time.gmtime(day["dt"]))

                    answer += (f'{date}:\n'
                               f'{description[0].upper()}{description[1:]}\n'
                               f'Температура: {round(temperature, 2)} °C\n'
                               f'Влажность: {humidity} %\n'
                               f'Облачность: {cloud} %\n'
                               f'Скорость ветра: {wind} м/с\n\n')
                return await message.answer(answer)
            else:
                result = response

                description = result["weather"][0]["description"]
                temperature = result["main"]["temp"] - 273
                humidity = result["main"]["humidity"]
                wind = result["wind"]["speed"]
                cloud = result["clouds"]["all"]

                answer = (f'{city}. Текущая погода.\n'
                          f'{description[0].upper()}{description[1:]}\n'
                          f'Температура: {round(temperature, 2)} °C\n'
                          f'Влажность: {humidity} %\n'
                          f'Облачность: {cloud} %\n'
                          f'Скорость ветра: {wind} м/с')
                return await message.answer(answer)
