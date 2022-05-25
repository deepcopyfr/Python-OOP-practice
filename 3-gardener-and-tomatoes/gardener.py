from tomato import Tomato
from tomatobush import TomatoBush

from string import ascii_letters


class Gardener:
    """
    Класс 'Gardener' предназначен для создания садовника, который может ухаживать за помидорами.

    Attributes:
        name(str): Имя садовника.
        plant(TomatoBush): Куст с помидорами.

    Methods:
        work: Позволяет садовнику работать из-за чего растение становится более зрелым.
        harvest: Собирает урожай, если все плоды созрели.
        display_knowledge_base: Выводит справку по садоводству.

    """

    ### Основные методы ###

    def __init__(self, name: str, plant: TomatoBush):
        self.__verify_name(name)
        self.__verify_plant(plant)

        self.name = name
        self._plant = plant

    def work(self):
        """Позволяет садовнику работать из-за чего растение становится более зрелым."""
        self._plant.grow_all()
        print("Садовник поработал\n")

    def harvest(self):
        """Собирает урожай, если все плоды созрели."""
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран\n\n")
        else:
            print("Вы пытаетесь собрать урожай, но не можете это сделать... "
                  "Плоды ещё не созрели\n\n")

    @staticmethod
    def display_knowledge_base():
        """Выводит справку по садоводству."""
        gardening_guide = f"""
        \t\tСправка по садоводству\n
        {Tomato.__doc__} {TomatoBush.__doc__} {Gardener.__doc__}"""
        print(gardening_guide)

    ### Вспомогательные методы ###

    @staticmethod
    def __verify_name(name: str) -> None:
        """Проверяет корректность ввода имени."""
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")

        if len(name) < 1:
            raise TypeError("Имя должно состоять хотя бы из 1 буквы")

        for letter in name:
            if letter not in ascii_letters:
                raise TypeError("Имя должно состоять из букв латинского алфавита")

    @staticmethod
    def __verify_plant(plant: TomatoBush):
        """Проверяет корректность ввода куста с помидорами."""
        if not isinstance(plant, TomatoBush):
            raise TypeError("Растение должно быть кустом с помидорами")
