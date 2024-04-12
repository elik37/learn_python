from utils import get_valid_number


def main() -> None:
    num_collection: list = []
    summa: int = 0

    while True:
        user_number: int = get_valid_number()

        if user_number >= 1:
            num_collection.append(user_number)

        elif user_number == 0:
            for number in num_collection:
                summa = summa + number
            print(f'Результат суммирования введенных чисел: {summa}')
            break


if __name__ == '__main__':
    main()
