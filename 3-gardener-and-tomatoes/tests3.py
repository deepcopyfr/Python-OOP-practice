from tomatobush import TomatoBush
from gardener import Gardener


def main():
    # 1. Вызов справки по садоводству.
    Gardener.display_knowledge_base()

    print('-' * 110)

    # 2. Создание объектов класса TomatoBush и Gardener.
    small_bush = TomatoBush(2)
    gardener = Gardener('Vladimir', small_bush)

    print()
    print()

    small_bush.display_info()
    print()

    # 3. Используя объект класса Gardener, поухаживаем за кустом с помидорами.
    gardener.work()
    small_bush.display_info()
    print()

    gardener.work()
    small_bush.display_info()
    print()

    # 4. Сбор урожая.
    gardener.harvest()

    # 5. Томаты ещё не созрели. Продолжаем ухаживать за ними.
    gardener.work()
    small_bush.display_info()
    print()

    # 6. Сбор урожая.
    gardener.harvest()


if __name__ == '__main__':
    main()
