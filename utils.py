from typing import Optional


def get_valid_number() -> int:
    """
    Функция запрашивает у пользователя ввод целого числа и возвращает его.
    А также предотвращает ошибки, например если пользователь ввел букву, или символ
    Returns:
        int: Введенное пользователем целое число.
    """
    user_number: Optional[int] = None

    while not isinstance(user_number, int):
        try:
            user_number = int(input('Введіть своє число: '))
        except ValueError:
            print('Ви помилились, спробуйте ще раз')
            continue
        else:
            return user_number
