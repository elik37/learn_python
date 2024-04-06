# Напишите функцию greet, которая принимает имя пользователя в качестве аргумента и
# выводит приветственное сообщение вида "Привет, [имя]!".

# def greet(name: str):
#     return f'Привет {name}'
#
# print(greet(name="Elik"))

# Напишите функцию count_vowels, которая принимает строку в качестве аргумента
# и возвращает количество гласных букв в этой строке.
text: str = "Helli Elik"

def count_vowels(string: str) -> None:
    VOWELS: str = 'aeiouAEIOU'
    count: int = 0

    for letter in string:
        if letter in VOWELS:
            count = count + 1

    print(count)

count_vowels(string=text)

def print_player_name(name: str):
    text = f'Futboler: {name}'
    print(text)

player_1 = 'Ronaldo'
print_player_name(name=player_1)

player_2 = 'Messi'
print_player_name(name=player_2)

player_3 = 'Neymar'
print_player_name(name=player_3)

player_4 = 'Ibrahimovic'
print_player_name(name=player_4)

player_5 = 'Shevchenko'
print_player_name(name=player_5)
