import random
from main import dp
from aiogram.types import Message


good_arr = ['Норм', 'C пивком потянет', 'Неплохо, но можно и лучше', 'Старайся и все получится',
            'Когда-нибудь ты получишь больше баллов', 'Брачное ложе предназначено для двоих: этой херни и тебя',
            'Когда-нибудь вы достигнете уровня Чиркова',
            'все не так плохо как я думала', 'Улыбайтесь - это всех раздражает. Ведь вы впереди других',
            'Может быть вам повернется удача и вы станете известным']
neg_arr = ['Пожалуйста, перестант этим заниматься', 'Подумой, астанавись', 'Не хочу больше такое оценивать',
           'Удалите это немедленно', 'Кровь из глаз и ушей', 'Как я и подозревала, ты — всего лишь человек.',
           'Разъярённого муравья тебе в трусы за такое!', 'Пора найти тебе парня...',
           'Кажется, это что-то неполноценное']

abs_pos = ['ВСе чики-пуки', 'Вау, легенда', 'Почти невозможно', 'Божественно', 'Это Илон Маск???',
           'Это точно не спизжено? Я не верю', 'Как это так удается???', 'За вами следят с Нибиру',
           'Вы почти Замай', 'Весь мир у ваших ног', 'Шедевры не подвергаются критике', 'Лучше только Путин',
           'Надеюсь, вы останетесь на вершине Олимпа']
abs_neg = ['Я так никогда не блевала', 'Г о в н о', 'Удалите это немедленно', 'Это точно не говно?',
           'Хуже только рэп батл', 'Если решишь блевать — сейчас лучший момент',
           'Вы достигли уровня треков Блэк стар', 'Ни богу свечка, ни чёрту кочерга.', 'Вас пора сослать в Гулаг',
           'Убогие вас сторонятся']


# command
# Оценить свои шансы на что-то
@dp.message_handler(commands=['eval'])
async def get_evaluating_of_something(message: Message):
    ext_answer = None
    points = random.randint(0, 10)
    max_points = 10
    med_points = int(max_points / 2)
    zero_point = int(max_points / 5)
    if points == max_points:
        ext_answer = random.choice(abs_pos)
    elif points <= zero_point:
        ext_answer = random.choice(abs_neg)
    elif points == 0 or points == 1:
        ext_answer = random.choice(abs_neg)
    elif points >= med_points:
        ext_answer = random.choice(good_arr)

    elif points < med_points and points > zero_point:
        ext_answer = random.choice(neg_arr)
    else:
        return await message.reply(
            f'Ошибка команды оценка\nmax_points = {max_points}\nmed_points = {med_points}\nzero_point = {zero_point}\npoints = {points}')
    answer = f'Моя оценка: {points} из 10\n{ext_answer}'

    await message.reply(str(answer))
