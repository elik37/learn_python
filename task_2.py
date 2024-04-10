import random
from utils import get_valid_number


def main() -> None:
    random_number: int = random.randrange(1,11)

    while True:
        user_number: int = get_valid_number()

        if user_number > random_number:
            print('Число більше ніж загадане')

        elif user_number < random_number:
            print('Число меньше ніж загадане')

        elif user_number == random_number:
            print('Число вірне')
            break


if __name__ == '__main__':
    main()
