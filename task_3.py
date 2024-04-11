def main() -> None:
    nums: list = list(range(1, 11))
    REQUIRED_NUMBER: int = 7

    def num_collection(nums: list) -> None:
        for num in nums:
            if num == REQUIRED_NUMBER:
                print(f'Число {REQUIRED_NUMBER} знайдене')
            else:
                print('Число не вірне')

    num_collection(nums)


if __name__ == '__main__':
    main()
