from human import Human
from house import House, SmallHouse


def main():
    # Создание различных домов.
    cottage = House(100, 100000)
    villa = House(500, 500000)
    residence = House(2500, 2500000)

    # 1. Вызов справочного метода default_info() для класса Human.
    print('\n--- default_info ---')
    Human.display_default_info()

    # 2. Создание объекта класса Human.
    vladimir = Human('Vladimir', 22)

    # 3. Вывод справочной информации о созданном объекте (метод info()).
    print('\n--- info ---')
    vladimir.display_info()

    # 4. Создание объекта класса SmallHouse.
    bungalow = SmallHouse(50000)

    print(f'\n--- earn_money ---')
    vladimir.earn_money(20000.0)

    # 5. Попытка купить дом, получение предупреждения.
    # print(f'\n--- buy_house ---')
    # vladimir.buy_house(bungalow, 5)

    print('\n--- info ---')
    vladimir.display_info()

    # 6. Зарабатываем денег.
    print(f'\n--- earn_money ---')
    vladimir.earn_money(250000.0)

    print('\n--- info ---')
    vladimir.display_info()

    # 7. Снова пробуем купить дом.
    print(f'\n--- buy_house ---')
    vladimir.buy_house(cottage, 10)

    # 8. Проверяем состояние объекта vladimir класса Human.
    print('\n--- info ---')
    vladimir.display_info()


if __name__ == '__main__':
    main()
