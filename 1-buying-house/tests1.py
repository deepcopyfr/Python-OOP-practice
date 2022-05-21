from human import Human
from house import House, SmallHouse


def main():
    # Создание различных домов.
    cottage = House(100, 100000)
    villa = House(500, 500000)
    residence = House(2500, 2500000)

    # Создание маленького домика.
    bungalow = SmallHouse(50000)

    # Создание человека.
    vladimir = Human('Vladimir', 22)

    # Тестирование.
    print('\n--- default_info ---')
    Human.display_default_info()

    print('\n--- info ---')
    vladimir.display_info()

    print(f'\n--- earn_money ---')
    vladimir.earn_money(50000.0)

    print(f'\n--- buy_house ---')
    vladimir.buy_house(bungalow, 5)

    print('\n--- info ---')
    vladimir.display_info()

    print(f'\n--- earn_money ---')
    vladimir.earn_money(150000.0)

    print('\n--- info ---')
    vladimir.display_info()

    print(f'\n--- buy_house ---')
    vladimir.buy_house(cottage, 10)

    print('\n--- info ---')
    vladimir.display_info()


if __name__ == '__main__':
    main()
