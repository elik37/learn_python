from typing import Optional


num_collection: list = []
summa: int = 0


def get_valid_number() -> int:
    user_number: Optional[int] = None

    while not isinstance(user_number, int):
        try:
            user_number = int(input('Введіть своє число: '))
        except ValueError:
            print('Вы додик')
            continue
        else:
            return user_number


while True:
    user_number: int = get_valid_number()

    if user_number >= 1:
        num_collection.append(user_number)

    elif user_number == 0:
        for number in num_collection:
            summa = summa + number
        print(f'Результат суммирования введенных чисел: {summa}')
        break
