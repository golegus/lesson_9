import random

numbers_by_text={
    1:'первое',
    2:'второе', 
    3:'третье',
    4:'четвертое',
    5:'пятое',
    6:'шестое',
    7:'седьмое',
    8:'восьмое',
    9:'девятое',
    10:'десятое',
    11:'одиннадцатое',
    12:'двенадцатое',
    13:'тринадцатое',
    14:'четырнадцатое',
    15:'пятнадцатое',
    16:'шестанадцатое',
    17:'семнадцатое',
    18:'восемнадцатое',
    19:'девятнадцатое',
    20:'двадцатое',
    30:'тридцатое'
}
months_by_text={
    1:'января',
    2:'февраля',
    3:'марта',
    4:'апреля',
    5:'мая',
    6:'июня',
    7:'июля',
    8:'августа',
    9:'сентября',
    10:'октября',
    11:'ноября',
    12:'декабря'
}

birthdays = {
    'Гвидо Ван Россум': '31.01.1956',
    'Линус Торвальдс': '28.12.1969',
    'Пол Маккартни': '18.06.1942',
    'Михаил Гельфанд': '25.10.1963',
    'Мария Кюри': '07.11.1867',
    'Илон Маск': '28.06.1971',
    'Чарли Чаплин': '16.04.1889',
    'Алан Мэтисон Тьюринг': '23.06.1912',
    'Альберт Энштейн': '14.03.1879',
    'Мэрилин Монро': '01.06.1926'   
}
keys_of_birthdays=list(birthdays.keys())
numbers=[0,1,2,3,4,5,6,7,8,9]

while True:
    random_persons=random.sample(numbers,5)
    print('Программа рандомно выбрала пять известных людей. \nВведите дату рождения каждого в формате \'dd.mm.yyy\'')
    score=0
    for i in random_persons:
        get_birthday=input(f'День рождения {keys_of_birthdays[i]}: ')
        if get_birthday!=birthdays[keys_of_birthdays[i]]:
            print('Неверно!')
            real_birthday=birthdays[keys_of_birthdays[i]].split('.')
            birth_day=int(real_birthday[0])
            birth_month=int(real_birthday[1])
            birth_year=real_birthday[2]
            if birth_day<21:
                birth_day=numbers_by_text[birth_day]
            elif birth_day<31:
                birth_day=f'двадцать {numbers_by_text[birth_day-20]}'
            else:
                birth_day='тридцать первое'
            print(f'{birth_day} {months_by_text[birth_month]} {birth_year}')
        else:
            score+=1

    print(f'Верных ответов: {score}. Неверных: {5-score}')
    if 'да'!=input('Наберите \"да\", если хотите попробовать еще:'):
        raise SystemExit(1)
