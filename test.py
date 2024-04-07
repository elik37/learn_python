# нап ф кот принимает число и воз это же число во 2 степени
# нап ф кот принимает 2 числа и воз их умножение
# нап ф кот принимает имя и воз текст "Привет имя" если имя не Дмитрий,
# а если Дмитрий то "имя Гондон"
# нап ф кот принимает имя и воз текст "имя - жинка" если имя женское, и "имя - музек" если имя мужское
# нап ф кот принимает 3 аргумента, первые 2 это числа, 3 аргумент это команда, команда может быть след типов:
# "умножение" и "сумма" в зависимости от команды делать это действие с 2 числами

def get_accepted_number(num: int) -> int:
    degree = num ** 2
    return degree

number = 55
result = get_accepted_number(num=number)
print(result)


def get_accepted_number(num_1: int, num_2: int) -> int:
    multiplication = num_1 * num_2
    return multiplication

number_1 = 234
number_2 = 576
res_mul = get_accepted_number(num_1=number_1, num_2=number_2)
print(res_mul)


def get_accepted_name(name: str) -> str:
    text_1 = f'Привет {name}'
    text_2 = ''
    if name == 'Дмитрий':
        text_2 = 'Гондон'
    return text_1 + ' ' + text_2

name_human = 'Дмитрий'
result = get_accepted_name(name=name_human)
print(result)


def get_human_name(name: str) -> str:
    text_1 = ''
    text_2 = ''
    if name[-1] in 'aeiou':
        text_2 = f'{name} - Жинка'
    else:
        text_1 = f'{name} - Хуемраз'
    return text_1 or text_2

name_1 = 'Viktoria'
res = get_human_name(name=name_1)
print(res)


def get_accepted_number(num_1: int, num_2: int, summation: str) -> int:
    if summation == 'Сумма':
        result = num_1 + num_2
    elif summation == 'Умножение':
        result = num_1 * num_2
    return result

number_1 = 3
number_2 = 6
result = 'Умножение'
fin_result = get_accepted_number(num_1=number_1, num_2=number_2, summation=result )
print(fin_result)
