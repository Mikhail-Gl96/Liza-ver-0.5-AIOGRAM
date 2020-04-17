Бот Лиза
======

## Для работы бота необходим<br>Python 3.6+ <br>С версиями ниже бот не работает


## Настройка
1. Перейдите в папку с ботом
2. Установить зависимости из файла `requirements.txt`<br>
   Возможные команды для установки:<br>
   `pip3 install -r requirements.txt`<br>
   `python -m pip install -r requirements.txt`<br>
   `python3.6 -m pip install -r requirements.txt`

3. Создайте файл config.py
4. Заполните файл config.py в соответствии с файлом config_example (открывается блокнотом)
5. Запустите бота<br>
   Возможные команды для запуска(из консоли, из папки с ботом):<br>
   `python3 main.py`<br>
   `python main.py`<br>
   `python3.6 main.py`<br>

Текущая версия бота: 0.5


## Команды

Все команды бота находятся в папке handlers.


Для распознавания речи в текст (Speech-to-Text) необходимо установить ffmpeg и указать путь к нему в файле config.py
(пример см. в файле config_example)б <br>

Внимание, для работы команды распознавания речи в текст необходимо получить .json ключ в google api. 
Необходимая технология называется Cloud Speech-to-Text
https://cloud.google.com/speech-to-text?hl=ru

## Создание команды

Пример оформления команды можно найти в файле handlers.py

Правильно оформленные команды автоматически собираются скриптом bot_commands.py и формируют один файл с import всех функций, оформленных по следующему правилу:
```
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
```


## Что нового будет до 1.0?

* Будет добавлено несколько игр (скорее всего с поддержкой клавиатур телеграмма)
* Возможно я когда-нибудь напишу requirements.txt  🤣🤣🤣
* Будет добавлено несколько команд развлекательного характера


## Что нового будет в 1.0?

Будет сделано:
* Модуль для работы с VK API от лица пользователя, а не как бот (CallbackApi, а не LongPoll)
(я очень очень надеюсь на это 🤣)
* Добавлена работа с БД
* Может быть будет прикручен Docker (там будет и бот, и бд)



## Связь с разработчиком

Разработчиков этого бота можно найти в вк:
* https://vk.com/id18456544


